import os
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from moviepy.editor import VideoFileClip, CompositeVideoClip

import ctypes
import sys


## testes de commit 


# Crie a janela principal
window = Tk()
window.geometry('800x580')
# Defina o caminho relativo para o arquivo de ícone .ico
icon_path = os.path.join( 'icone.ico')
print('icone', icon_path)
# Renomeie a janela
window.title("Vídeo Rápido.")

# Defina o ícone da janela
window.iconbitmap(icon_path)
# Carregue a imagem de fundo
background_image = PhotoImage(file=os.path.join( 'fundo.png'))
print('imagem ', background_image)
# Crie o rótulo para a imagem de fundo
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Defina a cor de fundo do balão
balloon_color = "#b14646"

# Defina o tamanho fixo dos balões
balloon_width = 25

# Defina a fonte e o tamanho da letra
font_size = 14
font_style = "Arial"

# Crie o título
title_label = Label(window, text="Mesclar vídeos para Tiktok de forma automatica", font=("Jackler West", 16, "bold"), bg=window.cget("highlightbackground"),pady=10)
title_label.pack(pady=10)

# Defina o espaçamento entre os botões
button_padding = 10

# Crie os balões
button1 = Button(window, text="Adicionar Vídeo Principal:",  width=balloon_width, font=(font_style, font_size))
button1.pack(pady=5)

button2 = Button(window, text="Adicionar Vídeo Secundário:",  width=balloon_width, font=(font_style, font_size))
button2.pack(pady=5)

button3 = Button(window, text="Selecionar Pasta para salvar:",  width=balloon_width, font=(font_style, font_size))
button3.pack(pady=5)

button4 = Button(window, text="Mesclar Vídeos", width=balloon_width, font=(font_style, font_size))
button4.pack(pady=5)

from PIL import Image, ImageTk

# Carregue a imagem usando a Pillow
qrcode_image = ImageTk.PhotoImage(Image.open("qrcode.jpg"))

# Crie o rótulo para a imagem
image_label = Label(window, image=qrcode_image)
image_label.pack(pady=15)

# Crie o rótulo para o texto
text_label = Label(window, text="QRCODE PIX DOAÇÃO TIKTOK", font=(font_style, font_size))
text_label.pack()
# Crie o rótulo para o texto
text_label2 = Label(window, text="PIX: 41995059996", font=(font_style, font_size))
text_label2.pack()

# Variáveis para armazenar os caminhos dos arquivos selecionados
video1_path = ""
video2_path = ""
output_folder = ""

# Crie o rótulo para exibir a mensagem
message_label = Label(window, text="", font=(font_style, font_size))
message_label.pack(pady=10)



# Inicia a janela
window.mainloop()