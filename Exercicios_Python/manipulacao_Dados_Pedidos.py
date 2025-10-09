# Este exericico simula a gestão de pedidos de uma pequena loja
# Objetivo: Criar, armazenar e realizar uma analise básica em uma lista de pedidos. 

historico_pedidos = []
total_faturamento = 0

pedido_1= {
 "id_pedido": 1, 
 "item": "camiseta", 
 "quantidade": 2, 
 "preco_unitario":39.90, 
 "status":"concluido"
}

pedido_2= {
 "id_pedido": 2, 
 "item": "tenis", 
 "quantidade": 1, 
 "preco_unitario":539.90, 
 "status":"concluido"
}

pedido_3= {
 "id_pedido": 3, 
 "item": "calça", 
 "quantidade": 4, 
 "preco_unitario":199.90, 
 "status":"processando"
}

historico_pedidos.extend([pedido_1,pedido_2,pedido_3])

# calculo do faturamento total
print("--- Processando pedidos para cálculo de faturamento ---")
for pedido in historico_pedidos:
    subtotal = pedido["quantidade"] * pedido["preco_unitario"]

    if pedido["status"] == "concluido":
        total_faturamento += subtotal
        print("\n === Seu Historio de pedidos: \n")
        print(f"[CONCLUÍDO] Pedido #{pedido['id_pedido']} de {pedido['item']}. Valor: R$ {subtotal:.2f}")    
    else:
        print(f"\n O Seu Pedido de {pedido["item"]} está {pedido["status"]} \n")

print(f"Faturamento Total da Compra(pedidos concluidos): R$ {total_faturamento:.2f}")
