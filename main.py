import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os
import pyautogui as py

def Download():
    pasta = entry_pasta.get()
    url = entry_url.get()
    if url:
        if pasta:
            try:
                yt = YouTube(url)
                out = yt.streams.filter(only_audio=True).first().download(output_path=entry_pasta.get())
                new_name = os.path.splitext(out)
                os.rename(out, new_name[0]+'.mp3')
            except:
                py.alert(text='Algo deu errado!') 
        else:
            try:
                yt = YouTube(url)
                out = yt.streams.filter(only_audio=True).first().download(output_path="C:/Users/Felipe/Downloads")
                new_name = os.path.splitext(out)
                os.rename(out, new_name[0]+'.mp3')
            except:
                py.alert(text='Algo deu errado!')

        entry_url.delete(0, tk.END)  # Limpa o conteúdo atual da Entry
    else:
        py.alert(text='Uma Url e necessaria!')

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)  # Limpa o conteúdo atual da Entry
    entry_pasta.insert(0, pasta_selecionada)  # Insere o caminho da pasta selecionada na Entry
  

janela = tk.Tk()
janela.resizable(False, False)
janela.title('Download Music')

#Frase Pasta
frame1 = tk.Frame()
frame1.grid(row=0, column=0, padx=(10,10), pady=10)

botao = tk.Button(frame1, text="Selecionar Pasta", command=selecionar_pasta)
botao.grid(row=0, column=0)

entry_pasta = tk.Entry(frame1, width=52)
entry_pasta.grid(row=0, column=1, padx=(10,10))

#Frame Url
frame2 = tk.Frame()
frame2.grid(row=1, column=0, padx=(10,10), pady=10)

text_url = tk.Label(frame2, text="Url:")
text_url.grid(row=0, column=0)

entry_url = tk.Entry(frame2, width=65)
entry_url.grid(row=0, column=1, padx=(10,10))

button_init = tk.Button(text="Iniciar Download", bg="green", fg="white", command=Download)
button_init.grid(row=2, column=0, padx=(10,10), pady=10)

janela.mainloop()