taxa_profit = 0.95
modo_venda = True
while True:
    try:
        resposta = input(f"Digite valor {"venda" if modo_venda else "compra"} que vc deseja ('q'/'t'/'c') ({100 - taxa_profit * 100} %): ")
        resposta_sanitizada = resposta.replace(" ", "").capitalize()
        if resposta_sanitizada == "Q":
            break
        if resposta_sanitizada == "C":
            modo_venda = not modo_venda
            continue
        if resposta_sanitizada == "T":
            resposta = input("Digite a taxa de profit que vc deseja (ex 5): ")
            taxa_profit = 1 - float(resposta) / 100
            continue
        valor_venda = float(resposta)
        valor_compra = float(resposta)
    except:
        print("Valor venda nao numerico")
        continue
    if (modo_venda):
        valor_compra_min = valor_venda * 0.98
        valor_compra = valor_compra_min * taxa_profit
        venda_pos_taxa = valor_venda * 0.98
        montante = valor_venda + venda_pos_taxa - valor_compra
        print(f"Valor venda: ${valor_venda} (pos taxa: ${round(venda_pos_taxa, 2)}) (profit: ${round(venda_pos_taxa - valor_compra, 2)}) (min: ${round(valor_compra_min)}) (montante: {round(montante, 2)})")
        print(f"Compre por: ${round(valor_compra, 2)}")
    else:
        valor_venda_min = valor_compra / 0.98
        valor_venda = valor_venda_min / taxa_profit
        venda_pos_taxa = valor_venda * 0.98
        montante = valor_venda + venda_pos_taxa - valor_compra
        print(f"Valor compra: ${valor_compra}")
        print(f"Venda por: ${round(valor_venda, 2)} (pos taxa: ${round(venda_pos_taxa, 2)}) (profit: ${round(venda_pos_taxa - valor_compra, 2)}) (min: ${round(valor_venda_min)}) (montante: {round(montante, 2)}")
        

    
    