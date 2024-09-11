import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import time
import threading


# Função para calcular o IMC
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)


# Nome BOT
botNome = "Dr. Ronaldo"

# Lista de doenças com sintomas fixos (obrigatórios) e variáveis (opcionais)
doencas = {
    "Gripe": {
        "fixos": ["Febre"],
        "variaveis": ["Dor de cabeça", "Dor muscular", "Cansaço", "Tosse", "Congestão nasal"]
    },
    "COVID-19": {
        "fixos": ["Febre", "Tosse"],
        "variaveis": ["Cansaço", "Falta de ar", "Perda de paladar", "Dor de cabeça", "Dor muscular", "Congestão nasal"]
    },
    "Dengue": {
        "fixos": ["Febre", "Dor muscular"],
        "variaveis": ["Dor de cabeça", "Sangramento", "Manchas na pele", "Cansaço"]
    },
    "Resfriado": {
        "fixos": ["Congestão nasal"],
        "variaveis": ["Tosse", "Dor de garganta", "Coriza"]
    },
    "Infecção viral": {
        "fixos": ["Febre"],
        "variaveis": ["Cansaço", "Dor de cabeça", "Dor muscular", "Náusea", "Vômito", "Congestão nasal"]
    },
    "Pneumonia": {
        "fixos": ["Febre", "Tosse"],
        "variaveis": ["Dor muscular", "Dificuldade para respirar", "Cansaço"]
    },
    "Bronquite aguda": {
        "fixos": ["Febre", "Tosse"],
        "variaveis": ["Dor muscular", "Dificuldade para respirar", "Cansaço"]
    },
    "Gastroenterite": {
        "fixos": ["Náusea", "Vômito"],
        "variaveis": ["Dores abdominais", "Diarreia"]
    },
    "Intoxicação alimentar": {
        "fixos": ["Náusea", "Vômito"],
        "variaveis": ["Dores abdominais", "Diarreia"]
    },
    "Úlcera gástrica": {
        "fixos": ["Dores abdominais"],
        "variaveis": ["Náusea", "Vômito"]
    },
    "Síndrome do intestino irritável (SII)": {
        "fixos": ["Dores abdominais"],
        "variaveis": ["Diarreia", "Constipação"]
    },
    "Doença inflamatória intestinal (DII)": {
        "fixos": ["Dores abdominais"],
        "variaveis": ["Diarreia", "Constipação", "Perda de peso inexplicada"]
    },
    "Depressão": {
        "fixos": ["Falta de apetite"],
        "variaveis": ["Perda de peso inexplicada", "Cansaço", "Alterações no sono", "Mudanças de humor"]
    },
    "Hipertireoidismo": {
        "fixos": ["Perda de peso inexplicada"],
        "variaveis": ["Falta de apetite", "Cansaço"]
    },
    "Câncer": {
        "fixos": ["Perda de peso inexplicada"],
        "variaveis": ["Falta de apetite", "Cansaço", "Alterações no sono"]
    },
    "Artrite reumatoide": {
        "fixos": ["Dores articulares"],
        "variaveis": ["Sensação de fraqueza", "Alterações na pele", "Cansaço"]
    },
    "Lupus eritematoso sistêmico": {
        "fixos": ["Dores articulares"],
        "variaveis": ["Sensação de fraqueza", "Alterações na pele", "Mudanças de humor"]
    },
    "Fibromialgia": {
        "fixos": ["Dores articulares"],
        "variaveis": ["Sensação de fraqueza", "Cansaço"]
    },
    "Ansiedade ou ataque de pânico": {
        "fixos": ["Palpitações"],
        "variaveis": ["Dificuldade para respirar", "Tontura", "Cansaço"]
    },
    "Asma": {
        "fixos": ["Dificuldade para respirar"],
        "variaveis": ["Sensação de fraqueza", "Palpitações", "Tosse"]
    },
    "Doença pulmonar obstrutiva crônica (DPOC)": {
        "fixos": ["Dificuldade para respirar"],
        "variaveis": ["Sensação de fraqueza", "Palpitações", "Tosse"]
    },
    "Enxaqueca com aura": {
        "fixos": ["Dor ocular"],
        "variaveis": ["Alterações na visão", "Tontura", "Náusea"]
    },
    "Glaucoma": {
        "fixos": ["Dor ocular"],
        "variaveis": ["Alterações na visão"]
    },
    "Uveíte": {
        "fixos": ["Dor ocular"],
        "variaveis": ["Alterações na visão"]
    },
    "Transtorno bipolar": {
        "fixos": ["Mudanças de humor"],
        "variaveis": ["Confusão ou dificuldade de concentração", "Alterações no sono", "Cansaço"]
    },
    "Insônia": {
        "fixos": ["Alterações no sono"],
        "variaveis": ["Confusão ou dificuldade de concentração", "Mudanças de humor", "Cansaço"]
    },
    "Síndrome da fadiga crônica": {
        "fixos": ["Cansaço"],
        "variaveis": ["Confusão ou dificuldade de concentração", "Tontura", "Alterações no sono"]
    },
    "Hipotireoidismo": {
        "fixos": ["Cansaço"],
        "variaveis": ["Falta de apetite", "Perda de peso inexplicada", "Alterações no sono"]
    },
    "Psoríase": {
        "fixos": ["Alterações na pele"],
        "variaveis": ["Dores articulares", "Sensação de fraqueza"]
    },
    "Neuropatia óptica": {
        "fixos": ["Alterações na visão"],
        "variaveis": ["Dor ocular", "Sensação de fraqueza"]
    },
    "Infecção respiratória": {
        "fixos": ["Febre"],
        "variaveis": ["Dor de cabeça", "Dor muscular", "Congestão nasal", "Tosse"]
    },
    "Malária": {
        "fixos": ["Febre"],
        "variaveis": ["Dor de cabeça", "Dor muscular", "Náusea", "Vômito"]
    },
    "Faringite": {
        "fixos": ["Dor de garganta"],
        "variaveis": ["Tosse", "Náusea", "Vômito"]
    },
    "Laringite": {
        "fixos": ["Dor de garganta"],
        "variaveis": ["Tosse", "Náusea"]
    },
}

