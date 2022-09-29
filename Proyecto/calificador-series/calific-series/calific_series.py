from logging import root
from os import link
import tkinter as tk
from client.gui_app import Frame 

def main():
    root = tk.Tk()
    root.title('Calificador de Series')
    root.resizable(0,0)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()