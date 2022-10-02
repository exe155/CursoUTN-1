from distutils.command.clean import clean
from os import stat
import tkinter as tk
from model.series_dao import crear_tabla, eliminar_tabla

def menu_sup(root):
    menu_sup = tk.Menu(root)
    root.config(menu=menu_sup, width= 700, height= 700)

    menu_archivo = tk.Menu(menu_sup, tearoff= 0)
    menu_sup.add_cascade(label = 'Archivo', menu = menu_archivo)
    
    menu_archivo.add_command(label = 'Crear lista')
    menu_archivo.add_command(label = 'Modificar lista')
    menu_archivo.add_command(label = 'Eliminar lista')
    menu_archivo.add_command(label = 'Salir', command= root.destroy)

    menu_edicion = tk.Menu(menu_sup, tearoff= 0)
    menu_sup.add_cascade(label = 'Edición', menu = menu_edicion)

    menu_edicion.add_command(label = 'Deshacer')
    menu_edicion.add_command(label = 'Cortar')
    menu_edicion.add_command(label = 'Copiar')
    menu_edicion.add_command(label = 'Pegar')
    menu_edicion.add_command(label = 'Eliminar')
    menu_edicion.add_command(label = 'Buscar')
    menu_edicion.add_command(label = 'Siguiente')
    menu_edicion.add_command(label = 'Anterior')

    menu_ver = tk.Menu(menu_sup, tearoff= 0)
    menu_sup.add_cascade(label = 'Ver', menu = menu_ver)

    menu_ver.add_command(label = 'Acercar')
    menu_ver.add_command(label = 'Alejar')
    menu_ver.add_command(label = 'Restaurar zoom predeterminado')

    menu_ayuda = tk.Menu(menu_sup, tearoff= 0)
    menu_sup.add_cascade(label = 'Ayuda', menu = menu_ayuda)

    menu_ayuda.add_command(label = 'Ver la ayuda')
    menu_ayuda.add_command(label = 'Enviar comentarios')
    menu_ayuda.add_command(label = 'Acerca de Calificador de Series')

class Frame(tk.Frame):
    def __init__(self, root = None):    
        super().__init__(root, width= 500, height= 350)
        self.root = root
        self.pack()
        self.config(bg = 'black')

        self.camps_series()

    def camps_series(self):

        # Nombres de campos de ingreso.

            self.label_nombre = tk.Label(self, text = 'Nombre: ')
            self.label_nombre.config(font = ('Times', 15, 'bold'))
            self.label_nombre.grid(row = 0, column= 0, padx= 10, pady= 10)

            self.label_capitulos = tk.Label(self, text = 'Capitulos: ')
            self.label_capitulos.config(font = ('Times', 15, 'bold'))
            self.label_capitulos.grid(row = 1, column= 0, padx= 10, pady= 10)

            self.label_genero = tk.Label(self, text = 'Genero: ')
            self.label_genero.config(font = ('Times', 15, 'bold'))
            self.label_genero.grid(row = 2, column= 0, padx= 10, pady= 10)
            
            self.label_puntaje = tk.Label(self, text = 'Puntaje: ')
            self.label_puntaje.config(font = ('Times', 15, 'bold'))
            self.label_puntaje.grid(row = 3, column= 0, padx= 10, pady= 10)

        # Entradas de campos.    

            self.mio_nombre = tk.StringVar()
            self.entry_nombre = tk.Entry(self, textvariable = self.mio_nombre)
            self.entry_nombre.config(width= 50, font = ('Arial', 12))
            self.entry_nombre.grid(row= 0, column= 1, padx= 10, pady= 10, columnspan= 2)

            self.mio_capitulos = tk.StringVar()
            self.entry_capitulos = tk.Entry(self, textvariable = self.mio_capitulos)
            self.entry_capitulos.config(width= 50, font = ('Arial', 12))
            self.entry_capitulos.grid(row= 1, column= 1, padx= 10, pady= 10, columnspan= 2)

            self.mio_genero = tk.StringVar()
            self.entry_genero = tk.Entry(self, textvariable = self.mio_genero)
            self.entry_genero.config(width= 50, font = ('Arial', 12))
            self.entry_genero.grid(row= 2, column= 1, padx= 10, pady= 10, columnspan= 2)

            self.mio_puntaje = tk.StringVar()
            self.entry_puntaje = tk.Entry(self, textvariable = self.mio_puntaje)
            self.entry_puntaje.config(width= 50, font = ('Arial', 12))
            self.entry_puntaje.grid(row= 3, column= 1, padx= 10, pady= 10, columnspan= 2)

        # Botones.

            self.boton_nuevo = tk.Button(self, text="Nuevo", command= self.camps_activate)
            self.boton_nuevo.config(width= 20, font=('Times', 15, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor= 'hand2', activebackground= '#35BD6F')
            self.boton_nuevo.grid(row= 4, column= 0)

            self.boton_guardar = tk.Button(self, text="Guardar")
            self.boton_guardar.config(width= 20, font=('Times', 15, 'bold'), fg = '#DAD5D6', bg = '#1658A2', cursor= 'hand2', activebackground= '#3586DF')
            self.boton_guardar.grid(row= 4, column= 1)

            self.boton_cancelar = tk.Button(self, text="Cancelar", command= self.camps_deactivate, )
            self.boton_cancelar.config(width= 20, font=('Times', 15, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor= 'hand2', activebackground= '#E15370')
            self.boton_cancelar.grid(row= 4, column= 2)

    def camps_activate(self):

            self.boton_nuevo()
            self.entry_nombre.config(state= 'normal')
            self.entry_genero.config(state= 'normal')
            self.entry_capitulos.config(state= 'normal')
            self.entry_puntaje.config(state= 'normal')   

            self.boton_guardar.config(state= 'normal')
            self.boton_cancelar.config(state= 'normal')

    def camps_deactivate(self):

            self.entry_nombre.config(state= 'disable')
            self.entry_genero.config(state= 'disable')
            self.entry_capitulos.config(state= 'disable')
            self.entry_puntaje.config(state= 'disable')   

            self.boton_guardar.config(state= 'disable')
            self.boton_cancelar.config(state= 'disable')



