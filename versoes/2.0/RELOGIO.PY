import tkinter as tk
from tkinter import colorchooser, simpledialog
from time import strftime
import subprocess
import sys
import time
from tkinter import messagebox
import config

cfg = config.carregar_config()
relogio_window = None

def iniciar_relogio():
    global relogio_window, cfg

    if relogio_window and relogio_window.winfo_exists():
        relogio_window.destroy()

    relogio_window = tk.Toplevel()
    relogio_window.overrideredirect(True)
    relogio_window.attributes("-topmost", True)

    TRANSPARENT_COLOR = cfg["cor_fundo"]
    relogio_window.config(bg=TRANSPARENT_COLOR)
    relogio_window.wm_attributes("-transparentcolor", TRANSPARENT_COLOR)

    relogio_window.geometry(f"+{cfg['posicao_x']}+{cfg['posicao_y']}")

    clock_label = tk.Label(
        relogio_window,
        font=(cfg["fonte"], cfg["tamanho_fonte"], "bold"),
        fg=cfg["cor_texto"],
        bg=TRANSPARENT_COLOR
    )
    clock_label.pack()

    def update_clock():
        current_time = strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        clock_label.after(1000, update_clock)

    # --- Funções para arrastar a janela ---
    def start_move(event):
        relogio_window.x = event.x
        relogio_window.y = event.y

    def do_move(event):
        dx = event.x - relogio_window.x
        dy = event.y - relogio_window.y
        new_x = relogio_window.winfo_x() + dx
        new_y = relogio_window.winfo_y() + dy
        relogio_window.geometry(f"+{new_x}+{new_y}")

        # Atualiza cfg para salvar nova posição
        cfg["posicao_x"] = new_x
        cfg["posicao_y"] = new_y
        config.salvar_config(cfg)

    # Vincula os eventos ao label
    clock_label.bind("<Button-1>", start_move)
    clock_label.bind("<B1-Motion>", do_move)

    update_clock()

def abrir_configuracoes():
    global cfg


    cor_texto = colorchooser.askcolor(title="Escolha a cor do texto")[1]
    if cor_texto:
        cfg["cor_texto"] = cor_texto

    
    tamanho = simpledialog.askinteger("Tamanho da Fonte", "Digite o tamanho da fonte:", initialvalue=cfg["tamanho_fonte"])
    if tamanho:
        cfg["tamanho_fonte"] = tamanho

    
    pos_x = simpledialog.askinteger("Posição X", "Digite a posição X:", initialvalue=cfg["posicao_x"])
    if pos_x is not None:
        cfg["posicao_x"] = pos_x

   
    pos_y = simpledialog.askinteger("Posição Y", "Digite a posição Y:", initialvalue=cfg["posicao_y"])
    if pos_y is not None:
        cfg["posicao_y"] = pos_y

    
    config.salvar_config(cfg)
    messagebox.showinfo("Configurações", "Configurações salvas! O relógio será reiniciado.")

    iniciar_relogio()

def sair():
    sair = tk.Toplevel()
    sair.title("Sair")
    sair.geometry("350x125")
    sair.resizable(False, False)
    sair.configure(
    bg="#1E1E1E"               
    )


    tk.Label(
    sair, 
    text="Deseja realmente sair?", 
    font=("Arial", 12),
    fg="white",
    bg="#1E1E1E"
    ).pack(pady=10)
    
    tk.Button(
    sair, 
    text="Sim", 
    command=janela.destroy,
    fg="white",
    bg="#1E1E1E",
    activebackground="#1E1E1E",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    bd=2
    ).pack(pady=5)
    
    tk.Button(
    sair, 
    text="Não", 
    command=sair.destroy,
    fg="white",
    bg="#1E1E1E",
    activebackground="#1E1E1E",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    bd=2
    ).pack(pady=5)

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("300x200")
janela.resizable(False, False)
janela.configure(bg="#1E1E1E")

tk.Label(
    janela,
    text="Clock App",
    font=("Arial", 14, "bold"),
    fg="white",      
    bg="#1E1E1E"
).pack(pady=10)

tk.Button(
        janela,
        text="Iniciar Relógio Flutuante",
        width=20,
        command=iniciar_relogio,
        fg="white",
        bg="#1E1E1E",
        activebackground="#1E1E1E",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=2
).pack(pady=5)

tk.Button(
        janela,
        text="Configurações",
        width=20,
        command=abrir_configuracoes,
        fg="white",
        bg="#1E1E1E",
        activebackground="#1E1E1E",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=2
).pack(pady=5)

tk.Button(
        janela,
        text="Sair",
        width=20,
        command=sair,
        fg="white",
        bg="#1E1E1E",
        activebackground="#1E1E1E",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=2
).pack(pady=5)

janela.mainloop()