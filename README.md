## Organizador de Arquivos 📂

Se você é assim como eu, uma pessoa que gosta de organização, já deve notar que quando usamos o PC, acabamos por ter muitos arquivos de todos os tipos e extensões.

Pensando nisso, porque não automatizar isso tudo invés de mover cada arquivo pro seu lugar?

Script criado em python, onde organiza todos os arquivos de uma pasta, movendo-os para uma subpasta de acordo com seu tipo.
- Organiza arquivos automaticamente em subpastas por categoria
- Possui modo Simulação, mostrando o que será feito antes de executar
- Gera logs dos arquivos movidos, com data, hora e nome do arquivo
- Não sobrevescreve, arquivos com nomes repetidos adiciona uma marcação para separá-los
- Fácil customização e roda de acordo com a pasta ativa no CMD

# Como utilizar?
- Deve-se ter Python 3.8 ou superior (não usei nenhuma biblioteca externa)

### Testar sem mexer em nada (Modo Simulação)
python organizar_pastas.py "C:/Users/admin/Pasta_teste" --simular

### Execução real
python organizar_pastas.py "C:/Users/admin/Pasta_teste"

## ⚙ Como funciona?
Lê os arquivos e indentifica as extensões, cria as subpastas e move de acordo com o que foi configurado em "Categorias", no início do Script. Os Logs server pra analisar e validar para onde foi cada arquivo.


#### Autora 👩‍💻
Brenda Schlosser Peters - [Meu Linkedin](https://www.linkedin.com/in/brendayyyy/)