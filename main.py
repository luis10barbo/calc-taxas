import customtkinter
from tkinter import messagebox

from calculadora import calcular_taxas # pyright: ignore[reportMissingTypeStubs]
estado = {"modo_venda": True}
def main():
    app = customtkinter.CTk()
    app.geometry("640x480")
    app.grid_columnconfigure(1, weight=1)

    button: customtkinter.CTkButton
    def trocar_label():
        label.configure(text=f"Digite um valor de {"venda" if estado['modo_venda'] else "compra"} que você deseja.") # pyright: ignore[reportUnknownMemberType]

    def trocar_modo():
        modo = estado["modo_venda"]
        estado["modo_venda"] = not modo
        if modo:
            button.configure(text="Trocar para Modo Venda") # pyright: ignore[reportUnknownMemberType]
        else:
            button.configure(text="Trocar para Modo Compra") # pyright: ignore[reportUnknownMemberType]
        trocar_label()

    button = customtkinter.CTkButton(app, text="Trocar para Modo Compra", command=trocar_modo)
    button.grid(row=0, column=0, padx=10, pady=10) # pyright: ignore[reportUnknownMemberType]

    label = customtkinter.CTkLabel(app)
    label.grid(row=1, column=0, padx=10, pady=10) # pyright: ignore[reportUnknownMemberType]
    trocar_label()

    label_taxa = customtkinter.CTkLabel(app, text="Taxa de profit (ex: 5 para 5%)")
    label_taxa.grid(row=3, column=0, padx=10, pady=10) # pyright: ignore[reportUnknownMemberType]

    input_valor = customtkinter.CTkTextbox(app, height=30, padx=10, pady=5, )
    input_valor.grid(row=2, column=0)

    input_taxa = customtkinter.CTkTextbox(app, height=30, padx=10, pady=5)
    input_taxa.grid(row=4, column=0, padx=(10, 0))

    def calcular():
        valor_string = input_valor.get("1.0", "end-1c")
        taxa_string = input_taxa.get("1.0", "end-1c")
        try:
            valor = float(valor_string)
            taxa = float(taxa_string)
            resultado = calcular_taxas(modo_venda=estado["modo_venda"], porcentagem_profit=taxa, valor=valor)
            if estado["modo_venda"]:
                label.configure(text=f"Compre por: ${round(resultado.resultado, 2)} (profit: ${round(resultado.profit, 2)}) (saldo pos taxa: ${round(resultado.resultado_pos_taxa, 2)})")
            else:
                label.configure(text=f"Venda por: ${round(resultado.resultado, 2)}  (profit: ${round(resultado.profit, 2)}) (saldo pos taxa: ${round(resultado.resultado_pos_taxa, 2)})")

        except:
            messagebox.showerror("Erro em input", "Você deve inserir um valor numérico válido em inputs taxa e valor (utilize . em vez de virgulas)")

    button_calcular = customtkinter.CTkButton(app, text="Calcular", command=calcular)
    button_calcular.grid(row=5, column=0, padx=10, pady=10) # pyright: ignore[reportUnknownMemberType]

    app.mainloop() # pyright: ignore[reportUnknownMemberType]
    
    


main()
    
    