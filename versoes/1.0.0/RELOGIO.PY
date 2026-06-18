import tkinter as tk
from time import strftime
import load

load.load()

pergunta = input('Deseja abrir o relógio? [S/N] ')

if pergunta == 's' or 'S':

    # Cria a janela
    root = tk.Tk()
    root.overrideredirect(True)          # Remove bordas
    root.attributes("-topmost", True)    # Fica sempre por cima

    # Cor que será transparente
    TRANSPARENT_COLOR = "black"
    root.config(bg=TRANSPARENT_COLOR)

    # Define transparência (Windows)
    root.wm_attributes("-transparentcolor", TRANSPARENT_COLOR)

    # Posição no canto superior esquerdo
    root.geometry("+120+8")

    # Label do relógio
    clock_label = tk.Label(
        root,
        font=("Consolas", 24, "bold"),
        fg="white",
        bg=TRANSPARENT_COLOR
    )
    clock_label.pack()

    def update_clock():
        current_time = strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        clock_label.after(1000, update_clock)

    update_clock()
    root.mainloop()
elif pergunta == 'n' or 'N':
    load.clear()
