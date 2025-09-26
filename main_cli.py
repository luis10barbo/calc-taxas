from calculadora import calcular_taxas

def profit_compra_venda_valor_especifico():
    while True:
        try:
            resposta_compra = input(f"Digite o valor inicial de compra: ")
            resposta_compra_sanitizada = resposta_compra.replace(" ", "").capitalize()
            if resposta_compra_sanitizada == "Q":
                break

            valor_compra = float(resposta_compra)

            while True:
                resposta_venda = input(f"Digite o valor de venda: ")
                resposta_venda_sanitizada = resposta_venda.replace(" ", "").capitalize()
                if resposta_venda_sanitizada == "Q":
                    break
                valor_venda = float(resposta_venda)

                venda_com_taxa = (valor_venda * 0.98)
                profit = venda_com_taxa - valor_compra
                print(f"Profit {round(profit, 2)} (venda com taxa: {round(venda_com_taxa, 2)})")
        except:
            print("Valor venda nao numerico")
            continue

def menu_cli():
    porcentagem_profit = 5
    modo_venda = True
    while True:
        try:
            resposta = input(f"Digite valor {"venda" if modo_venda else "compra"} que vc deseja ('q'/'t'/'c'/'e') ({porcentagem_profit} %): ")
            resposta_sanitizada = resposta.replace(" ", "").capitalize()
            if resposta_sanitizada == "Q":
                break
            if resposta_sanitizada == "C":
                modo_venda = not modo_venda
                continue
            if resposta_sanitizada == "E":
                profit_compra_venda_valor_especifico()
                continue
            if resposta_sanitizada == "T":
                resposta = input("Digite a taxa de profit que vc deseja (ex 5): ")
                porcentagem_profit = float(resposta)
                continue
            valor_venda = float(resposta)
            valor_compra = float(resposta)
        except:
            print("Valor venda nao numerico")
            continue
        if (modo_venda):
            resultado = calcular_taxas(True, porcentagem_profit=porcentagem_profit, valor=valor_venda)
            print(f"Compre por: ${round(resultado.resultado, 2)} (profit: ${round(resultado.profit, 2)}) (saldo pos taxa: ${round(resultado.resultado_pos_taxa)})")
        else:
            resultado = calcular_taxas(False, porcentagem_profit=porcentagem_profit, valor=valor_compra)
            print(f"Venda por: ${round(resultado.resultado, 2)}  (profit: ${round(resultado.profit, 2)}) (saldo pos taxa: ${round(resultado.resultado_pos_taxa)})")
        
menu_cli()