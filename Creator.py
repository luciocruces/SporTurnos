from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import Calendar
import datetime
import Creador_BD

class CreateNewClub:

    def  __init__(self):                         # Ventana de fondo

            self.VentFondo = Toplevel()
            self.VentFondo.geometry("350x300")
            self.VentFondo.title("Creador de Clubes en SPORTURNOS")

            self.Frame_1 = ttk.LabelFrame(self.VentFondo, text="Inicio de sesión")
            self.Frame_1.place(relx=0.5, rely=0.5, anchor="center")

            ttk.Label(self.Frame_1, text="Administrador", font=("Calibri", 14)).grid()
            self.usuario = StringVar()
            self.entryUser = ttk.Entry(self.Frame_1, font=14, justify="center",textvariable=self.usuario)
            self.entryUser.focus()
            self.entryUser.grid(padx=50)

            ttk.Label(self.Frame_1, text="").grid()

            ttk.Label(self.Frame_1, text="Contraseña", font=("Calibri", 14)).grid()
            self.password = StringVar()
            self.entryPass = ttk.Entry(self.Frame_1, font=14, justify="center", textvariable=self.password, show="*")
            self.entryPass.grid()

            self.info_1 = ttk.Label(self.Frame_1, text="")
            self.info_1.grid()
            
            self.botonCrear = ttk.Button(self.Frame_1, text="\n Entrar \n", command=self.loginCreador)
            self.botonCrear.grid(pady=8)
            self.VentFondo.mainloop()
            

    def ventana2(self):

            self.superficieDicc = {
            "Futbol": [["Sintetico"], ["Cesped o Tierra"], ["Cemento"]],
            "Padel": [["Sintetico"], ["Cemento"]], 
            "Tenis": [["Polvo Ladrillo"], ["Cemento"], ["Cesped"]], 
            "Voley": [["Cemento"], ["Arena"]],
            "Hockey": [["Sintetico"], ["Cemento"]], 
            "Basquet": [["Cemento"]],
            }

            self.Frame_1.destroy()
            self.VentFondo.geometry("650x600")

            self.Frame_2 = ttk.LabelFrame(self.VentFondo, text="")
            self.Frame_2.grid()
            self.Frame_2.place(relx=0.4, rely=0.5, anchor="e")

            ttk.Label(self.Frame_2, text="Nombre del Club", font=("Calibri", 13)).grid()
            self.club = StringVar()
            self.entryClub = ttk.Entry(self.Frame_2, font=14, justify="center", textvariable=self.club)
            self.entryClub.grid(padx=5)

            ttk.Label(self.Frame_2, text="").grid()

            ttk.Label(self.Frame_2, text="Encargado", font=("Calibri", 13)).grid()
            self.encargado = StringVar()
            self.entryEncargado = ttk.Entry(self.Frame_2, font=14, justify="center", textvariable=self.encargado)
            self.entryEncargado.grid(padx=5)

            ttk.Label(self.Frame_2, text="").grid()

            ttk.Label(self.Frame_2, text="Telefono", font=("Calibri", 13)).grid()
            self.telefono = StringVar()
            self.entryTelefono = ttk.Entry(self.Frame_2, font=14, justify="center", textvariable=self.telefono)
            self.entryTelefono.grid(padx=5)

            ttk.Label(self.Frame_2, text="").grid()

            ttk.Label(self.Frame_2, text="Dirección", font=("Calibri", 13)).grid()
            self.lugar = StringVar()
            self.entryLugar = ttk.Entry(self.Frame_2, font=14, justify="center", textvariable=self.lugar)
            self.entryLugar.grid(padx=5)

            ttk.Label(self.Frame_2, text="").grid()

            self.lista_deportes = ["Futbol   ", "Padel    ", "Tenis     ", "Voley    ", "Hockey ", "Basquet"]
            ttk.Label(self.Frame_2, text="Seleccione los deportes\n disponibles en el club", font=("Calibri", 12)).grid()

            self.deportes_select = []
            for i in range(len(self.lista_deportes)):

                self.deportes_select.append(tk.IntVar(value=0))
                self.cb = tk.Checkbutton(
                                        self.Frame_2, 
                                        text=self.lista_deportes[i], 
                                        font=("Calibri", 11), 
                                        variable=self.deportes_select[i],
                                        command= self.check_deportes,
                                        )
                self.cb.grid(padx=4, column=0, sticky="n")


            # ------------------------ Frame Derecho ------------------------
            
            self.Frame_3 = ttk.LabelFrame(self.VentFondo, text="")
            self.Frame_3.grid()
            self.Frame_3.place(relx=0.5, rely=0.5, anchor="w")

            ttk.Label(self.Frame_3, text="Fecha de Inicio", font=("Calibri", 13)).grid()
            mindate = datetime.date.today()
            self.calendario = Calendar(self.Frame_3, date_pattern = "y-mm-dd", mindate=mindate)
            self.calendario.grid(padx=10)

            ttk.Label(self.Frame_3).grid()

            horarios = ["07:00","08:00", "09:00","10:00","11:00", "12:00"]
            horarios2 = ["19:00","20:00", "21:00","22:00","23:00", "00:00", "01:00", "02:00"]

            ttk.Label(self.Frame_3, text="Horarios", font=("Calibri", 13)).grid()
            ttk.Label(self.Frame_3, text="Apertura", justify="center", font=('Calibri', 12)).grid()
            self.horaApertura = StringVar()
            tk.Spinbox(self.Frame_3, values=horarios, width=6, font=("calibri",12), justify="center", textvariable=self.horaApertura).grid()
            ttk.Label(self.Frame_3).grid()
            ttk.Label(self.Frame_3, text="Cierre", justify="center", font=('Calibri', 12)).grid()
            self.horaCierre = StringVar()
            tk.Spinbox(self.Frame_3, values=horarios2, width=6, font=("calibri",12), justify="center", textvariable=self.horaCierre).grid()
            ttk.Label(self.Frame_3).grid()

            self.botonGuardar = ttk.Button(self.Frame_3, text="\nSiguiente\n", command=self.guardar)
            self.botonGuardar.grid()
            
            self.botonVolver = ttk.Button(self.Frame_3, text="\nCerrar\n", command=self.cerrarCreador)
            self.botonVolver.grid(pady=6)

            self.info_2 = ttk.Label(self.Frame_3, text="")
            self.info_2.grid()


    def ventana3(self):

        try:
            self.Frame_1.destroy()
            self.Frame_2.destroy()
            self.Frame_3.destroy()
        except AttributeError:
            pass

        self.VentFondo.geometry("340x300")
        self.Frame_4 = ttk.LabelFrame(self.VentFondo, text="")
        self.Frame_4.grid(row=0, column=0)
        self.Frame_4.place(relx=0.5, rely=0.1, anchor="n")
        ttk.Label(self.Frame_4, text="Canchas por superficie", font=("Calibri", 13), justify="center").grid()

        self.n = 0
        self.ventana3_render(self.listaDeporteSel[self.n])


    def ventana3_render(self, deporte):

        self.Frame_sup = ttk.LabelFrame(self.VentFondo, text="")
        self.Frame_sup.grid(row=1, column=0)
        self.Frame_sup.place(relx=0.5, rely=0.28, anchor="n")

        titulo = ttk.Label(self.Frame_sup, text=deporte.upper(), font=("Calibri", 13, "bold"), justify="center")
        titulo.place(relx=0.5)
        titulo.grid(columnspan=3)

        superficieLabel = ttk.Label(self.Frame_sup, text=self.superficieDicc[deporte][0][0], font=("Calibri", 12), justify="center")
        superficieLabel.grid(column=1, row=1)
        supNum = IntVar()
        tk.Spinbox(self.Frame_sup, width=6, font=("calibri",12), justify="center", from_=0, to=20, textvariable=supNum).grid(column=1, row=2)
        ttk.Label(self.Frame_sup, text="                  ", font=("calibri",12)).grid(column=1, row=3)

        superficieLabel2 = ttk.Label(self.Frame_sup, text="--------", font=("Calibri", 12), justify="center")
        superficieLabel2.grid(column=0, row=1)
        supNum2 = IntVar()
        sbIzq = tk.Spinbox(self.Frame_sup, width=6, font=("calibri",12), justify="center", from_=0, to=20, state="disabled", textvariable=supNum2)
        sbIzq.grid(column=0, row=2)
        tk.Label(self.Frame_sup, text="                    ", font=("calibri",12)).grid(column=0, row=3)

        try:
            superficieLabel2.config(text=self.superficieDicc[deporte][1][0])
            sbIzq.config(state="normal")
        except IndexError:
            pass
        
        superficieLabel3 = ttk.Label(self.Frame_sup, text="--------", font=("Calibri", 12), justify="center")
        superficieLabel3.grid(column=2, row=1)
        supNum3 = IntVar()
        sbDer = tk.Spinbox(self.Frame_sup, width=6, font=("calibri",12), justify="center", from_=0, to=20, state="disabled", textvariable=supNum3)
        sbDer.grid(column=2, row=2)
        tk.Label(self.Frame_sup, text="                    ", font=("calibri",12)).grid(column=2, row=3)

        try:
            superficieLabel3.config(text=self.superficieDicc[deporte][2][0])
            sbDer.config(state="normal")
        except IndexError:
            pass
        
        botonSiguiente = ttk.Button(self.Frame_sup, text="\n Siguiente \n", command= lambda:self.siguiente2(supNum.get(), supNum2.get(), supNum3.get()))
        botonSiguiente.grid(column=2, row=4)

        botonAnterior = ttk.Button(self.Frame_sup, text="\n Anterior \n", command= lambda:self.anterior(supNum.get(), supNum2.get(), supNum3.get()))
        botonAnterior.grid(column=0, row=4)

    # ----------------------------- FUNCION BOTONES -----------------------------

    def loginCreador(self):

        if Creador_BD.inicio(self.usuario.get(), self.password.get()):
            self.info_1.config(text="")
            self.ventana2()
        else:
            self.info_1.config(text="Usuario o contraseña incorrecta")
        pass
        

    def guardar(self):
        
        datos = [self.entryClub.get(), self.entryEncargado.get(), self.entryLugar.get(), self.entryTelefono.get()]
        self.surfaceTuplas = []

        for dato in datos:
            if len(dato) < 1:
                self.info_2.config(text="Los campos no pueden estar vacíos", foreground="red")
                a = False
                break
            else:
                self.info_2.config(text="")
                a = True

        for n in self.deportes_select:
            if n.get() == 1:
                b = True
                break
            else:
                b = False
                self.info_2.config(text="Seleccione al menos 1 deporte", foreground="red")

        if not a:
            self.info_2.config(text="Los campos no pueden estar vacíos", foreground="red")
        else:
            if b:
                self.siguiente()
        

    def cerrarCreador(self):
        
        self.VentFondo.destroy()


    def siguiente(self):
        
        self.listaDeporteSel = []
        for n in range(len(self.deportes_select)):
            if self.deportes_select[n].get() == 1:
                self.lista_deportes[n] = self.lista_deportes[n].strip()
                self.listaDeporteSel.append(self.lista_deportes[n])
        lista = str(self.listaDeporteSel)
        self.tuplaDatos = [
                    self.entryClub.get(), 
                    self.entryEncargado.get(), 
                    self.entryTelefono.get(),
                    self.entryLugar.get(),
                    self.calendario.get_date(),
                    self.horaApertura.get(),
                    self.horaCierre.get(),
                    lista,
                    ]
        if Creador_BD.chequear(tuple(self.tuplaDatos)):
            self.ventana3()
        else:
            self.info_2.config(text="Ya existe un club con ese nombre", foreground="red")


    def siguiente2(self, s1, s2, s3):

        self.t = (s1, s2, s3)
        self.surfaceTuplas.append(self.t)

        for i in range(len(self.superficieDicc[self.listaDeporteSel[self.n]])):
            self.superficieDicc[self.listaDeporteSel[self.n]][i].append(self.t[i])

        self.n += 1

        try:
            self.Frame_sup.destroy()
            self.ventana3_render(self.listaDeporteSel[self.n])
        except IndexError:
            self.tuplaDatos.append(str(self.surfaceTuplas))
            Creador_BD.guardar_en_registro(self.tuplaDatos, True)
            Creador_BD.guardar_en_club(self.tuplaDatos[0], self.listaDeporteSel, self.superficieDicc, self.tuplaDatos)
            preg = mb.askyesno("Datos guardados", "Desea añadir un nuevo club?")
            if preg:
                self.Frame_4.destroy()
                self.ventana2()
            else:
                self.VentFondo.destroy()


    def anterior(self, arg, arg2, arg3):
        print(arg, arg2, arg3)


    def check_deportes(self):

        pass
