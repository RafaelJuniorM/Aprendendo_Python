nome = "rAfAeL"

print(nome.upper())  # R A F A E L
print(nome.lower())  # r a f a e l  
print(nome.title())  # R A F A E L

## Eliminando espaçoes em branco
print(" \n === Eliminando espaços em branco === \n ")
texto = "   Olá, Mundo!    "

print(texto.strip())   # "Olá, Mundo!"
print(texto.lstrip())  # "Olá, Mundo!    "  
print(texto.rstrip())  # "   Olá, Mundo!"


## junçao e separação de strings
print(" \n === Junção e separação de strings === \n ")
menu = "python"

print(menu.center(20,"@"))
print("-".join(menu))

## Interpolação de strings
print(" \n === Interpolação de strings === \n")
nome2 = "Livia"
idade = 40
saldo = 49.765789
dados = {"nome": "Ana", "idade": 30}

print("A {nome} tem {idade} anos.".format(**dados))

print("A {} tem {} anos.".format(nome2, idade))

print(f"A {nome2} tem {idade} anos saldo: {saldo:.2f}. \n")

## strings triplas 

print(" \n === Strings triplas === \n")
mensagem = """Olá,
    Tudo bem? 
        Seja bem-vindo(a)!
    Abraços,
Rafael
""" 
print(mensagem)