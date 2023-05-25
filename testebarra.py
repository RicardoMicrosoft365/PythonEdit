import os
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from moviepy.editor import VideoFileClip, CompositeVideoClip

import ctypes
import sys

def run_as_admin():
    # Verifica se o programa está sendo executado como administrador
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        # Se não estiver sendo executado como administrador, solicita a elevação de privilégios
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

# Chama a função para solicitar a elevação de privilégios
run_as_admin()

# Resto do seu código aqui...


# Chama a função para solicitar a elevação de privilégios
run_as_admin()

# Resto do seu código aqui...


def merge_videos(video1_path, video2_path, output_folder):
    
    
    # Carrega o vídeo 1
    video1 = VideoFileClip(video1_path)

    # Carrega o vídeo 2 e remove o áudio
    video2 = VideoFileClip(video2_path).without_audio()

    # Ajusta a duração do vídeo 2 para corresponder à duração do vídeo 1
    video2 = video2.set_duration(video1.duration)

    # Redimensiona o vídeo 2 para ter o mesmo tamanho do vídeo 1
    video2 = video2.resize(video1.size)

    # Redimensiona o vídeo 1 para as dimensões desejadas
    target_width, target_height = video1.size
    video1 = video1.resize((target_width, target_height))

    # Redimensiona o vídeo 2 para as mesmas dimensões do vídeo 1
    video2 = video2.resize((target_width, target_height))

    # Define a posição do vídeo 2 na tela (canto superior esquerdo)
    video2 = video2.set_position((0, 0))

    # Define a posição do vídeo 1 na tela (canto superior direito)
    video1 = video1.set_position((target_width, 0))

    # Combina os vídeos em um único vídeo
    final_video = CompositeVideoClip([video2, video1], size=(target_width * 2, target_height))

    # Obtém o nome do arquivo de vídeo 1
    video1_filename = os.path.basename(video1_path)

    # Define o nome e o caminho do arquivo de vídeo final
    output_path = os.path.join(output_folder, f"{video1_filename}_merged.mp4")

    # Salva o vídeo final
    final_video.write_videofile(output_path, codec="libx264")

    # Obtém a duração total dos vídeos em segundos
    total_duration = max(video1.duration, video2.duration)

def select_video1():
    global video1_path
    video1_path = askopenfilename(title="Selecione o vídeo Principal")
    print("Vídeo 1 selecionado:", video1_path)

def select_video2():
    global video2_path
    video2_path = askopenfilename(title="Selecione o vídeo Secundário")
    print("Vídeo 2 selecionado:", video2_path)

def select_output_folder():
    global output_folder
    output_folder = askdirectory(title="Selecione a pasta de destino do vídeo final")
    print("Pasta de destino selecionada:", output_folder)


def merge_button_clicked():
    if video1_path and video2_path and output_folder:
        merge_videos(video1_path, video2_path, output_folder)
        print("Vídeo final criado com sucesso!")
        # Exibe a mensagem na tela
        message_label.config(text="Vídeo final finalizado.")
        # Aguarda 2 segundos antes de fechar a janela
        window.after(10000, window.destroy)
    else:
        print("Selecione todos os arquivos necessários antes de mesclar os vídeos.")

# Obtenha o diretório do script em execução
script_dir = os.path.dirname(os.path.abspath(__file__))

# Crie a janela principal
window = Tk()
window.geometry('800x400')
# Defina o caminho relativo para o arquivo de ícone .ico
icon_path = os.path.join(script_dir, 'icone.ico')
print('icone', icon_path)
# Renomeie a janela
window.title("Vídeo Rápido.")

# Defina o ícone da janela
window.iconbitmap(icon_path)
# Carregue a imagem de fundo
background_image = PhotoImage(file=os.path.join(script_dir, 'fundo.png'))
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
button1 = Button(window, text="Adicionar Vídeo Principal:", command=select_video1, width=balloon_width, font=(font_style, font_size))
button1.pack()

button2 = Button(window, text="Adicionar Vídeo Secundário:", command=select_video2, width=balloon_width, font=(font_style, font_size))
button2.pack()

button3 = Button(window, text="Selecionar Pasta para salvar:", command=select_output_folder, width=balloon_width, font=(font_style, font_size))
button3.pack()

button4 = Button(window, text="Mesclar Vídeos", command=merge_button_clicked, width=balloon_width, font=(font_style, font_size))
button4.pack()

# Variáveis para armazenar os caminhos dos arquivos selecionados
video1_path = ""
video2_path = ""
output_folder = ""

# Crie o rótulo para exibir a mensagem
message_label = Label(window, text="", font=(font_style, font_size))
message_label.pack(pady=10)


# Inicia a janela
window.mainloop()