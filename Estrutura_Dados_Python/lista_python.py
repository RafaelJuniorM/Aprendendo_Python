# CRIANDO LISTA EM PYTHON
lista = [1, 2, 3, 4, 5]
print(lista )
print("============ ")
letras = list("python")
print(letras)
print("============ ")
numeros = list(range(11))
print(numeros)
print("============ ")
# ACESSANDO ELEMENTOS DA LISTA
print(lista[0])  # Primeiro elemento
print("============ ")
# LISTAS ANINHADAS
matriz = [
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]
]
print(matriz[1][2])  # Acessa o elemento 6
print("============ ")
# PERCORRENDO LISTA COM FOR
carros = ["Ford", "Volvo", "BMW"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# CRIANDO NOVA LISTA ATRAVES DE UM "FILTRO"
print("============ ")
print("Versao numero 1 - como fazer um filtro ")
numeros = [2, 8,10, 15, 27,31,45,34, 89]
pares = []
for numero in numeros: 
  if numero % 2 == 0:
    pares.append(numero)
print(pares)

print("Versao numero 2 - como fazer um filtro ")
pares2 = [num for num in numeros if num % 2 == 0]
print(pares2)