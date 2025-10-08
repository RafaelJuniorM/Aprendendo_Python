## metodos SETs

# Conjuntos (sets) em Python são coleções não ordenadas de elementos únicos. 
# Eles são úteis para armazenar itens distintos e realizar operações matemáticas como união, interseção e
# diferença. 
# Criação de um conjunto
meu_conjunto = {1, 2, 3,7}
meu_conjunto2 = set([1, 2, 3,4,5])

# Union (união)
print(meu_conjunto.union(meu_conjunto2))  # Resultado: {1, 2, 3, 4, 5}

# Intersection (interseção)
print(meu_conjunto.intersection(meu_conjunto2))  # Resultado: {1,2,3}

# Difference (diferença)

print(meu_conjunto2.difference(meu_conjunto))  # Resultado: {4, 5}
print(meu_conjunto.difference(meu_conjunto2))  # Resultado: {7}

#symmetric_difference (diferença simétrica)
print(meu_conjunto.symmetric_difference(meu_conjunto2))  # Resultado: {4, 5, 7}

# issubset (subconjunto)
print(meu_conjunto.issubset(meu_conjunto2))  # Resultado: False
print(meu_conjunto2.issubset(meu_conjunto))