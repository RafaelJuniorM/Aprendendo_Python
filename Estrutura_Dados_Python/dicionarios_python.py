## DICIONARIO EM PYTHON
# Dicionários são estruturas de dados que armazenam pares de chave-valor.

pessoa = {
    "nome":"João", 
    "idade": 30, 
    "cidade":"São Paulo"
}
print(pessoa["cidade"]) # Acessa o valor associado à chave "cidade"

# Adiciona um novo par chave-valor
pessoa["profissão"] = "Engenheiro"
pessoa["idade"] = 31  # Atualiza o valor associado à chave "idade"
print(pessoa)
print("=======================")
contatos = {
    "user_1": {"nome": "Maria", "telefone": "1234-5678"},
    "user_2": {"nome": "Pedro", "telefone": "9876-5432"},
    "user_3": {"nome": "Ana", "telefone": "5678-1234"}
}

print(contatos["user_2"]["telefone"])  # Acessa o telefone do user_2
print("=======================")

# interar sobre um dicionario
for chave, valor in contatos.items():
    print(chave, valor)
print("=======================")

# FROMKEYS - adiciona chaves com valor padrão

print(dict.fromkeys(["sexo", "altura"]))
print(dict.fromkeys(["sexo", "altura"], "não definido"))
print("=======================")

# GET  - acessa o valor de uma chave, se não existir retorna None ou valor padrão
print(contatos.get("user_4"))  # Retorna None
print(contatos.get("user_3"))
print(contatos.get("user_4","user não encontrado"))  # Retorna "user não encontrado"

print("=======================")

# POP - remove o item com a chave especificada e retorna o valor

print(contatos.pop("user_2"))
print(contatos)
print("=======================")

# SETDEFAULT - se a chave não existir, adiciona a chave com o valor padrão
print(contatos.setdefault("user_4", {"nome": "Lucas", "telefone": "1111-2222"}))
print(contatos.setdefault("user_5", {"nome": "Carlos", "telefone": "3333-4444"}))  

print("=======================")

# IN - verifica se a chave existe no dicionário
print("user_1" in contatos)  # True
print("user_6" in contatos)  # False
print("sexo" in contatos["user_1"])