def calcular_correspondencia(sintomas_informados, doencas):
    resultados = {}

    for doenca, sintomas in doencas.items():
        fixos = sintomas["fixos"]
        variaveis = sintomas["variaveis"]

        # Verificar se todos os sintomas fixos estão presentes
        if all(sintoma in sintomas_informados for sintoma in fixos):
            # Calcular correspondência com sintomas variáveis
            correspondencia_variavel = sum(1 for sintoma in variaveis if sintoma in sintomas_informados)
            total_sintomas = len(fixos) + len(variaveis)
            correspondencia_total = (len(fixos) + correspondencia_variavel) / total_sintomas

            resultados[doenca] = correspondencia_total

    return resultados

def gerar_diagnostico(nome, sexo, peso, altura, sintomas):
    global doenca
    
    resultado = calcular_correspondencia(sintomas, doencas)
    doencas_possiveis = sorted(resultado.items(), key=lambda x: x[1], reverse=True)

    if doencas_possiveis:
        doenca = doencas_possiveis[0][0]  # A doença com maior correspondência
        correspondencia = doencas_possiveis[0][1] * 100  # Percentual de correspondência
    else:
        doenca = "Desconhecida"
        correspondencia = 0

    imc = calcular_imc(peso, altura)
    data_diagnostico = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if imc > 25:
        recomendacao = "Fazer exercícios e dieta.\nPara uma avaliação completa e precisa, é essencial consultar um profissional de saúde."
    else:
        recomendacao = "Ótimo! Mantenha o peso e continue assim!\nPara uma avaliação completa e precisa, é essencial consultar um profissional de saúde."

    return (
        f"Nome: {nome}\n"
        f"Sexo: {sexo}\n"
        f"Peso: {peso} kg\n"
        f"Altura: {altura} m\n"
        f"Sintomas: {', '.join(sintomas)}\n"
        f"Doença diagnosticada: {doenca}\n"
        f"Correspondência com a doença: {correspondencia:.2f}%\n"
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

    if not (3 <= len(sintomas)):
        messagebox.showerror("Erro", "Selecione no mínimo 3 sintomas")
        return

    diagnostico = gerar_diagnostico(nome, sexo, peso, altura, sintomas)

    text_diagnostico.config(state=tk.NORMAL)
    text_diagnostico.delete(1.0, tk.END)
    text_diagnostico.insert(tk.END, diagnostico)
    text_diagnostico.config(state=tk.DISABLED)

    horario_atual = datetime.now().strftime("%H:%M:%S")
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END,
                     f"\n{horario_atual} | {botNome}: {nome}, aqui está o seu diagnóstico:\n------------------------------------------\n\n{diagnostico}\n")
    chat_area.config(state=tk.DISABLED)

