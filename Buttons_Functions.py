import DataBase_conn
import datetime 
from datetimerange import *


def checkDatosLogin(user, password, nombre_club):
    if len(user) == 0 or len(password) == 0:
        st = "Los campos no pueden estar vacíos"
        return st
    if len(nombre_club) == 0:
        st = "Seleccione un club"
        return st
    check = DataBase_conn.loginDB(user, password, nombre_club)
    if check:
        return True
    else:
        st = "Usuario o contraseña incorrecta"
        return st

def checkBuscarEmp(BusquedaStr):
    if len(BusquedaStr) == 0:
        return False
    else:
        return True

def checkNewPassword(pass1, pass2):

    if len(pass1) < 4:
        return "La contraseña debe contener al menos 4 caracteres"
    else:
        if pass1 != pass2:
            return "Las contraseñas no coinciden"
        else:
            return 0

def listasDepSup(nombre_club):

    deportes = DataBase_conn.depEnClub(nombre_club)
    deportes = list(dict.fromkeys(deportes))
    return deportes

def horas(horaI, horaF):

    time_range = DateTimeRange(horaI, horaF)
    time_range.start_time_format = "%H:%M:%S"
    horasDis = []
    for h in time_range.range(datetime.timedelta(hours=1)):
        horasDis.append(h.strftime("%H:%M"))
    return horasDis

def checkDatosBusqTurno(inicio, final):

    inicio = int(inicio.split(":")[0])
    final = int(final.split(":")[0])
    
    if inicio < final:
        return True
    else:
        return False

def checkNombre(nombre):

    if len(nombre) < 3:
        return False
    else:
        return True

def checkLenStr(lista):

    resp = True
    for str in lista:
        if len(str) == 0:
            resp = False

    return resp