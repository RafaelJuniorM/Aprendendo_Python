idade_para_cnh = 18
idade_user = int(input("Digite sua idade: "))

if idade_user < idade_para_cnh:
    print("Você não possui idade para tirar a CNH")
elif idade_user >=25:
    print("Parabens!! \n Voce esta esta apto para tirar sua CNH de Caminhão.")    
else:
    print("Parabens!! \nVocê pode tirar a CNH")