def enviar_resposta(event=None):
    global etapa
    resposta = entry_resposta.get()
    entry_resposta.delete(0, tk.END)

    if resposta:
        horario_atual = datetime.now().strftime("%H:%M:%S")
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"{horario_atual} | Você: {resposta}\n")
        chat_area.config(state=tk.DISABLED)

    if etapa == 0:
        mostrar_mensagem(f"Vamos começar com algumas informações básicas, primeiro me diga qual é o seu nome?")
        etapa += 1
    elif etapa == 1:
        nome = resposta
        if str(nome).isalpha():
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome)
            mostrar_mensagem(
                f"Prazer em conhecê-lo, {nome}! Qual é sua idade?")
            etapa += 1
        else:
            mostrar_mensagem(
                f"Por favor, insira um nome válido.")

    elif etapa == 2:
        try:
            idade = int(resposta)
            sexo = resposta.upper()
            mostrar_mensagem(
                f"Beleza!! Qual é o seu sexo? (M/F)")
            etapa += 1
        except ValueError:
            mostrar_mensagem(
                f"Por favor, insira um valor numérico válido para a idade.")
    elif etapa == 3:
        try:
            sexo = resposta
            if sexo == "M" or sexo == "F":
                var_sexo.set(sexo)
        except ValueError:
            mostrar_mensagem(f"Por favor, digite apenas M ou F")
        var_sexo.set(sexo)
        mostrar_mensagem(
            f"Saquei!! Qual é o seu peso em kg?")
        etapa += 1
    elif etapa == 4:
        try:
            peso = float(resposta)
            entry_peso.delete(0, tk.END)
            entry_peso.insert(0, str(peso))
            mostrar_mensagem(f"E qual é a sua altura em metros?")
            etapa += 1
        except ValueError:
            mostrar_mensagem(
                f"Por favor, insira um valor numérico válido para o peso.")
    elif etapa == 5:
        try:
            altura = float(resposta)
            entry_altura.delete(0, tk.END)
            entry_altura.insert(0, str(altura))
            mostrar_mensagem(
                f"Valeu pelas informações. Agora, por favor, clica no que estiver sentindo (mínimo 3 sintomas).")
            mostra_sintomas()
            etapa += 1
        except ValueError:
            mostrar_mensagem(
                f"Por favor, insira um valor numérico válido para a altura.")
    elif etapa == 6:
        enviar_sintomas()


def mostrar_mensagem(mensagem):
    def simular_digitacao():
        chat_area.config(state=tk.NORMAL)
        horario_atual = datetime.now().strftime("%H:%M:%S")  # Captura o horário atual
        chat_area.insert(tk.END, f"{horario_atual} | {botNome}: ")
        for char in mensagem:
            chat_area.insert(tk.END, char)
            chat_area.update_idletasks()
            time.sleep(0.03)  # Simula a digitação lenta
        chat_area.insert(tk.END, "\n")
        chat_area.config(state=tk.DISABLED)

    # Inicia a simulação de digitação em uma thread separada
    threading.Thread(target=simular_digitacao, daemon=True).start()



