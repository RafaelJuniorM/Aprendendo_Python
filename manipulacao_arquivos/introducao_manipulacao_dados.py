# Arquivos meio de armazenar e recuperar dados; 
# Atraves da manipulação de arquivos, podemos persistir dados 

# abrindo e fechando arquivos
arquivo = open('dados.txt', 'w')  # 'w' para escrita (write)

arquivo.close()  # sempre fechar o arquivo após o uso

# Difentes modos de abrir arquivos
# 'r' - leitura (read)
arquivo = open('dados.txt', 'r') 
# 'w' - escrita (write)
arquivo = open('dados.txt', 'w') 
# 'a' - anexar (append)
arquivo = open('dados.txt', 'a') 