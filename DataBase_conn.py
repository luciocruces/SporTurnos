import sqlite3
import os


def createDB():

    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    query = '''
            CREATE TABLE IF NOT EXISTS "registroClubes" (
            "club"	TEXT NOT NULL UNIQUE,
            "encargado"	TEXT NOT NULL,
            "telefono"	INTEGER NOT NULL,
            "lugar"	TEXT NOT NULL,
            "fecha_inicio"	TEXT NOT NULL,
            "apertura"	TEXT,
            "cierre"	TEXT,
            "deportes"	TEXT,
            "superficies"	TEXT,
            PRIMARY KEY("club") 
            )
    '''
    cursor.execute(query)
    conn.commit()
    query = '''
            CREATE TABLE IF NOT EXISTS "usuariosTodos" (
            "nombre"	TEXT NOT NULL,
            "password"	TEXT NOT NULL,
            "level"	INTEGER NOT NULL,
            PRIMARY KEY("nombre")
            )
    '''
    cursor.execute(query)
    conn.commit()
    user = ("admin", "admin", 3)
    query = "INSERT INTO 'usuariosTodos' VALUES (?, ?, ?)"
    try:
        cursor.execute(query, user)
    except:
        pass
    conn.commit()
    conn.close()

def loginDB(user, password, nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    tarea = "SELECT contraseña FROM empleados WHERE usuario = (?) "
    try:
        cursor.execute(tarea, (user,))
        passwInDB = cursor.fetchone()
        conn.close()
        if password == passwInDB[0]:
            return True
        else:
            return False
    except:
        conn.close()
        return False

def listaClubes():
    
    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    query = "SELECT club FROM registroClubes"
    cursor.execute(query)
    ls = cursor.fetchall()
    ls_clubes = [club[0] for club in ls]
    conn.close()
    return ls_clubes

def datos_del_club(nombre_club):

    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    query = "SELECT * FROM registroClubes WHERE club=(?) "
    cursor.execute(query, (nombre_club,))
    lista = cursor.fetchall()
    conn.close()
    ls = [n for n in lista[0]]
    return ls

def guardar_datos_club(tupla):
    
    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    query = "DELETE FROM registroClubes WHERE club = (?)"
    cursor.execute(query, (tupla[0],))
    conn.commit()
    query2 = "INSERT INTO registro VALUES (?,?,?,?,?,?,?,?,?)"
    try:
        cursor.execute(query2, (tupla[0],tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8]))
        conn.commit()
        conn.close()
        return "Datos guardados correctamente"
    except sqlite3.IntegrityError:
        conn.commit()
        conn.close()
        return "Hubo un problema"

def datos_empleado(nombre_club, filtro, dato):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = "SELECT * FROM empleados WHERE " + filtro.lower() + " = (?) "
    cursor.execute(query, (dato.capitalize(),))
    datos = cursor.fetchall()
    conn.close()
    try:
        if len(datos[0]) == 0:
            return False
        else:
            return datos[0]
    except:
        pass

def usuario_conectado(usuario, nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    tarea = "SELECT * FROM empleados WHERE usuario = (?) "
    cursor.execute(tarea, (usuario,))
    datos = cursor.fetchall()
    return datos

def guardarDatosEmpleado(datos, nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    tarea = "UPDATE empleados SET usuario = (?), correo = (?), celular = (?), permisos = (?) WHERE id = (?)"
    cursor.execute(tarea, (datos))
    conn.commit()
    conn.close()
    return True

def guardarNuevoPassword(passw, id,  nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    tarea = "UPDATE empleados SET contraseña = (?) WHERE id = (?)"
    try:
        cursor.execute(tarea, (passw, id))
        conn.commit()
        conn.close()
        return True
    except:
        conn.commit()
        conn.close()
        return False

def depEnClub(nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = "SELECT deporte FROM superficies"
    cursor.execute(query)
    ls = cursor.fetchall()
    conn.close()
    return ls

def supPorDeporte(nombre_club, deporte):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = "SELECT superficie FROM superficies WHERE deporte = (?) "
    cursor.execute(query, (deporte,))
    ls = cursor.fetchall()
    conn.close()
    return ls

def busqTurnos(nombre_club, lsHoras, fecha, deporte, superf, disp):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    fecha = fecha.replace("-", "/")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    lsHoras.pop(len(lsHoras)-1)
    infoTurnos = {}
    for courtNumber in range(canchasPorSup(nombre_club, deporte, superf)[2]):
        ls = []
        cancha = deporte + "_" + superf + "_" + str(courtNumber+1)
        cancha = cancha.replace(" ", "_")
        for hora in lsHoras:
            query = f"SELECT fecha,hora,reserva,quien FROM {cancha} WHERE fecha = '{fecha}' and hora like '{hora}%' and reserva like '{disp}'"
            cursor.execute(query)
            turno = cursor.fetchone()
            if turno:
                ls.append(turno)
        if len(ls) > 0:
            infoTurnos[cancha] = ls
    conn.close()
    return infoTurnos

def canchasPorSup(nombre_club, deporte, superf):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = f"SELECT * FROM superficies WHERE deporte = '{deporte}' and superficie = '{superf}'"
    cursor.execute(query)
    num = cursor.fetchone()
    conn.close()
    return num

def reservarTurno(nombre_club, lista, cancha,):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    try:
        query = f"UPDATE {cancha} SET reserva = '{lista[2]}', quien = '{lista[3]}' WHERE fecha = '{lista[0]}' and hora = '{lista[1]}'"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

def datos_todos_empleado(nombre_club):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = "SELECT * FROM empleados"
    cursor.execute(query)
    datos = cursor.fetchall()
    conn.close()
    try:
        if len(datos[0]) == 0:
            return False
        else:
            return datos
    except:
        pass

def borrar_empleado(nombre_club, id):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = f"DELETE FROM empleados WHERE id = {id}"
    cursor.execute(query)
    conn.commit()
    conn.close()
    return True

def guardar_nuevo_empleado(nombre_club, datos):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{nombre_club}\\{nombre_club}")
    cursor = conn.cursor()
    query = f"INSERT INTO empleados (usuario, contraseña, correo, dni, celular, permisos) VALUES {datos}"
    try:
        cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

print("aaaa")