def mostra_sintomas():
    sintomas_frame.pack(pady=10)
    entry_resposta.pack_forget()
    btn_enviar.pack_forget()
    btn_sintomas.pack(pady=10)


def enviar_sintomas():
    sintomas = [s for s, var in sintomas_vars.items() if var.get()]
    if not (3 <= len(sintomas)):
        messagebox.showerror("Erro", "Selecione entre pelo menos 3 sintomas.")
        return
    processar_dados()
    tab_control.select(tab_diagnostico)


def reiniciarDoenca():
    global doenca
    doenca = "Desconhecida"


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
text_diagnostico = tk.Text(tab_diagnostico, height=15,
                           width=75, state=tk.DISABLED, font=fonte_padrao)
text_diagnostico.pack(pady=10)

# Inicialização da etapa
etapa = 0

# Área para selecionar sintomas
sintomas_frame = tk.Frame(tab_chat)

sintomas_vars = {
    "Febre": tk.BooleanVar(),
    "Tosse": tk.BooleanVar(),
    "Naúsea": tk.BooleanVar(),
    "Vômito": tk.BooleanVar(),
    "Coriza": tk.BooleanVar(),
    "Diarréia": tk.BooleanVar(),
    "Sangramento": tk.BooleanVar(),
    "Cansaço": tk.BooleanVar(),
    "Dores abdominais": tk.BooleanVar(),
    "Dores articulares": tk.BooleanVar(),
    "Dor muscular": tk.BooleanVar(),
    "Dor de cabeça": tk.BooleanVar(),
    "Dor de garganta": tk.BooleanVar(),
    "Congestão Nasal": tk.BooleanVar(),
    "Falta de Ar": tk.BooleanVar(),
    "Constipação": tk.BooleanVar(),
    "Falta de apetite": tk.BooleanVar(),
    "Perda de peso": tk.BooleanVar(),
    "Alterações no sono": tk.BooleanVar(),
    "Sensação de fraqueza": tk.BooleanVar(),
    "Alterações na pele": tk.BooleanVar(),
    "Palpitações/Arritmia Cárdiaca": tk.BooleanVar(),
    "Alterações na visão": tk.BooleanVar(),
    "Tontura": tk.BooleanVar(),
    "Confusão/Falta de concentração": tk.BooleanVar(),
    "Mudança de Humor": tk.BooleanVar(),
}

# Organizar os Checkbuttons em múltiplas colunas com 4 itens por linha
colunas = 6
linha_frame = None
for i, (sintoma, var) in enumerate(sintomas_vars.items()):
    if i % colunas == 0:
        linha_frame = tk.Frame(sintomas_frame)
        linha_frame.pack(anchor="w")
    tk.Checkbutton(linha_frame, text=sintoma, variable=var,
                   font=fonte_padrao).pack(side=tk.LEFT, padx=5, pady=2)

btn_sintomas = tk.Button(sintomas_frame, text="Enviar sintomas",
                         command=enviar_sintomas, font=fonte_padrao)
btn_sintomas.pack(pady=10)

# Campos para armazenar as informações coletadas
entry_nome = tk.Entry(tab_chat)
entry_peso = tk.Entry(tab_chat)
entry_altura = tk.Entry(tab_chat)
var_sexo = tk.StringVar()

# Início da interação do chatbot
mostrar_mensagem(
    f"Olá! Seja bem-vindo à conversa, sou o {botNome}. Antes de começarmos, entenda:\nO software é apenas educacional e não substitui uma avaliação médica.\nPara diagnóstico completo, consulte um profissional de saúde.")
entry_resposta.pack(pady=10)
btn_enviar.pack(pady=10)

root.mainloop()