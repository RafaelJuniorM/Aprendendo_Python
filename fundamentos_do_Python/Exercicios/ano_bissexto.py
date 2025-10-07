def verificador_ano_bissexto():
    ano = int(input())
    ano_divisel_por_quatro = ano % 4
    ano_divisel_por_cem = ano % 100
    ano_divisel_por400 = ano %400 
  
    if (ano_divisel_por_quatro == 0) and (ano_divisel_por_cem != 0) or (ano_divisel_por400 == 0):
        print("SIM")
    else:
        print("NÃO")
verificador_ano_bissexto()