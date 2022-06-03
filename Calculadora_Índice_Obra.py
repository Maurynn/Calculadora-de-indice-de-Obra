from tkinter import *

janela = Tk()
janela.title('By: Mauro Alves')
janela.geometry("280x300")
janela.configure(background="#3b3b3b",
                 borderwidth="3",
                 highlightbackground="#ff5706",
                 highlightthickness="2",
                 relief="groove")
janela.resizable(False, False)

# Cálculo Média:


def calcular():
    armacao = armacao_entry.get()
    produtividade = produtividade_entry.get()
    operarios = operarios_entry.get()
    horas = horas_trabalhadas_entry.get()
    calculo = int(produtividade) * int(operarios) * int(horas)
    indice = int(armacao) / int(calculo)

    if indice >= 6 and indice <= 9:
        indice = (f'**Índice calculado igual a {indice:.1f}**\nNão será necessário\naumentar a produção')
    else:
        indice = (f'**Índice calculado igual a {indice:.1f}**\nSerá necessário\naumentar a produção')

    resultado_label['text'] = indice

        # build ui
label = Label(janela)
label.configure(
    background="#ff5706",
    font="{Nirmala UI} 11 {bold}",
    foreground="#ffffff",
    justify="center",
)
label.configure(relief="ridge", text="CÁLCULO DE ÍNDICE DE OBRA", width="100")
label.pack(padx="5", pady="5", side="top")
armacao_label = Label(janela)
armacao_label.configure(
    background="#3b3b3b",
    font="{Arial Baltic} 12 {bold}",
    foreground="#ffffff",
    text="Qtde Armação Kg:",
)
armacao_label.place(anchor="nw", relx="0.0", rely="0.12", x="5", y="11")
armacao_entry = Entry(janela)
armacao_entry.configure(
    borderwidth="3",
    font="{Ebrima} 10 {}",
    highlightbackground="black",
    highlightthickness="1",
)
armacao_entry.configure(
    insertwidth="0", relief="sunken", selectborderwidth="0", width="13"
)
armacao_entry.place(relx="0.62", rely="0.13", width="80", x="17", y="09")
produtividade_label = Label(janela)
produtividade_label.configure(
    background="#3b3b3b",
    font="{Arial Baltic} 12 {bold}",
    foreground="#ffffff",
    text="kg por Hora:",
)
produtividade_label.place(anchor="nw", rely="0.22", x="5", y="19")
produtividade_entry = Entry(janela)
produtividade_entry.configure(
    borderwidth="3",
    font="{Ebrima} 10 {}",
    highlightbackground="black",
    highlightthickness="1",
)
produtividade_entry.configure(width="13")
produtividade_entry.place(
    anchor="nw",
    height="25",
    relx="0.62",
    rely="0.21",
    width="80",
    x="17",
    y="22",
)
operarios_label = Label(janela)
operarios_label.configure(
    background="#3b3b3b",
    font="{Arial Baltic} 12 {bold}",
    foreground="#ffffff",
    text="Qtde de Operários:",
)
operarios_label.place(anchor="nw", rely="0.31", x="5", y="25")
operarios_entry = Entry(janela)
operarios_entry.configure(
    borderwidth="3",
    font="{Ebrima} 10 {}",
    highlightbackground="black",
    highlightthickness="1",
)
operarios_entry.configure(width="13")
operarios_entry.place(
    anchor="nw", height="25", relx="0.62", rely="0.40", width="80", x="17"
)
calcular = Button(janela, command=calcular)
calcular.configure(
    background="#ff5706",
    borderwidth="2",
    font="{Arial CE} 10 {bold}",
    foreground="#ffffff"
)
calcular.configure(relief="raised", text="Calcular ", width="11")
calcular.place(
    anchor="nw", relx="0.0", rely="0.50", width="262", x="5", y="37"
)
horas_trabalhadas_label = Label(janela)
horas_trabalhadas_label.configure(
    background="#3b3b3b",
    disabledforeground="#ffffff",
    font="{Arial Baltic} 12 {bold}",
    foreground="#ffffff",
)
horas_trabalhadas_label.configure(text="Horas Trabalhadas:")
horas_trabalhadas_label.place(anchor="nw", rely="0.42", x="5", y="26")
horas_trabalhadas_entry = Entry(janela)
horas_trabalhadas_entry.configure(
    borderwidth="3",
    font="{Ebrima} 10 {}",
    highlightbackground="black",
    highlightthickness="1",
)
horas_trabalhadas_entry.configure(takefocus=False)
horas_trabalhadas_entry.place(
    anchor="nw",
    height="25",
    relx="0.62",
    rely="0.41",
    width="80",
    x="17",
    y="30",
)
resultado_label = Label(janela)
resultado_label.configure(
    background="#ffffff",
    borderwidth="3",
    font="Arial 11 bold")
resultado_label.configure(
    highlightthickness="2", justify="center", relief="sunken", text=""
)
resultado_label.place(
    anchor="nw", height="72", rely="0.66", width="262", x="5", y="24")

janela.mainloop()
