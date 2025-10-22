import os
import shutil
from pathlib import Path   

ROOT_PATH = Path(__file__).parent # pega o caminho do diretório atual

# Criar um novo diretório
os.mkdir(ROOT_PATH / "exemplo_diretorio_criado")

#arquivo = open(ROOT_PATH / "novo_diretorio.txt", "w")
#arquivo.close()

#renomeando o arquivo
os.rename(ROOT_PATH / "novo_diretorio.txt", ROOT_PATH / "arquivo_renomeado.txt")

#removendo o arquivo
os.remove(ROOT_PATH / "novo_diretorio.txt")

# movendo o diretório
shutil.move(ROOT_PATH / "texto.txt", ROOT_PATH / "exemplo_diretorio_criado" / "texto.txt")