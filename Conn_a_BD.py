import sqlite3
import os

def iniciar(dni, password, nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    tarea = "SELECT contraseña FROM usuarios WHERE usuario = (?) "
    try:
        cursor.execute(tarea, (dni,))
        d = cursor.fetchone()
        conn.close()
        if password == d[0]:
            return True
        else:
            return False
    except:
        pass


def nueva_cancha(club):
    conn = sqlite3.connect(club)

    pass


def buscar_turnos(nombre_club, cancha, fecha):

    conn = sqlite3.connect(nombre_club)
    cursor = conn.cursor()
    tarea = "SELECT fecha, hora, reservada FROM " + cancha + " WHERE fecha ='" + fecha + "'"
    try:
        cursor.execute(tarea)
    except sqlite3.OperationalError:
        return False
    resultado = cursor.fetchall()
    conn.close()
    return resultado


def creacion_de_club(club_name):

    conn = sqlite3.connect("Clubes Registrados")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM registro")
    clubes = cursor.fetchall()
    if (club_name,) in clubes:
        n = 1
        conn.close()
        return n
    else:
        cursor.execute("INSERT INTO registro VALUES (NULL,?,?)", (club_name, 1))
        conn.commit()
        conn.close()
        conn = sqlite3.connect(club_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS deportes (deporte TEXT, superficie TEXT, nro_canchas INTEGER)")
        conn.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS datos_usuarios ( dni INTEGER, user TEXT, password TEXT, categoria TEXT, PRIMARY KEY(dni) )")
        conn.commit()
        conn.close()
        nueva_cancha(club_name)
        n = "SI"
        return n


def lista_clubes():
    conn = sqlite3.connect("Clubes Registrados")
    cursor = conn.cursor()
    cursor.execute("SELECT club FROM registro ORDER BY club")
    lista = cursor.fetchall()
    clubes = []
    for club in lista:
        clubes.append(club[0])
    conn.close()
    return clubes

    
def deportes_en_club(nombre_club, deporte):                 # Guardar deportes disponibles en el club

    deporte = deporte.lower()
    conn = sqlite3.connect(nombre_club)
    cursor = conn.cursor()
    cursor.execute("SELECT deporte FROM deportes")
    lista = cursor.fetchall()
    if (deporte,) in lista:
        pass
    else:
        cursor.execute("INSERT INTO deportes VALUES (?, NULL, 1)", (deporte,))
        conn.commit()

    conn.close()


def lista_de_deportes(nombre_club):
    
    conn = sqlite3.connect(nombre_club)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deportes")
    lista = cursor.fetchall()
    #   [('padel', None, 1), ('tenis', None, 1)]  <<<< Devuelve algo así
    conn.close()
    return lista