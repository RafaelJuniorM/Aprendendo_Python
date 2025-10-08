 #  metodos listas em python 

## APPEND - Adiciona um elemento ao final da lista
lista = []
lista.append(1)
lista.append("ola mundo!!")
lista.append([2,3,4])
print(lista[2][1])

print('=====================')
## CLEAR - Remove todos os elementos da lista
lista.clear()
print(lista)

print('=====================')
## COPY - Retorna uma cópia da lista
lista = [1,2,3,4,5]
lista.copy()
print(lista)

print('=====================')
## COUNT - Retorna o número de ocorrências de um elemento na lista
cores = ['azul', 'verde', 'amarelo', 'azul', 'vermelho', 'azul']
print(cores.count("azul"))
print(cores.count("amarelo"))

print('=====================')
## EXTEND - Estende a lista adicionando todos os elementos de um iterável (lista, tupla, dicionário, etc.)
times_brasileiro = ["galo", "santos", "palmeiras"]
print(times_brasileiro)
times_brasileiro.extend(["flamengo", "vasco"])
print(times_brasileiro)

print('=====================')
## INDEX - Retorna o índice do primeiro elemento com o valor especificado
print(times_brasileiro.index("santos")) 

print("=====================")
## POP - Remove o elemento no índice especificado e o retorna. Se nenhum índice for especificado, remove e retorna o último item da lista
print(times_brasileiro.pop())
print(times_brasileiro)
print(times_brasileiro.pop(1))
print(times_brasileiro)

print('=====================')
## REMOVE - Remove a primeira ocorrência do elemento com o valor especificado
times_brasileiro.remove("flamengo")
print(times_brasileiro) 

print('=====================')
## REVERSE - Inverte a ordem dos elementos na lista
times_brasileiro.reverse()
print(times_brasileiro)

print('=====================')
## SORT - Ordena os elementos da lista
numeros_aleatorios = [10, 20,32, 55, 78, 99, 120, 2, 7,300]
print(numeros_aleatorios)
numeros_aleatorios.sort()
print(numeros_aleatorios)
numeros_aleatorios.sort(reverse=True)
print(numeros_aleatorios)
cores.sort(key=lambda x: len(x))
print(cores)

print('=====================')
#LEN - Retorna o número de elementos na lista
print(len(cores))

print(n**2 if n > 6 else n for n in range(10) if n % 2 == 0)