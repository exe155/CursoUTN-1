import tkinter as tk
from client.gui_app import Frame, menu_sup

def main():
    root = tk.Tk()
    root.title('Calificador de Series')
    # root.resizable(0,0)
    menu_sup(root)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()