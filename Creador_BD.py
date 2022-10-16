import sqlite3
import os
import datetime

def inicio(usuario, password):

    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    tarea = "SELECT password FROM usuariosTodos WHERE nombre = (?) "
    try:
        cursor.execute(tarea, (usuario,))
        d = cursor.fetchone()
        conn.close()
        if password == d[0]:
            return True
        else:
            return False
    except:
        pass


def guardar_en_registro(tupla, conf):

    resp = True

    try:
        os.makedirs(f'clubes/{tupla[0]}')
    except:
        pass

    if conf:
        conn = sqlite3.connect("Database")
        cursor = conn.cursor()
        try:
            tarea = "INSERT INTO registroClubes VALUES (?,?,?,?,?,?,?,?,?)"
            cursor.execute(tarea, (tupla))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            conn.commit()
            conn.close()
            resp = False
            
    nombre = tupla[0]
    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn2 = sqlite3.connect(f"{ruta}\\clubes\\{nombre}\\{nombre}")
    cursor2 = conn2.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS empleados (
	"id"	INTEGER NOT NULL UNIQUE,
	"usuario"	TEXT UNIQUE,
	"contraseña"	TEXT,
	"correo"	TEXT UNIQUE,
	"dni"	TEXT UNIQUE,
	"celular"	TEXT,
	"permisos"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
    )'''
    cursor2.execute(query)
    

    tarea = "INSERT INTO empleados VALUES (?,?,?,?,?,?,?)"
    tup = (1, 'admin','admin','ad@min','666','15','admin')
    cursor2.execute(tarea, (tup))
    conn2.commit()

    cursor2.execute('CREATE TABLE IF NOT EXISTS superficies (deporte TEXT,superficie TEXT,nro INTEGER)')
    conn2.commit()
    conn2.close()
    return resp


def guardar_en_club(club, listaDeportes, supDicc, tuplaDatos):

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{club}\\{club}")
    cursor = conn.cursor()

    for i in range(len(listaDeportes)):
        for superficie in supDicc[listaDeportes[i]]:
            cursor.execute('INSERT INTO superficies VALUES (?,?,?)', (listaDeportes[i], superficie[0], superficie[1]))
            for n in range(superficie[1]):
                m = str(n+1)
                sup = superficie[0].replace(" ", "_")
                tabla = f"{listaDeportes[i]}_{sup}_{m}"
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabla} (fecha TEXT, hora TEXT, reserva TEXT, quien TEXT, precio FLOAT, ult_modif TEXT)')
                conn.commit()
                horarios_canchas(club, tuplaDatos, tabla)
    conn.close()


def chequear(tupla):

    conn = sqlite3.connect("Database")
    cursor = conn.cursor()
    tarea = "SELECT club FROM registroClubes"
    cursor.execute(tarea)
    clubes = cursor.fetchall()
    conn.commit()
    conn.close()
    if tupla[0] in clubes:
        return False
    else:
        return True
    

def horarios_canchas(club, tuplaDatos, tabla):

    fecha = tuplaDatos[4]
    fecha = fecha.split("-")
    hora_apertura = tuplaDatos[5]
    hora_apertura = hora_apertura.split(":")
    hora_cierre = tuplaDatos[6]
    hora_cierre = hora_cierre.split(":")
    supLista = fecha + hora_apertura + hora_cierre
    lista_enteros = []
    for n in supLista:
        n = int(n)
        lista_enteros.append(n)

    dif = lista_enteros[5] - lista_enteros[3]
    if lista_enteros[5] < lista_enteros[3]:
        dif = 25 + lista_enteros[5] - lista_enteros[3]

    ruta = os.getcwd()
    ruta = ruta.replace("\\","\\\\")
    conn = sqlite3.connect(f"{ruta}\\clubes\\{club}\\{club}")
    cursor = conn.cursor()

    fecha_inicio = datetime.datetime(year=lista_enteros[0], month=lista_enteros[1], day=(lista_enteros[2]), hour=lista_enteros[3])
    for dia in range(30): # Cambiar rango a 180 dias despues

        for i in range(dif):

            hora_inicio = fecha_inicio + datetime.timedelta(hours= i)
            hora_final = hora_inicio + datetime.timedelta(hours= 1)
            turno = hora_inicio.strftime("%H:%M") + " a " + hora_final.strftime("%H:%M")
            busqueda = cursor.execute("SELECT fecha, hora FROM " + tabla )
            b = busqueda.fetchall()
            a = (str(fecha_inicio), turno)
            if a in b:
                pass
            else:
                cursor.execute("INSERT INTO " + tabla + " VALUES(?, ?, ?, ?, ?, ?)", (hora_inicio.strftime("%d/%m/%Y"), turno, "no", "", 0, ""))
                conn.commit()
    
        fecha_inicio = fecha_inicio + datetime.timedelta(days = 1)
    conn.close()
