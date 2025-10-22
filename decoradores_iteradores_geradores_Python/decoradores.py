# DECORADORES EM PYTHON
# Utilizada quando queremos adicionar funcionalidade extra a uma função existente
# ou seja, antes de execuatr a função principal, será executada uma função extra

def meu_decorador(funcao):
    def funcao_decorada():
        print("Algo está acontecendo antes da função ser chamada.")
        funcao()
        print("Algo está acontecendo depois da função ser chamada.")
    return funcao_decorada

@meu_decorador
def ola_mundo():
    print("Olá, Mundo!")

ola_mundo()


def decorador_duplicar(funcao_original):
    def funcao_decorada(*args, **kwargs):
        funcao_original(*args, **kwargs)
        funcao_original(*args, **kwargs)
    return funcao_decorada

@decorador_duplicar
def mostrar_aprendizado(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

mostrar_aprendizado("Python")