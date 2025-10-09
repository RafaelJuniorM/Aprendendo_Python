
## *ARGS e **KWARGS 

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n ".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "25 de Dezembro de 2023",
    "Hoje é um dia especial",
    "É Natal",
    autor="João da Silva",
    local="Brasil"
)