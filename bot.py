import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import time

# Função para calcular o IMC


def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

# Função para gerar um diagnóstico com base nos sintomas


def gerar_diagnostico(nome, sexo, peso, altura, sintomas):
    recomendacao = ""
    doenca = "Desconhecida"

    if "dor de cabeça" in sintomas:
        doenca = "Enxaqueca"
    elif "febre alta" in sintomas:
        doenca = "Infecção"
    elif "tosse persistente" in sintomas:
        doenca = "Gripe"

    imc = calcular_imc(peso, altura)
    data_diagnostico = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if imc > 25:
        recomendacao = "Fazer exercícios e dieta"
    else:
        recomendacao = "Mantenha o peso"

    return (
        f"Nome: {nome}\n"
        f"Sexo: {sexo}\n"
        f"Peso: {peso} kg\n"
        f"Altura: {altura} m\n"
        f"Sintomas: {', '.join(sintomas)}\n"
        f"Doença diagnosticada: {doenca}\n"
        f"IMC: {imc}\n"
        f"Recomendação médica: {recomendacao}\n"
        f"Data do diagnóstico: {data_diagnostico}"
    )


def processar_dados():
    nome = entry_nome.get()
    sexo = var_sexo.get()
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira valores numéricos válidos para peso e altura.")
        return

    sintomas = [s for s, var in sintomas_vars.items() if var.get()]

    if not (1 <= len(sintomas) <= 3):
        messagebox.showerror("Erro", "Selecione entre 1 e 3 sintomas.")
        return

    diagnostico = gerar_diagnostico(nome, sexo, peso, altura, sintomas)

    text_diagnostico.config(state=tk.NORMAL)
    text_diagnostico.delete(1.0, tk.END)
    text_diagnostico.insert(tk.END, diagnostico)
    text_diagnostico.config(state=tk.DISABLED)

    # Atualizar chat com o diagnóstico
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"\nDr.Brabo: {nome}, aqui está o seu diagnóstico:\n------------------------------------------\n\n{diagnostico}\n")
    chat_area.config(state=tk.DISABLED)


def enviar_resposta(event=None):
    global etapa
    resposta = entry_resposta.get()
    entry_resposta.delete(0, tk.END)

    if resposta:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Você: {resposta}\n")
        chat_area.config(state=tk.DISABLED)

    if etapa == 0:
        mostrar_mensagem("Dr.Brabo: Olá! Qual é o seu nome?")
        etapa += 1
    elif etapa == 1:
        nome = resposta
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, nome)
        mostrar_mensagem(
            f"Dr.Brabo: Prazer em conhecê-lo, {nome}! Quantos anos você tem?")
        etapa += 1
    elif etapa == 2:
        sexo = resposta.upper()
        mostrar_mensagem(
            "Dr.Brabo: Beleza!!\nDr.Brabo: Qual é o seu sexo? (M/F)")
        etapa += 1
    elif etapa == 3:
        try:
            sexo = resposta
            if sexo == "M" or sexo == "F":
                var_sexo.set(sexo)
        except ValueError:
            mostrar_mensagem("Dr.Brabo: Por favor, digite apenas M ou F")
        var_sexo.set(sexo)
        mostrar_mensagem(
            "Dr.Brabo: Saquei!!\nDr.Brabo: Qual é o seu peso em kg?")
        etapa += 1
    elif etapa == 4:
        try:
            peso = float(resposta)
            entry_peso.delete(0, tk.END)
            entry_peso.insert(0, str(peso))
            mostrar_mensagem("Dr.Brabo: E qual é a sua altura em metros?")
            etapa += 1
        except ValueError:
            mostrar_mensagem(
                "Dr.Brabo: Por favor, insira um valor numérico válido para o peso.")
    elif etapa == 5:
        try:
            altura = float(resposta)
            entry_altura.delete(0, tk.END)
            entry_altura.insert(0, str(altura))
            mostrar_mensagem(
                "Dr.Brabo: Valeu pelas informações.\nDr.Brabo: Agora, por favor, clica no que estiver sentido (mínimo 2, máximo 3).")
            mostra_sintomas()
            etapa += 1
        except ValueError:
            mostrar_mensagem(
                "Dr.Brabo: Por favor, insira um valor numérico válido para a altura.")
    elif etapa == 6:
        enviar_sintomas()


