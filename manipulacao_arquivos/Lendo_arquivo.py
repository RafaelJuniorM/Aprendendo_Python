arquivo = open("D:/Aulas/Python/Aprendendo_Python/manipulacao_arquivos/texto.txt", "r", encoding="utf-8")

#print(arquivo.read())# lendo todo o conteudo do arquivo
#print(arquivo.readline()) # lendo linha por linha
print(arquivo.readlines()) # lendo todas as linhas e retornando uma lista

arquivo.close()