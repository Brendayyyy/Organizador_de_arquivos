import argparse
import logging
import shutil
from pathlib import Path
from datetime import datetime

# Possivel editar/expandir conforme a necessidade
CATEGORIAS = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Documentos": [".docx", ".doc", ".txt"],
    "Apresentacoes": [".pptx", ".ppt"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Audio": [".mp3"],
    "Video": [".mp4", ".avi"],
}

def configurar_log(pasta_destino: Path) -> Path:
    """Configura o log"""
    pasta_destino.mkdir(parents=True, exist_ok=True)
    caminho_log = pasta_destino / "log_pastas.txt"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        handlers=[
            logging.FileHandler(caminho_log, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    return caminho_log

def categoria_do_arquivo(arquivo: Path) -> str:
    extensao = arquivo.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"

def organizar_pasta(pasta_origem: Path, simular: bool = False) -> dict:
    """Organiza os arquivos da pasta de origem em subpastas por categoria"""
    if not pasta_origem.exists():
        raise FileNotFoundError(f"A pasta '{pasta_origem}' não existe.")

    resumo = {}
    arquivos = [f for f in pasta_origem.iterdir() if f.is_file()]
    arquivos = [f for f in arquivos if f.name != "log_pastas.txt"]

    if not arquivos:
        logging.info("Arquivo não encontrado para organizar em '%s'.", pasta_origem)
        return resumo

    for arquivo in arquivos:
        categoria = categoria_do_arquivo(arquivo)
        pasta_categoria = pasta_origem / categoria

        if simular:
            logging.info("[SIMULAÇÃO] '%s' seria movido para '%s/'", arquivo.name, categoria)
        else:
            pasta_categoria.mkdir(exist_ok=True)
            destino = pasta_categoria / arquivo.name

            if destino.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                destino = pasta_categoria / f"{arquivo.stem}_{timestamp}{arquivo.suffix}"

            shutil.move(str(arquivo), str(destino))
            logging.info("'%s' movido para '%s/'", arquivo.name, categoria)

        resumo[categoria] = resumo.get(categoria, 0) + 1

    return resumo

def exibir_resumo(resumo: dict, simular: bool) -> None:
    """Exibe um resumo final da organização."""
    acao = "seriam organizados" if simular else "foram organizados"
    total = sum(resumo.values())

    print("\n" + "=" * 40)
    print(f"RESUMO: {total} arquivo(s) {acao}")
    print("=" * 40)
    for categoria, quantidade in sorted(resumo.items()):
        print(f"  {categoria}: {quantidade}")
    print("=" * 40 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Organiza arquivos de uma pasta em subpastas por tipo (PDFs, Imagens, etc)."
    )
    parser.add_argument(
        "pasta",
        type=str,
        help="Caminho da pasta que será organizada (ex: C:/Users/admin/Downloads)",
    )
    # No comando, rodando com --simular, ele apenas mostra o que seria feito sem mover os arquivos
    parser.add_argument(
        "--simular",
        action="store_true",
        help="Mostra o que seria feito sem mover os arquivos",
    )

    args = parser.parse_args()
    pasta_origem = Path(args.pasta).expanduser().resolve()

    configurar_log(pasta_origem)

    if args.simular:
        logging.info("Modo SIMULAÇÃO (nenhum arquivo será movido)")

    resumo = organizar_pasta(pasta_origem, simular=args.simular)
    exibir_resumo(resumo, simular=args.simular)

if __name__ == "__main__":
    main()

"""Autora: Brenda Schlosser Peters"""