# EXCEÇÕES MAIS COMUNS 

# FileNotFoundError: arquivo ou diretório não encontrado
# PermissionError: sem permissão para acessar o arquivo ou diretório
# IsADirectoryError: tentou-se abrir um diretório como se fosse um arquivo
# NotADirectoryError: tentou-se acessar um arquivo como se fosse um diretório
# IOError: erro genérico de entrada/saída (problema de permissaõ, falta de espaço em disco etc)
# unicodeDecodeError: erro ao decodificar dados de um arquivo (encoding errado)


# codigo padrao para tratar erros ao manipular arquivos
from pathlib import Path
ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "arquivo_inexistente.txt" / "novo.txt" ,"r")
except FileNotFoundError as exc: # informar qual erro ocorreu e capturar a exceção em uma variável
    print(f"Arquivo ou diretório não encontrado.{exc}") # exibe a mensagem do erro
except IsADirectoryError as exc:
    print(f"Era esperado um arquivo, mas um diretório foi fornecido.{exc}")
except IOError as exc:
    print(f"Erro de entrada/saída ao manipular o arquivo.{exc}")
