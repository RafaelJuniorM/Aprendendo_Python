# Catalogo de produtos e tags unicas 
# Exircio que simula a gestao de produtos e o processamento de listas de codigos unicos(tags)
# OBJETIVO: Organizar um catálogo usando um dicionario e extrair dados unicos usando conjuntos 


catalago_produtos = {
    "panelas": {
        "estoque": 50,
        "preco": 39.90,
        "tags": ["cozinha"]
    },
    "Pneu - Aro 20": {
        "estoque": 20,
        "preco": 199.90,
        "tags": ["automotivo"]
    },
    "microondas": {
        "estoque": 15,
        "preco": 499.90,
        "tags": ["cozinha",]
    },
    "geladeira": {
        "estoque": 0,
        "preco": 1999.90,
        "tags": ["eletrodomesticos"]
    },
    "celular": {
        "estoque": 5,  
        "preco": 999.90,
        "tags": ["eletronicos"]
    }
}

def verificar_estoque(nome_produto: str, quantidade_produto: int) -> bool:
    if nome_produto not in catalago_produtos:
        return False
    
    # 2. Agora é seguro acessar o estoque, pois a existência já foi verificada
    estoque_atual = catalago_produtos[nome_produto]["estoque"]
    
    # Retorna True se a quantidade desejada for menor ou igual ao estoque
    return quantidade_produto <= estoque_atual

    

def verificar_tags_unicas():
    tags_unicas = set()
    for produto in catalago_produtos.values():
        tags_unicas.update(produto["tags"])
    return tags_unicas


## Executar 
produto_checar = "celular"
quantidade_comprar = 1
disponivel = verificar_estoque(produto_checar, quantidade_comprar)

print("-" * 40)
print(f"VERIFICAÇÃO DE DISPONIBILIDADE:")

if disponivel:
    # se possui produto e quantidade suficiente
    print(f"O produto '{produto_checar}' está disponível em quantidade suficiente ({quantidade_comprar} unidades).")
else:
   # Verifica o motivo da indisponibilidade para dar uma mensagem clara
    if produto_checar not in catalago_produtos:
        print(f"FALHA: O produto '{produto_checar}' não foi encontrado no catálogo.")
    else:
        estoque = catalago_produtos[produto_checar]["estoque"]
        print(f"FALHA: O produto '{produto_checar}' não está disponível em quantidade suficiente ({quantidade_comprar} unidades).")
        print(f"Temos em estoque: {estoque} unidades.")

# --- Teste de Tags Únicas ---
tags_finais = verificar_tags_unicas()

print("\n" + "=" * 40)
print(f"TOTAL DE TAGS ÚNICAS NO CATÁLOGO ({len(tags_finais)}):")
print(sorted(list(tags_finais)))
print("=" * 40)