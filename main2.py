import tkinter as tk
from tkinter import filedialog
from yt_dlp import YoutubeDL


def Download():
    try:
        caminho_destino = entry_pasta.get()
        url = entry_url.get()

        if not caminho_destino:# Caso não tenha uma pasta
            caminho_destino = "C:\\Users\\Felipe\\Downloads"

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{caminho_destino}/%(title)s.mp3',  # Define o caminho e nome do arquivo
            'metadata_from_title': '%(artist)s - %(title)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        entry_url.delete(0, tk.END)  # Limpa o conteúdo atual da Entry

    except:
        print("Algo deu errado")


def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)  # Limpa o conteúdo atual da Entry
    entry_pasta.insert(0, pasta_selecionada)  # Insere o caminho da pasta selecionada na Entry


janela = tk.Tk()
janela.resizable(False, False)
janela.title('Download Music')

# Frame Pasta
frame1 = tk.Frame()
frame1.grid(row=0, column=0, padx=(10,10), pady=10)

botao = tk.Button(frame1, text="Selecionar Pasta", command=selecionar_pasta)
botao.grid(row=0, column=0)

entry_pasta = tk.Entry(frame1, width=52)
entry_pasta.grid(row=0, column=1, padx=(10,10))

# Frame Url
frame2 = tk.Frame()
frame2.grid(row=1, column=0, padx=(10,10), pady=10)

text_url = tk.Label(frame2, text="Url:")
text_url.grid(row=0, column=0)

entry_url = tk.Entry(frame2, width=65)
entry_url.grid(row=0, column=1, padx=(10,10))

button_init = tk.Button(text="Iniciar Download", bg="green", fg="white", command=Download)
button_init.grid(row=2, column=0, padx=(10,10), pady=10)

janela.mainloop()