def mostrar_mensagem(mensagem):
    chat_area.config(state=tk.NORMAL)
    for char in mensagem:
        chat_area.insert(tk.END, char)
        chat_area.update_idletasks()
        time.sleep(0.03)  # Simula a digitação lenta
    chat_area.insert(tk.END, "\n")
    chat_area.config(state=tk.DISABLED)


def mostra_sintomas():
    sintomas_frame.pack(pady=10)
    entry_resposta.pack_forget()
    btn_enviar.pack_forget()
    btn_sintomas.pack(pady=10)


def enviar_sintomas():
    sintomas = [s for s, var in sintomas_vars.items() if var.get()]
    if not (2 <= len(sintomas) <= 3):
        messagebox.showerror("Erro", "Selecione entre 2 e 3 sintomas.")
        return
    processar_dados()
    tab_control.select(tab_diagnostico)


# Configuração da interface gráfica
root = tk.Tk()
root.title("Auto-Diagnóstico")

# Criação das abas
tab_control = ttk.Notebook(root)

# Aba de chat
tab_chat = ttk.Frame(tab_control)
tab_control.add(tab_chat, text='Chat')
tab_control.pack(expand=1, fill='both')

# Aba de diagnóstico
tab_diagnostico = ttk.Frame(tab_control)
tab_control.add(tab_diagnostico, text='Diagnóstico')

# Fonte moderna
fonte_padrao = ("Arial", 12)
fonte_chat = ("Arial", 12)

# Área de chat
chat_area = tk.Text(tab_chat, height=30, width=100,
                    state=tk.DISABLED, font=fonte_chat)
chat_area.pack(pady=10)

# Frame para organizar a entrada de texto e o botão de envio lado a lado
entry_frame = tk.Frame(tab_chat)
entry_frame.pack(pady=10)

# Caixa de entrada de respostas
entry_resposta = tk.Entry(entry_frame, width=50, font=fonte_padrao)
entry_resposta.pack(side=tk.LEFT, padx=5)
entry_resposta.bind("<Return>", enviar_resposta)

# Botão de envio de resposta
btn_enviar = tk.Button(entry_frame, text="Enviar",
                       command=enviar_resposta, font=fonte_padrao)
btn_enviar.pack(side=tk.LEFT)

# Área de diagnóstico
text_diagnostico = tk.Text(tab_diagnostico, height=10,
                           width=50, state=tk.DISABLED, font=fonte_padrao)
text_diagnostico.pack(pady=10)

# Inicialização da etapa
etapa = 0

# Área para selecionar sintomas
sintomas_frame = tk.Frame(tab_chat)
sintomas_vars = {
    "dor de cabeça": tk.BooleanVar(),
    "febre alta": tk.BooleanVar(),
    "tosse persistente": tk.BooleanVar()
}

for sintoma, var in sintomas_vars.items():
    tk.Checkbutton(sintomas_frame, text=sintoma, variable=var,
                   font=fonte_padrao).pack(anchor="w")

btn_sintomas = tk.Button(sintomas_frame, text="Enviar sintomas",
                         command=enviar_sintomas, font=fonte_padrao)

# Campos para armazenar as informações coletadas
entry_nome = tk.Entry(tab_chat)
entry_peso = tk.Entry(tab_chat)
entry_altura = tk.Entry(tab_chat)
var_sexo = tk.StringVar()

# Início da interação do chatbot
mostrar_mensagem("Dr.Brabo: Olá! Bem-vindo pra conversa com o Dr.Brabo.")
entry_resposta.pack(pady=10)
btn_enviar.pack(pady=10)

root.mainloop()