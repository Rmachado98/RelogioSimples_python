# Relogio simples em Python!
# Projeto realizado didaticamente com a intenção de praticar os aprendizados na linguagem Python

from tkinter import *
from tkinter.ttk import *
from time import strftime
from turtle import update

root = Tk()
root.title ("Clock")

def update_time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    # vai chamar essa função a cada 1000 milisegundo
    label.after(1000, update_time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="#90EE90")

label.pack(anchor="center")
update_time()

mainloop()
