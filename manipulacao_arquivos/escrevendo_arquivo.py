arquivo = open("D:/Aulas/Python/Aprendendo_Python/manipulacao_arquivos/texto.txt", "w", encoding="utf-8")

arquivo.write("Primeira linha do arquivo.\n")
arquivo.write("Segunda linha do arquivo.\n")
arquivo.writelines(["Terceira linha do arquivo.\n", "Quarta linha do arquivo.\n"])
arquivo.close()