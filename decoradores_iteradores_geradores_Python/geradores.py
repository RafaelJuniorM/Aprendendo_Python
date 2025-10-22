# GERADORES
# Uma função que gera uma sequencia de valores sem armazenas todos eles na memória. 
# Entrega um por um, somente quando solicitado.

def gerar_numeros():
    for num in range(1,7):
        print("Irei informar o numero... ")
        yield num  # yield transforma a função em um gerador
        print("estou fazendo um café...")
gerar = gerar_numeros()

print(next(gerar))
print(next(gerar))