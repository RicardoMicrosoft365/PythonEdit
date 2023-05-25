import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog, messagebox

def edit_video():
    root = tk.Tk()
    root.withdraw()

    # Solicitar arquivo de vídeo
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    if not file_path:
        return

    # Solicitar pasta de destino
    save_folder = filedialog.askdirectory()
    if not save_folder:
        return

    # Solicitar tempo de início e fim em minutos
    start_time = tk.simpledialog.askstring("Tempo de Início", "Digite o tempo de início (MM:SS):")
    if not start_time:
        return

    end_time = tk.simpledialog.askstring("Tempo de Fim", "Digite o tempo de fim (MM:SS):")
    if not end_time:
        return

    # Converter tempo para segundos
    start_time = convert_time_to_seconds(start_time)
    end_time = convert_time_to_seconds(end_time)

    # Editar o vídeo
    video = mp.VideoFileClip(file_path)
    video = video.subclip(start_time, end_time)

    # Salvar o vídeo editado
    save_path = f"{save_folder}/edited_video.mp4"
    video.write_videofile(save_path)
    messagebox.showinfo("Sucesso", f"Vídeo editado salvo em:\n{save_path}")
    video.close()

def convert_time_to_seconds(time_str):
    try:
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds
    except ValueError:
        return None

def start_editing():
    edit_video()

root = tk.Tk()
root.title("Edição de Vídeo")
root.geometry("300x200")

# Botão Play
play_button = tk.Button(root, text="Play", command=start_editing)
play_button.pack(pady=20)

root.mainloop()
