# ITERADOR 
# Objeto que permite percorrer (iterar) uma coleção de dados (listas, tuplas, dicionários, etc.)
# Possui dois métodos principais: 
#       __iter__()  => retorna o próprio iterador 
#       __next__()  => retorna o próximo valor da coleção

numeros = [1, 2, 3]

iterador = iter(numeros)

print(iter(iterador))

print(next(iterador))
print(next(iterador))
print(next(iterador))


# Vantagens de usar iteradores:
# 1. Eficiência de memória: não é necessário carregar toda a coleção na memória.
# 2. Consigo decidir quando quero o próximo valor
