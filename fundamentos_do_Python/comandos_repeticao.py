## FOR 
for numero in range(1, 6):
    print(numero, end=' ' "\n")

for multiplo_5 in range(5, 51, 5):
    print(multiplo_5, end=' ') 


## WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Depositar\n[0] Sair\n"))

    if opcao == 1:
        print("Saque realizado")    
    elif opcao == 2:
        print("Depósito realizado")
else: 
    print("Volte sempre!")
