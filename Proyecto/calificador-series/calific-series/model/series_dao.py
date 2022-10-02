from .conexion_db import conexionDB
from tkinter import menssagebox

def crear_tabla():
    conexion = conexionDB()

    sql = '''
    CREATE TABLE series(
        id_serie INTEGER,
        nombre VARCHAR(100),
        capitulos VARCHAR(3000),
        genero VARCHAR(100),
        puntaje VARCHAR(10),
        PRIMARY KEY(id_serie AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()


def eliminar_tabla():
    conexion = conexionDB()

    sql = 'DROP TABLE series'

    conexion.cursor.execute(sql)
    conexion.cerrar()