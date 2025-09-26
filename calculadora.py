from dataclasses import dataclass
from matematica import porcento_subtracao

@dataclass
class Taxas:
    resultado: float
    resultado_pos_taxa: float
    input: float
    profit: float

PORCENTAGEM_TAXA_VENDA_CSFLOAT = 2
def calcular_taxas(modo_venda: bool, porcentagem_profit: float, valor: float):
    
    if (modo_venda):
        # Inserido valor que usuario deseja de venda, calcule o valor de compra para que tenha profit
        resultado_min = valor * porcento_subtracao(PORCENTAGEM_TAXA_VENDA_CSFLOAT)
        resultado = resultado_min * porcento_subtracao(porcentagem_profit)
        profit = resultado_min - resultado

        return Taxas(resultado=resultado, input=valor, resultado_pos_taxa=resultado_min, profit=profit)
    else:
        # Inserido 'valor' que usuario deseja de compra, calcule o valor de venda para que tenha profit 'taxa_profit'
        valor_venda = valor / porcento_subtracao(PORCENTAGEM_TAXA_VENDA_CSFLOAT) / porcento_subtracao(porcentagem_profit)
        resultado_min = valor_venda * porcento_subtracao(PORCENTAGEM_TAXA_VENDA_CSFLOAT)
        resultado = resultado_min * porcento_subtracao(porcentagem_profit) 
        profit = resultado_min - resultado

        return Taxas(resultado=valor_venda, input=valor, resultado_pos_taxa=resultado_min, profit=profit)