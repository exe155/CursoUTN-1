import tkinter as tk
from model.series_dao import crear_tabla, eliminar_tabla

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 500, height= 350)
        self.root = root
        self.pack()
        self.config(bg = 'black')
