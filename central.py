import tkinter as tk
from PIL import Image, ImageTk

# Função para criar uma nova página quando um ícone é clicado
def criar_pagina(pagina):
    # Limpar a área de visualização atual
    for widget in frame_visualizacao.winfo_children():
        widget.destroy()

    # Criar conteúdo para a nova página
    if pagina == "Pagina1":
        label = tk.Label(frame_visualizacao, text="Conteúdo da Página 1")
        label.pack()
    elif pagina == "Pagina2":
        label = tk.Label(frame_visualizacao, text="Conteúdo da Página 2")
        label.pack()
    elif pagina == "Pagina3":
        label = tk.Label(frame_visualizacao, text="Conteúdo da Página 3")
        label.pack()

# Criar janela principal
janela = tk.Tk()
janela.title("Sidebar com Ícones")

# Frame para a barra lateral
frame_sidebar = tk.Frame(janela, bg="blue", width=150)  # Aumente o valor do width conforme necessário
frame_sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Frame para a área de visualização do conteúdo
frame_visualizacao = tk.Frame(janela)
frame_visualizacao.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Carregar ícones
icones = []
for i in range(1, 4):
    imagem = Image.open("Iate-vetor.png")  # Substitua pelo caminho das suas imagens
    imagem = imagem.resize((50, 50), Image.ANTIALIAS)
    icone = ImageTk.PhotoImage(imagem)
    icones.append(icone)

# Botões da barra lateral com ícones
botaopagina1 = tk.Button(frame_sidebar, image=icones[0], command=lambda: criar_pagina("Pagina1"))
botaopagina1.pack(pady=10)
botaopagina2 = tk.Button(frame_sidebar, image=icones[1], command=lambda: criar_pagina("Pagina2"))
botaopagina2.pack(pady=10)
botaopagina3 = tk.Button(frame_sidebar, image=icones[2], command=lambda: criar_pagina("Pagina3"))
botaopagina3.pack(pady=10)

# Iniciar com a primeira página
criar_pagina("Pagina1")

# Iniciar a interface gráfica
janela.mainloop()
