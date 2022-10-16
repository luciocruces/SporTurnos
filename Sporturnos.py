from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import Calendar
import DataBase_conn, Buttons_Functions, Creator
import datetime


class ProgramaPrincipal:
    
    def __init__(self):                         # Ventana de fondo
        
        DataBase_conn.createDB()
        self.Fondo = tk.Tk()
        self.w, self.h = self.Fondo.winfo_screenwidth(), self.Fondo.winfo_screenheight()
        self.Fondo.geometry(f"{self.w}x{self.h}")
        self.Fondo.title("SPORTURNOS")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        style.configure("Treeview", 
                        font=("Calibri", 13),
                        rowheight = 35,
                        )
        style.configure('TButton', font = ("Calibri", 13), justify=CENTER)
        style.configure("*TCombobox*Listbox*Font", font = ("Calibri", 30))
        style.configure("TListbox", font = ("Calibri", 30))

        self.ventana_inicio()
        self.Fondo.mainloop()

    def ventana_inicio(self):                   # Frame inicio de sesion
        
        # --------------- Primer Frame ---------------
        self.Frame_LOGIN = ttk.LabelFrame(self.Fondo, text="Inicio de sesión")
        self.Frame_LOGIN.place(relx=0.5, rely=0.3, anchor="center")

        # --------------- Segundo Frame ---------------
        self.Frame_LOGIN_2 = ttk.LabelFrame(self.Fondo, text="Otras opciones")
        self.Frame_LOGIN_2.place(relx=0.5, rely=0.6, anchor="center")

        # --------------- Primer Frame ---------------
        ttk.Label(self.Frame_LOGIN, text = "Bienvenido a \nSporTurno", font=("Calibri", 14, "bold"), justify="center").grid(pady=2)
        ttk.Label(self.Frame_LOGIN, text="").grid()
        ttk.Label(self.Frame_LOGIN, text="Usuario", font=("Calibri", 14)).grid()
        self.user = StringVar()
        self.entryUser = ttk.Entry(self.Frame_LOGIN, font=14, justify="center",textvariable=self.user)
        self.entryUser.focus()
        self.entryUser.grid(padx=50)

        ttk.Label(self.Frame_LOGIN, text="").grid()

        ttk.Label(self.Frame_LOGIN, text="Contraseña", font=("Calibri", 14)).grid()
        self.password = StringVar()
        self.entryPass = ttk.Entry(self.Frame_LOGIN, font=14, justify="center", textvariable=self.password, show="*")
        self.entryPass.grid()

        ttk.Label(self.Frame_LOGIN, text = "", font=("Calibri", 16)).grid(pady=5)

        ls_clubes = DataBase_conn.listaClubes()
        ttk.Label(self.Frame_LOGIN, text = "Elija su club", font=("Calibri", 15)).grid(pady=5)
        self.club = ttk.Combobox(self.Frame_LOGIN,
                                state="readonly",
                                values=ls_clubes,
                                style="TCombobox",
                                )
        self.club.grid()

        self.info_1 = ttk.Label(self.Frame_LOGIN, text="")
        self.info_1.grid()

        self.botonEntrar = ttk.Button(self.Frame_LOGIN, text="\n Entrar \n", command=self.login)
        self.botonEntrar.grid(pady=5)


        # --------------- Segundo Frame ---------------
        self.botonAAA = ttk.Button(self.Frame_LOGIN_2, text="\n Registrarse \n")
        self.botonAAA.grid(column=0, row=0, padx=5, pady=15)
        self.botonAAA.config(state="disabled")

        self.botonBBB = ttk.Button(self.Frame_LOGIN_2, text="\n Crear Club \n", command=self.crearClub)
        self.botonBBB.grid(column=1, row=0, padx=5)

        self.botonCCC = ttk.Button(self.Frame_LOGIN_2, text="\n Salir \n", command=self.salir)
        self.botonCCC.grid(column=2, row=0, padx=5)

    def Main_window(self):                      # Gestión (4 botones)

        self.listaFrames = []

        try:
            self.Frame_LOGIN.destroy()
            self.Frame_LOGIN_2.destroy()
        except:
            pass

        self.listaDatosClub = DataBase_conn.datos_del_club(self.clubSelect)

        self.Frame_MainW = ttk.LabelFrame(self.Fondo, text="SPORTUNOS")
        self.Frame_MainW.place(relx=0.5, rely=0.3, anchor="center")

        ttk.Label(self.Frame_MainW, text=self.clubSelect, font=("Calibri", 16, "bold"), justify="center").grid(column=0, sticky=N, pady=8, columnspan=2)
        ttk.Button(self.Frame_MainW, text="\n\n Canchas \n\n", command=self.ventana_canchas).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.Frame_MainW, text="\n\n Empleados \n\n", command=self.ventana_empleados).grid(row=1, column=1)
        ttk.Button(self.Frame_MainW, text="\n\n Turnos \n\n", command=self.ventana_turnos).grid(row=4, column=0)
        ttk.Button(self.Frame_MainW, text="\n\n Club \n\n", command=self.ventana_club).grid(row=4, column=1, padx=10, pady=10)

        self.Frame_MainW2 = ttk.LabelFrame(self.Fondo, text="Otras opciones")
        self.Frame_MainW2.place(relx=0.5, rely=0.55, anchor="center")
        ttk.Button(self.Frame_MainW2, text="\n Mi usuario \n", command=self.ventana_miUsuario).grid(row=0, column=0, pady=5)
        ttk.Button(self.Frame_MainW2, text="\n Cerrar sesión \n", command=self.cerrar_sesion).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(self.Frame_MainW2, text="\n Estadísticas \n", command=self.ventana_canchas, state="disabled").grid(row=0, column=2, pady=5)

    def ventana_canchas(self):                          # Ventana Canchas
        
        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()

        self.deportesEnClub = Buttons_Functions.listasDepSup(self.clubSelect)
        
        self.Frame_canchasTop = ttk.LabelFrame(self.Fondo, text="Deportes y superficies")
        self.Frame_canchasTop.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.ButtonSport1 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(0))
        self.ButtonSport1.config(state="disabled")
        self.ButtonSport1.grid(pady=10, padx=10, row=0, column=0)
        self.ButtonSport2 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(1))
        self.ButtonSport2.config(state="disabled")
        self.ButtonSport2.grid(pady=10, padx=5, row=0, column=1)
        self.ButtonSport3 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(2))
        self.ButtonSport3.config(state="disabled")
        self.ButtonSport3.grid(pady=10, padx=10, row=0, column=2)
        self.ButtonSport4 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(3))
        self.ButtonSport4.config(state="disabled")
        self.ButtonSport4.grid(pady=10, padx=10, row=1, column=0)
        self.ButtonSport5 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(4))
        self.ButtonSport5.config(state="disabled")
        self.ButtonSport5.grid(pady=10, padx=5, row=1, column=1)
        self.ButtonSport6 = ttk.Button(self.Frame_canchasTop, text="\n  \n", command= lambda:self.seleccion_deporte(5))
        self.ButtonSport6.config(state="disabled")
        self.ButtonSport6.grid(pady=10, padx=10, row=1, column=2)

        ttk.Label(self.Frame_canchasTop, text="Seleccione Superficie", font=("calibri",13, "bold")).grid(row=2, column=0, columnspan=3, pady=5)

        self.ButtonSup1 = ttk.Button(self.Frame_canchasTop, text=" ", command= lambda:self.seleccion_superficie(0))
        self.ButtonSup1.config(state="disabled")
        self.ButtonSup1.grid(pady=10, padx=10, row=3, column=0)
        self.ButtonSup2 = ttk.Button(self.Frame_canchasTop, text=" ", command= lambda:self.seleccion_superficie(1))
        self.ButtonSup2.config(state="disabled")
        self.ButtonSup2.grid(pady=10, padx=5, row=3, column=1)
        self.ButtonSup3 = ttk.Button(self.Frame_canchasTop, text=" ", command= lambda:self.seleccion_superficie(2))
        self.ButtonSup3.config(state="disabled")
        self.ButtonSup3.grid(pady=10, padx=10, row=3, column=2)

        self.ButtonList = [
                self.ButtonSport1,
                self.ButtonSport2,
                self.ButtonSport3,
                self.ButtonSport4,
                self.ButtonSport5,
                self.ButtonSport6,
        ]
        self.SupButtonList = [
            self.ButtonSup1,
            self.ButtonSup2,
            self.ButtonSup3,
        ]

        for n in range(len(self.deportesEnClub)):
            depStr = "\n" + self.deportesEnClub[n][0] + "\n"
            self.ButtonList[n].config(text=depStr)
            self.ButtonList[n]["state"] = "enabled"

        self.Frame_canchasDown = ttk.LabelFrame(self.Fondo, text="Otras opciones")
        self.Frame_canchasDown.place(relx=0.5, rely=0.4, anchor=CENTER)

        ttk.Button(self.Frame_canchasDown, text="\n Agregar \n").grid(pady=10, padx=10, row=0, column=0)
        ttk.Button(self.Frame_canchasDown, text="\n Borrar \n").grid(pady=10, padx=5, row=0, column=1)
        ttk.Button(self.Frame_canchasDown, text="\n Volver \n", command= self.volver_a_gestion).grid(pady=10, padx=10, row=0, column=2)

        self.listaFrames.append(self.Frame_canchasTop)
        self.listaFrames.append(self.Frame_canchasDown)

    def ventana_canchas_2(self, nro):
        
        try:
            self.Frame_canchasCenter.destroy()
        except:
            pass

        self.Frame_canchasDown.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        datosCanchasySup = DataBase_conn.canchasPorSup(self.clubSelect, self.deporteSelect, self.superficieSelect)
        superf = datosCanchasySup[1] + " " + str(nro+1)
        
        self.Frame_canchasCenter = ttk.LabelFrame(self.Fondo, text="Información de la cancha", height=300,width=350)
        self.Frame_canchasCenter.place(relx=0.5, rely=0.54, anchor=CENTER)
        ttk.Label(self.Frame_canchasCenter, text=datosCanchasySup[0], font=("calibri",15, "bold"), justify=CENTER).grid(pady=4, padx=30, column= 0, columnspan=3)
        ttk.Label(self.Frame_canchasCenter, text=superf, font=("calibri",15, "bold"), justify=CENTER).grid(pady=4, padx=30, column= 0, columnspan=3)

        ttk.Label(self.Frame_canchasCenter, text="Precio por hora", font=("calibri",13), justify="center").grid(column= 0, columnspan=3)
        self.precio = IntVar()
        self.EntryPrecio = ttk.Entry(self.Frame_canchasCenter, textvariable=self.precio, font=("calibri",13), justify=CENTER)
        self.EntryPrecio.config(state="disabled")
        self.EntryPrecio.grid(padx=40, pady=5, column= 0, columnspan=3)

        ttk.Label(self.Frame_canchasCenter).grid()

        ttk.Label(self.Frame_canchasCenter, text="Minutos por turno", font=("calibri",13), justify="center").grid(column= 0, columnspan=3)
        fraccion = IntVar()
        Button_30min = ttk.Radiobutton(self.Frame_canchasCenter, text="30 min", variable=fraccion, value=30)
        Button_30min.config(state="disabled")
        Button_30min.grid(column=1, pady=10, row=6)
        Button_60min = ttk.Radiobutton(self.Frame_canchasCenter, text="60 min", variable=fraccion, value=60)
        Button_60min.config(state="disabled")
        Button_60min.grid(column=1, pady=10, row=7)

        ttk.Label(self.Frame_canchasCenter).grid(row=8)

        anterior = ttk.Button(self.Frame_canchasCenter, text="\n <----- \n", command= lambda:self.anterior_cancha(nro))
        anterior.grid(pady=10, padx=10, row=9, column=0)
        if (nro+1) == 1:
            anterior.config(state="disabled")
        
        editarCancha = ttk.Button(self.Frame_canchasCenter, text="\n Editar \n")
        editarCancha.grid(pady=10, padx=5, row=9, column=1)

        siguiente = ttk.Button(self.Frame_canchasCenter, text="\n -----> \n", command= lambda:self.siguiente_cancha(nro))
        siguiente.grid(pady=10, padx=10, row=9, column=2)
        if (nro+1) == datosCanchasySup[2]:
            siguiente.config(state="disabled")

        self.listaFrames.append(self.Frame_canchasCenter)

    def ventana_turnos(self):                           # Ventana Turnos
        
        try:
            self.Frame_TurnosBusq.destroy()
            self.Frame_TURNOS.destroy()
        except:
            pass

        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()
        self.deportesEnClub = Buttons_Functions.listasDepSup(self.clubSelect)

        self.Frame_TurnosBusq = ttk.LabelFrame(self.Fondo, text="BUSCAR TURNOS")
        self.Frame_TurnosBusq.place(relx=0.35, rely=0.45, anchor=CENTER)
        
        self.Frame_TURNOSizq1 = ttk.LabelFrame(self.Frame_TurnosBusq, text="Deportes y superficies")
        self.Frame_TURNOSizq1.grid(row=0, column=0, padx=30, pady=5, columnspan=2)

        self.ButtonSport1 = ttk.Button(self.Frame_TURNOSizq1, text="\n  1 \n", command= lambda:self.seleccion_deporte(0))
        self.ButtonSport1.config(state="disabled")
        self.ButtonSport1.grid(pady=10, padx=10, row=0, column=0)
        self.ButtonSport2 = ttk.Button(self.Frame_TURNOSizq1, text="\n  \n", command= lambda:self.seleccion_deporte(1))
        self.ButtonSport2.config(state="disabled")
        self.ButtonSport2.grid(pady=10, padx=5, row=0, column=1)
        self.ButtonSport3 = ttk.Button(self.Frame_TURNOSizq1, text="\n  \n", command= lambda:self.seleccion_deporte(2))
        self.ButtonSport3.config(state="disabled")
        self.ButtonSport3.grid(pady=10, padx=10, row=0, column=2)
        self.ButtonSport4 = ttk.Button(self.Frame_TURNOSizq1, text="\n  \n", command= lambda:self.seleccion_deporte(3))
        self.ButtonSport4.config(state="disabled")
        self.ButtonSport4.grid(pady=10, padx=10, row=1, column=0)
        self.ButtonSport5 = ttk.Button(self.Frame_TURNOSizq1, text="\n  \n", command= lambda:self.seleccion_deporte(4))
        self.ButtonSport5.config(state="disabled")
        self.ButtonSport5.grid(pady=10, padx=5, row=1, column=1)
        self.ButtonSport6 = ttk.Button(self.Frame_TURNOSizq1, text="\n  \n", command= lambda:self.seleccion_deporte(5))
        self.ButtonSport6.config(state="disabled")
        self.ButtonSport6.grid(pady=10, padx=10, row=1, column=2)

        ttk.Label(self.Frame_TURNOSizq1, text="Seleccione Superficie", font=("calibri",13, "bold")).grid(row=2, column=0, columnspan=3, pady=5)

        self.ButtonSup1 = ttk.Button(self.Frame_TURNOSizq1, text=" ", command= lambda:self.seleccion_superficie(0))
        self.ButtonSup1.config(state="disabled")
        self.ButtonSup1.grid(pady=10, padx=10, row=3, column=0)
        self.ButtonSup2 = ttk.Button(self.Frame_TURNOSizq1, text=" ", command= lambda:self.seleccion_superficie(1))
        self.ButtonSup2.config(state="disabled")
        self.ButtonSup2.grid(pady=10, padx=5, row=3, column=1)
        self.ButtonSup3 = ttk.Button(self.Frame_TURNOSizq1, text=" ", command= lambda:self.seleccion_superficie(2))
        self.ButtonSup3.config(state="disabled")
        self.ButtonSup3.grid(pady=10, padx=10, row=3, column=2)

        self.Frame_TURNOSizq2 = ttk.LabelFrame(self.Frame_TurnosBusq, text="Fecha y hora")
        self.Frame_TURNOSizq2.grid(row=1, column=0, padx=30, pady=10, columnspan=2)

        today = datetime.date.today()
        ttk.Label(self.Frame_TURNOSizq2, text="Seleccione fecha", font=("calibri",15, "bold")).grid(row=0, columnspan=2, pady=5)
        self.calendario = Calendar(self.Frame_TURNOSizq2, statestr="disabled", date_pattern = "dd-mm-y", font=21, showweeknumbers=False, mindate=today)
        self.calendario.grid(row=1, columnspan=2, padx=35, pady=8)

        self.HorasDis_ls = Buttons_Functions.horas(self.listaDatosClub[5], self.listaDatosClub[6])
        cantH = len(self.HorasDis_ls)-1

        ttk.Label(self.Frame_TURNOSizq2, text="Rango Horario", font=("calibri",15, "bold")).grid(row=2, column=0, columnspan=3, pady=5)
        ttk.Label(self.Frame_TURNOSizq2, text="Hora de \nInicio", font=("calibri",12), justify="center").grid(column=0, row=3)
        self.startHour = StringVar()
        tk.Spinbox(self.Frame_TURNOSizq2, width=6, font=("calibri",13), justify="center", values=self.HorasDis_ls, textvariable=self.startHour).grid(row=4, column=0, padx=25, pady=5)
        ttk.Label(self.Frame_TURNOSizq2, text="", font=(), justify="center").grid(column=1, padx=20)
        ttk.Label(self.Frame_TURNOSizq2, text="Hora de\nFinalización", font=("calibri",12), justify="center").grid(column=1, row=3)
        self.finalHour = StringVar()
        tk.Spinbox(self.Frame_TURNOSizq2, width=6, font=("calibri",13), justify="center", values=self.HorasDis_ls, textvariable=self.finalHour).grid(row=4, column=1, padx=25, pady=5)
        self.finalHour.set(self.HorasDis_ls[cantH])
        
        self.infoTurno = ttk.Label(self.Frame_TurnosBusq, text="", font=("calibri",12), justify="center")
        self.infoTurno.grid(column=0, row=2, columnspan=2)

        ttk.Button(self.Frame_TurnosBusq, text="\n Cambiar \n", command=self.ventana_turnos).grid(pady=5, row=3, column=0)

        self.BuscarTurnoButton = ttk.Button(self.Frame_TurnosBusq, text="\n Buscar \n", command= lambda:self.buscarTurno("no"))
        self.BuscarTurnoButton.config(state="disabled")
        self.BuscarTurnoButton.grid(pady=5, padx=5, column=1, row=3)
        
        ttk.Button(self.Frame_TurnosBusq, text="\n Volver \n", command=self.volver_a_gestion).grid(pady=10, row=4, columnspan=2)

        self.ButtonList = [
                self.ButtonSport1,
                self.ButtonSport2,
                self.ButtonSport3,
                self.ButtonSport4,
                self.ButtonSport5,
                self.ButtonSport6,
        ]
        self.SupButtonList = [
            self.ButtonSup1,
            self.ButtonSup2,
            self.ButtonSup3,
        ]
        for n in range(len(self.deportesEnClub)):
            depStr = "\n" + self.deportesEnClub[n][0] + "\n"
            self.ButtonList[n].config(text=depStr)
            self.ButtonList[n]["state"] = "enabled"

        self.listaFrames.append(self.Frame_TurnosBusq)

    def ventana_turnos_2(self, dictTurnos, nro):

        try:
            self.Frame_TURNOS.destroy()
        except:
            pass

        lis = list(dictTurnos.keys())

        self.Frame_TURNOS = ttk.LabelFrame(self.Fondo, text="Disponible")
        self.Frame_TURNOS.place(relx=0.65, rely=0.45, anchor="center")

        ttk.Label(self.Frame_TURNOS, text=lis[nro].replace("_", " "), justify="center", font=("calibri",15, "bold")).grid(row=0, column=0, padx=20, pady=10, columnspan=3)        
        columnas = ('#1', '#2', '#3', '#4')
        self.tree = ttk.Treeview(self.Frame_TURNOS, columns=columnas, show='headings', height=12)

        self.tree.heading('#1', text='Fecha')
        self.tree.heading('#2', text='Horario')
        self.tree.heading('#3', text='Reservado')
        self.tree.heading('#4', text='A nombre de')
        self.tree.column("#1", width=120, anchor=CENTER)
        self.tree.column("#2", width=130, anchor=CENTER)
        self.tree.column("#3", width=100, anchor=CENTER)
        self.tree.column("#4", width=120, anchor=CENTER)

        self.tree.grid(pady=10, padx=25, row=1, column=0, columnspan=3)

        for row in dictTurnos[lis[nro]]:
            self.tree.insert("", tk.END, values=row)

        buttonPrevious = ttk.Button(self.Frame_TURNOS, text="\n<---\n", command= lambda: self.anteriorTurno(dictTurnos, nro))
        buttonPrevious.grid(pady=5, row=2, column=0)
        buttonNext = ttk.Button(self.Frame_TURNOS, text="\n--->\n", command= lambda: self.siguienteTurno(dictTurnos, nro))
        buttonNext.grid(pady=5, row=2, column=2)
        if nro == 0:
            buttonPrevious.config(state="disabled")
        if nro >= len(lis)-1:
            buttonNext.config(state="disabled")

        ttk.Button(self.Frame_TURNOS, text="\n Seleccionar \n", command= lambda:self.selectTurno(lis[nro])).grid(pady=5, row=2, column=1)
        ttk.Button(self.Frame_TURNOS, text="Mostrar\n todos\n los turnos", command=self.todosTurnos).grid(pady=10, row=3, column=1)

        self.listaFrames.append(self.Frame_TURNOS)

    def ventana_club(self):                             # Ventana Club
        
        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()
        ls = DataBase_conn.datos_del_club(self.clubSelect)

        self.Frame_CLUB = ttk.LabelFrame(self.Fondo, text="Datos del Club")
        self.Frame_CLUB.place(relx=0.5, rely=0.4, anchor="center")

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()
        ttk.Label(self.Frame_CLUB, text=ls[0], font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_CLUB, text="Nombre del Club", font=("Calibri", 13)).grid()
        self.entryNew_name = ttk.Entry(self.Frame_CLUB, font=13, justify="center")
        self.entryNew_name.insert(0,ls[0])
        self.entryNew_name.config(state="disabled")
        self.entryNew_name.grid(padx=20)

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_CLUB, text="Encargado", font=("Calibri", 13)).grid()
        self.new_encargado = StringVar()
        self.entryNew_encargado = ttk.Entry(self.Frame_CLUB, font=13, justify="center", textvariable=self.new_encargado)
        self.entryNew_encargado.insert(0,ls[1])
        self.entryNew_encargado.config(state="disabled")
        self.entryNew_encargado.grid()

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_CLUB, text="Telefono", font=("Calibri", 13)).grid()
        self.new_telefono = StringVar()
        self.entryNew_telefono = ttk.Entry(self.Frame_CLUB, font=13, justify="center", textvariable=self.new_telefono)
        self.entryNew_telefono.insert(0,ls[2])
        self.entryNew_telefono.config(state="disabled")
        self.entryNew_telefono.grid()

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_CLUB, text="Lugar", font=("Calibri", 13)).grid()
        self.new_lugar = StringVar()
        self.entryNew_lugar = ttk.Entry(self.Frame_CLUB, font=13, justify="center", textvariable=self.new_lugar)
        self.entryNew_lugar.insert(0,ls[3])
        self.entryNew_lugar.config(state="disabled")
        self.entryNew_lugar.grid()

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_CLUB, text="Hora de apertura", font=("Calibri", 13)).grid()
        self.new_apertura = StringVar()
        self.entryNew_apertura = ttk.Entry(self.Frame_CLUB, font=13, justify="center", textvariable=self.new_apertura)
        self.entryNew_apertura.insert(0,ls[5])
        self.entryNew_apertura.config(state="disabled")
        self.entryNew_apertura.grid()

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_CLUB, text="Hora de cierre", font=("Calibri", 13)).grid()
        self.new_cierre = StringVar()
        self.entryNew_cierre = ttk.Entry(self.Frame_CLUB, font=13, justify="center", textvariable=self.new_cierre)
        self.entryNew_cierre.insert(0,ls[6])
        self.entryNew_cierre.config(state="disabled")
        self.entryNew_cierre.grid()

        ttk.Label(self.Frame_CLUB, font=("Calibri", 11, "bold")).grid()

        self.editClubButton = ttk.Button(self.Frame_CLUB, text="\n Editar \n", command=self.editarClub)
        self.editClubButton.grid()
        ttk.Button(self.Frame_CLUB, text="\n Volver \n", command=self.volver_a_gestion).grid(pady=10)

        self.listaFrames.append(self.Frame_CLUB)

    def ventana_empleados(self):                        # Ventana Empleados
        
        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()

        self.Frame_EMPLEADOS = ttk.LabelFrame(self.Fondo, text="EMPLEADOS")
        self.Frame_EMPLEADOS.place(relx=0.5, rely=0.2, anchor="center")

        ttk.Label(self.Frame_EMPLEADOS, text="Buscar empleado por: ", font=("Calibri", 13, "bold")).grid(pady=4, columnspan=2)
        filtrosEmpleado = ["Usuario", "Correo", "DNI"]
        self.filtro = ttk.Combobox(self.Frame_EMPLEADOS,
                                state="readonly",
                                font=("Calibri", 13),
                                values=filtrosEmpleado)
        self.filtro.current([0])
        self.filtro.grid(columnspan=2)

        self.busquedaEmp = StringVar()
        self.entry_BusqEmpleado = ttk.Entry(self.Frame_EMPLEADOS, font=13, justify="center", textvariable=self.busquedaEmp)
        self.entry_BusqEmpleado.grid(pady=5, padx=40, columnspan=2)
        self.info_2 = ttk.Label(self.Frame_EMPLEADOS, font=("Calibri", 10))
        self.info_2.grid(columnspan=2)

        ttk.Button(self.Frame_EMPLEADOS, text="\n Buscar \n", command=self.buscarEmp).grid(pady=10, row=4)

        self.ventana_empleado_2(0)

        self.listaFrames.append(self.Frame_EMPLEADOS)

    def ventana_empleado_2(self, nro):

        datos = DataBase_conn.datos_todos_empleado(self.clubSelect)

        self.Frame_EMPLEADOS2 = ttk.LabelFrame(self.Fondo, text="EMPLEADO")
        self.Frame_EMPLEADOS2.place(relx=0.5, rely=0.52, anchor="center")

        ttk.Label(self.Frame_EMPLEADOS2, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_EMPLEADOS2, text="Nombre", font=("Calibri", 13)).grid(columnspan=3)
        self.empleado = StringVar()
        self.entry_Empleado = ttk.Entry(self.Frame_EMPLEADOS2, font=13, justify="center", textvariable=self.empleado)
        self.entry_Empleado.insert(0, datos[nro][1])
        self.entry_Empleado.config(state="disabled")
        self.entry_Empleado.grid(padx=40, columnspan=3)

        ttk.Label(self.Frame_EMPLEADOS2, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_EMPLEADOS2, text="Correo", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCorreo = StringVar()
        self.entry_EmpleadoCorreo = ttk.Entry(self.Frame_EMPLEADOS2, font=13, justify="center", textvariable=self.empleadoCorreo)
        self.entry_EmpleadoCorreo.insert(0, datos[nro][3])
        self.entry_EmpleadoCorreo.config(state="disabled")
        self.entry_EmpleadoCorreo.grid(columnspan=3)

        ttk.Label(self.Frame_EMPLEADOS2, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_EMPLEADOS2, text="Telefono", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCel = StringVar()
        self.entry_empleadoCel = ttk.Entry(self.Frame_EMPLEADOS2, font=13, justify="center", textvariable=self.empleadoCel)
        self.entry_empleadoCel.insert(0, datos[nro][5])
        self.entry_empleadoCel.config(state="disabled")
        self.entry_empleadoCel.grid(columnspan=3)

        ttk.Label(self.Frame_EMPLEADOS2, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_EMPLEADOS2, text="Nivel", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCat = IntVar()
        ls_perm = ["cliente", "empleado", "admin"]
        self.entry_empleadoCat = ttk.Combobox(self.Frame_EMPLEADOS2,
                                state="readonly",
                                values=ls_perm,
                                font= 12,
                                justify="center",
                                )
        self.entry_empleadoCat.set(datos[nro][6])
        self.entry_empleadoCat.config(state="disabled")
        self.entry_empleadoCat.grid(columnspan=3, pady=5)

        anterior = ttk.Button(self.Frame_EMPLEADOS2, text="\n <----- \n", command= lambda:self.anterior_empleado(nro))
        anterior.grid(pady=10, padx=10, row=12, column=0)
        if (nro+1) == 1:
            anterior.config(state="disabled")
        
        self.editEmpleadoButton = ttk.Button(self.Frame_EMPLEADOS2, text="\n Editar \n", command=lambda:self.editarEmpleado(datos[nro][0]))
        self.editEmpleadoButton.grid(pady=10, padx=5, row=12, column=1)

        siguiente = ttk.Button(self.Frame_EMPLEADOS2, text="\n -----> \n", command= lambda:self.siguiente_empleado(nro))
        siguiente.grid(pady=10, padx=10, row=12, column=2)        
        if (nro+1) == len(datos):
            siguiente.config(state="disabled")
        
        self.Frame_EMPLEADOS3 = ttk.LabelFrame(self.Fondo, text="Opciones")
        self.Frame_EMPLEADOS3.place(relx=0.5, rely=0.8, anchor="center")

        ttk.Button(self.Frame_EMPLEADOS3, text="Añadir\n Nuevo\n Empleado", command=self.ventana_empleado_3).grid(pady=8, column=0, row=0, padx=10)
        borrarButton = ttk.Button(self.Frame_EMPLEADOS3, text="\n Borrar \n", command=lambda: self.borrar_empleado_check(datos[nro][0]))
        borrarButton.grid(pady=8, column=1, padx=5, row=0)
        if self.UserDatos[0][6] != "admin":
            borrarButton.config(state="disabled")
        ttk.Button(self.Frame_EMPLEADOS3, text="\n Volver \n", command=self.volver_a_gestion).grid(pady=8, column=2, row=0, padx=10)

        self.listaFrames.append(self.Frame_EMPLEADOS2)
        self.listaFrames.append(self.Frame_EMPLEADOS3)

    def ventana_empleado_3(self):

        self.popup_crearEmp = Toplevel()
        self.popup_crearEmp.geometry("400x580")
        self.popup_crearEmp.resizable(False,False)

        self.Frame_creacionEmpleado = ttk.LabelFrame(self.popup_crearEmp, text="CREAR EMPLEADO")
        self.Frame_creacionEmpleado.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_creacionEmpleado, text="Nombre", font=("Calibri", 13)).grid(columnspan=3)
        self.empleado = StringVar()
        self.entry_Empleado = ttk.Entry(self.Frame_creacionEmpleado, font=13, justify="center", textvariable=self.empleado)
        self.entry_Empleado.grid(padx=40, columnspan=3)

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_creacionEmpleado, text="Contraseña", font=("Calibri", 13)).grid(columnspan=3)
        self.password_Empleado = StringVar()
        self.entry_EmpleadoPassword = ttk.Entry(self.Frame_creacionEmpleado, font=13, justify="center", textvariable=self.password_Empleado, show="*")
        self.entry_EmpleadoPassword.grid(padx=40, columnspan=3)

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_creacionEmpleado, text="Correo", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCorreo = StringVar()
        self.entry_EmpleadoCorreo = ttk.Entry(self.Frame_creacionEmpleado, font=13, justify="center", textvariable=self.empleadoCorreo)
        self.entry_EmpleadoCorreo.grid(columnspan=3)

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()

        ttk.Label(self.Frame_creacionEmpleado, text="DNI", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoDNI = StringVar()
        self.entry_EmpleadoDNI = ttk.Entry(self.Frame_creacionEmpleado, font=13, justify="center", textvariable=self.empleadoDNI)
        self.entry_EmpleadoDNI.grid(padx=40, columnspan=3)

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_creacionEmpleado, text="Telefono", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCel = StringVar()
        self.entry_empleadoCel = ttk.Entry(self.Frame_creacionEmpleado, font=13, justify="center", textvariable=self.empleadoCel)
        self.entry_empleadoCel.grid(columnspan=3)

        ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_creacionEmpleado, text="Nivel", font=("Calibri", 13)).grid(columnspan=3)
        self.empleadoCat = IntVar()
        ls_perm = ["cliente", "empleado", "admin"]
        self.entry_empleadoCat = ttk.Combobox(self.Frame_creacionEmpleado,
                                state="readonly",
                                values=ls_perm,
                                font= 12,
                                justify="center",
                                )
        self.entry_empleadoCat.config(state="disabled")
        self.entry_empleadoCat.set(ls_perm[1])
        self.entry_empleadoCat.grid(columnspan=3, pady=5)

        self.infoCreacionEmp = ttk.Label(self.Frame_creacionEmpleado, font=("Calibri", 11, "bold"))
        self.infoCreacionEmp.grid(columnspan=3)

        saveButton = ttk.Button(self.Frame_creacionEmpleado, text="\n Guardar \n", command= self.guardarNuevoEmpleado)
        saveButton.grid(pady=10, padx=5, columnspan=3)

    def borrar_empleado_check(self, id):

        self.popup_delete = Toplevel()
        self.popup_delete.geometry("300x250")
        self.popup_delete.resizable(False,False)
        Frame_delete = ttk.LabelFrame(self.popup_delete, text="Contraseña")
        Frame_delete.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(Frame_delete, text="Ingrese su contraseña\n para confirmar", font=("Calibri", 13), justify=CENTER).grid(pady=5)
        password = StringVar()
        ttk.Entry(Frame_delete, font=("Calibri", 13), textvariable=password).grid(pady=5)

        ttk.Button(Frame_delete, text="Borrar", command=lambda: self.borrar_empleado(id, password.get())).grid(pady=10)

    def ventana_miUsuario(self):

        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()

        self.Frame_miUsuario = ttk.LabelFrame(self.Fondo, text="Mi Usuario")
        self.Frame_miUsuario.place(relx=0.5, rely=0.3, anchor="center")

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_miUsuario, text="Nombre", font=("Calibri", 13)).grid()
        self.miUsuario = StringVar()
        self.entry_miUsuario = ttk.Entry(self.Frame_miUsuario, font=13, justify="center", textvariable=self.miUsuario)
        self.entry_miUsuario.insert(0, self.UserDatos[0][1])
        self.entry_miUsuario.config(state="disabled")
        self.entry_miUsuario.grid(padx=25)

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_miUsuario, text="Correo", font=("Calibri", 13)).grid()
        self.miUsuarioCorreo = StringVar()
        self.entry_miUsuarioCorreo = ttk.Entry(self.Frame_miUsuario, font=13, justify="center", textvariable=self.miUsuarioCorreo)
        self.entry_miUsuarioCorreo.insert(0, self.UserDatos[0][3])
        self.entry_miUsuarioCorreo.config(state="disabled")
        self.entry_miUsuarioCorreo.grid()

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_miUsuario, text="DNI", font=("Calibri", 13)).grid()
        self.entry_miUsuarioDNI = ttk.Entry(self.Frame_miUsuario, font=13, justify="center")
        self.entry_miUsuarioDNI.insert(0, self.UserDatos[0][4])
        self.entry_miUsuarioDNI.config(state="disabled")
        self.entry_miUsuarioDNI.grid()

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_miUsuario, text="Telefono", font=("Calibri", 13)).grid()
        self.miUsuarioCel = StringVar()
        self.entry_miUsuarioCel = ttk.Entry(self.Frame_miUsuario, font=13, justify="center", textvariable=self.miUsuarioCel)
        self.entry_miUsuarioCel.insert(0, self.UserDatos[0][5])
        self.entry_miUsuarioCel.config(state="disabled")
        self.entry_miUsuarioCel.grid()

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        
        ttk.Label(self.Frame_miUsuario, text="Nivel", font=("Calibri", 13)).grid()
        self.miUsuarioCat = IntVar()
        ls_perm = ["cliente", "empleado", "admin"]
        self.entry_miUsuarioCat = ttk.Combobox(self.Frame_miUsuario,
                                state="readonly",
                                values=ls_perm,
                                font= 12,
                                justify="center",
                                )
        self.entry_miUsuarioCat.set(self.UserDatos[0][6])
        self.entry_miUsuarioCat.config(state="disabled")
        self.entry_miUsuarioCat.grid()

        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()
        ttk.Label(self.Frame_miUsuario, font=("Calibri", 11, "bold")).grid()

        self.Frame_miUsuario2 = ttk.LabelFrame(self.Fondo, text="Opciones")
        self.Frame_miUsuario2.place(relx=0.5, rely=0.6, anchor="center")

        ttk.Button(self.Frame_miUsuario2, text="\n Contraseña \n", command=self.ventana_miUsuarioPass).grid(row=0, column=0, padx=8)
        self.editmiUsuarioButton = ttk.Button(self.Frame_miUsuario2, text="\n Editar \n", command=self.editarMiUsuario)
        self.editmiUsuarioButton.grid(pady=8, row=0, column=1)
        ttk.Button(self.Frame_miUsuario2, text="\n Volver \n", command=self.volver_a_gestion).grid(row=0, column=2, padx=8)

        self.listaFrames.append(self.Frame_miUsuario)
        self.listaFrames.append(self.Frame_miUsuario2)

    def ventana_miUsuarioPass(self):

        popup_passw = Toplevel()
        popup_passw.geometry("600x350")
        popup_passw.resizable(False,False)
        self.Frame_Password = ttk.LabelFrame(popup_passw, text="Cambiar contraseña")
        self.Frame_Password.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.Frame_Password, text="Contraseña Actual", font=("Calibri", 13)).grid()
        self.entryOld_Pass = ttk.Entry(self.Frame_Password, font=13, justify="center", show="*")
        self.entryOld_Pass.focus()
        self.entryOld_Pass.grid(padx=12)

        self.info_3 = ttk.Label(self.Frame_Password)
        self.info_3.grid()

        ttk.Label(self.Frame_Password, text="Nueva contraseña", font=("Calibri", 13)).grid()
        self.entryNew_Pass = ttk.Entry(self.Frame_Password, font=13, justify="center", show="*")
        self.entryNew_Pass.config(state="disabled")
        self.entryNew_Pass.grid()

        ttk.Label(self.Frame_Password).grid()

        ttk.Label(self.Frame_Password, text="Nueva contraseña", font=("Calibri", 13)).grid()
        self.entryNew_Pass2 = ttk.Entry(self.Frame_Password, font=13, justify="center", show="*")
        self.entryNew_Pass2.config(state="disabled")
        self.entryNew_Pass2.grid()

        self.info_4 = ttk.Label(self.Frame_Password)
        self.info_4.grid()

        ttk.Button(self.Frame_Password, text="\n Guardar \n", command=self.savePassword).grid(padx=8, pady=10)

        self.entryOld_Pass.bind('<Return>', self.checkOldPass)

    # ------------------------------ BOTONES ------------------------------

    def salir(self):
        self.Fondo.destroy()

    def login(self):
        
        s = Buttons_Functions.checkDatosLogin(self.user.get(), self.password.get(), self.club.get())
        self.clubSelect = self.club.get()
        self.info_1.config(text=s, foreground="red")
        if s == True:
            self.UserDatos = DataBase_conn.usuario_conectado(self.entryUser.get(), self.club.get())
            self.Main_window()
        else:
            self.info_1.config(text=s, foreground="red")

    def registrarse(self):
        pass

    def crearClub(self):

        Creator.CreateNewClub()

    def volver_a_gestion(self):

        for frame in self.listaFrames:
            try:
                frame.destroy()
                self.listaFrames.pop(frame)
            except:
                pass

        self.Main_window()

    def editarClub(self):
        
        self.editClubButton.config(text="\nGuardar\n", command=self.guardarDatosClub)
        botones = [ 
            self.entryNew_encargado, 
            self.entryNew_telefono,
            self.entryNew_lugar,
            self.entryNew_apertura,
            self.entryNew_cierre,
            ]
        for bot in botones:
            bot["state"]= "enabled"

    def guardarDatosClub(self):
        
        tup = (
            self.clubSelect, 
            self.new_encargado.get(), 
            self.new_telefono.get(), 
            self.new_lugar.get(),
            self.listaDatosClub[4],
            self.new_apertura.get(),
            self.new_cierre.get(),
            self.listaDatosClub[7],
            self.listaDatosClub[8],
            )
        mb.showinfo("Info", DataBase_conn.guardar_datos_club(tup))
        
    def buscarEmp(self):
        if Buttons_Functions.checkBuscarEmp(self.entry_BusqEmpleado.get()) == True:
            datos = DataBase_conn.datos_empleado(self.clubSelect, self.filtro.get(), self.entry_BusqEmpleado.get())
            if datos:
                self.info_2.config(text="", foreground="red")
                self.ventana_empleado_2(int(datos[0])-1)
            else:
                self.info_2.config(text="No se encontraron empleados con esos datos", foreground="red")
        else:
            self.info_2.config(text="Ingrese datos para la busqueda", foreground="red")

    def editarEmpleado(self, id):

        botones = [ 
            self.entry_Empleado, 
            self.entry_EmpleadoCorreo,
            self.entry_empleadoCel,
            ]

        if self.UserDatos[0][6] == "admin":
            self.entry_empleadoCat["state"]= "normal"
            self.editEmpleadoButton.config(text="\nGuardar\n", command=lambda:self.guardarEmpleado(id))
            for bot in botones:
                bot["state"]= "enabled"
        else:
            mb.showwarning("Advertencia", "Solo los administradores pueden editar usuarios")
    
    def guardarEmpleado(self, id):
        datosEmp = [
            self.entry_Empleado.get(),
            self.entry_EmpleadoCorreo.get(),
            self.entry_empleadoCel.get(),
            self.entry_empleadoCat.get(),
            id,
            ]

        if DataBase_conn.guardarDatosEmpleado(datosEmp, self.clubSelect):
            self.Frame_EMPLEADOS2.destroy()
            mb.showinfo("Guardado", "Los cambios fueron guardados")

    def guardarNuevoEmpleado(self):
        datosEmp = [
            self.entry_Empleado.get(),
            self.entry_EmpleadoPassword.get(),
            self.entry_EmpleadoCorreo.get(),
            self.entry_EmpleadoDNI.get(),
            self.entry_empleadoCel.get(),
            self.entry_empleadoCat.get(),
            ]

        datosEmp = tuple(datosEmp)

        if Buttons_Functions.checkLenStr(datosEmp):
            if DataBase_conn.guardar_nuevo_empleado(self.clubSelect, datosEmp):
                self.popup_crearEmp.destroy()
                mb.showinfo("Guardado", "Nuevo empleado generado con exito")
            else:
                mb.showerror("Error", "Nombre, DNI o correo ya estan registrados")
        else:
            self.infoCreacionEmp.config(text="Los campos no pueden estar vacios", foreground="red")

    def editarMiUsuario(self):

        self.editmiUsuarioButton.config(text="\nGuardar\n", command=self.guardarMiUsuario)
        botones = [ 
            self.entry_miUsuario, 
            self.entry_miUsuarioCorreo,
            self.entry_miUsuarioCel,
            ]

        if self.UserDatos[0][6] == "admin":
            self.entry_miUsuarioCat["state"]= "normal"
        for bot in botones:
            bot["state"]= "enabled"

    def guardarMiUsuario(self):

        datosMiUser = [ 
            self.entry_miUsuario.get(),
            self.entry_miUsuarioCorreo.get(),
            self.entry_miUsuarioCel.get(),
            self.entry_miUsuarioCat.get(),
            self.UserDatos[0][0],
            ]
        if DataBase_conn.guardarDatosEmpleado(datosMiUser, self.clubSelect):
            mb.showinfo("Guardado", "Los cambios fueron guardados")
        else:
            mb.showinfo("Error", "Algo ocurrió")

    def cerrar_sesion(self):

        self.Frame_MainW.destroy()
        self.Frame_MainW2.destroy()
        self.ventana_inicio()

    def checkOldPass(self, event):

        if self.UserDatos[0][2] == self.entryOld_Pass.get():

            self.entryNew_Pass.config(state="enabled")
            self.entryNew_Pass2.config(state="enabled")
            self.info_3.config(text="")
        
        else:
            self.info_3.config(text="Contraseña incorrecta")

    def savePassword(self):

        resp = Buttons_Functions.checkNewPassword(self.entryNew_Pass.get(), self.entryNew_Pass2.get())
        if resp != 0:
            self.info_4.config(text=resp, foreground="red")
        else:
            self.info_4.config(text="")
            if DataBase_conn.guardarNuevoPassword(self.entryNew_Pass.get(), self.UserDatos[0][0], self.clubSelect):
                mb.showinfo("Info", "La contraseña fue cambiada")
            else:
                mb.showinfo("Info", "Ocurrió un error")

    def seleccion_deporte(self, nro):

        self.superfiesTurnos_ls = DataBase_conn.supPorDeporte(self.clubSelect, self.deportesEnClub[nro][0])
        self.deporteSelect = self.deportesEnClub[nro][0]
        for boton in self.ButtonList:
            if boton != self.ButtonList[nro]:
                boton.config(state="disabled")
        for n in range(len(self.superfiesTurnos_ls)):
            self.SupButtonList[n].config(text=self.superfiesTurnos_ls[n])
            self.SupButtonList[n].config(state="enabled")

    def seleccion_superficie(self, nro):

        self.superficieSelect = self.superfiesTurnos_ls[nro][0]
        condCanchas = False
        for boton in self.SupButtonList:
            if boton != self.SupButtonList[nro]:
                boton.config(state="disabled")
        try:
            self.BuscarTurnoButton.config(state="enabled")
        except:
            condCanchas = True
            pass
        
        if condCanchas:
            try:
                self.ventana_canchas_2(0)
            except:
                pass

    def buscarTurno(self, disp):

        if Buttons_Functions.checkDatosBusqTurno(self.startHour.get(), self.finalHour.get()) == True:
            horasBusq = Buttons_Functions.horas(self.startHour.get(), self.finalHour.get())
            turnosDict = DataBase_conn.busqTurnos(self.clubSelect, horasBusq, self.calendario.get_date(), self.deporteSelect, self.superficieSelect, disp)
            longTurnos = len(turnosDict)
            if longTurnos > 0:
                self.infoTurno.config(text="")
                self.ventana_turnos_2(turnosDict, 0)
            else:
                self.infoTurno.config(text="No se encontraron canchas disponibles", foreground="red")
        else:
            self.infoTurno.config(text="Rango horario invalido", foreground="red")

    def siguienteTurno(self, dictTurnos, nro):
        nro += 1
        self.ventana_turnos_2(dictTurnos, nro)

    def anteriorTurno(self, dictTurnos, nro):
        nro -= 1
        self.ventana_turnos_2(dictTurnos, nro)
    
    def todosTurnos(self):

        self.buscarTurno("__")

    def selectTurno(self, cancha):
        
        dic = self.tree.item(self.tree.focus())
        ls = dic["values"]
        if len(ls) == 0:
            mb.showerror("SPORTURNOS", "Seleccione un turno")
        else:
            self.popUpTurno = Toplevel()
            self.popUpTurno.geometry("400x550")
            self.popUpTurno.resizable(False,False)

            self.Frame_TurnoSelect = ttk.LabelFrame(self.popUpTurno, text="Reserva de Turno")
            self.Frame_TurnoSelect.place(relx=0.5, rely=0.5, anchor="center")

            ttk.Label(self.Frame_TurnoSelect, text="Fecha", font=("Calibri", 13)).grid(columnspan=2)
            date = ttk.Entry(self.Frame_TurnoSelect, font=("Calibri", 13), justify="center")
            date.insert(0,ls[0])
            date.config(state="disabled")
            date.grid(padx=20, columnspan=2)

            ttk.Label(self.Frame_TurnoSelect).grid()

            ttk.Label(self.Frame_TurnoSelect, text="Horario", font=("Calibri", 13)).grid(columnspan=2)
            schedule = ttk.Entry(self.Frame_TurnoSelect, font=("Calibri", 13), justify="center")
            schedule.insert(0,ls[1])
            schedule.config(state="disabled")
            schedule.grid(padx=12, columnspan=2)

            ttk.Label(self.Frame_TurnoSelect).grid()

            ttk.Label(self.Frame_TurnoSelect, text="¿Reservado?", font=("Calibri", 13)).grid(columnspan=2)
            self.varYesNo = IntVar()
            Button_no = ttk.Radiobutton(self.Frame_TurnoSelect, text="NO", variable=self.varYesNo, value=0)
            Button_no.grid(column=0, pady=10, row=7)
            Button_si = ttk.Radiobutton(self.Frame_TurnoSelect, text="SI", variable=self.varYesNo, value=1)
            Button_si.grid(column=1, pady=10, row=7)

            ttk.Label(self.Frame_TurnoSelect, text="A nombre de:", font=("Calibri", 13)).grid(columnspan=2)
            nameEntry = ttk.Entry(self.Frame_TurnoSelect, font=("Calibri", 13), justify="center", textvariable=StringVar())
            nameEntry.insert(0,ls[3])
            nameEntry.grid(padx=12, columnspan=2)

            ttk.Label(self.Frame_TurnoSelect).grid()

            ttk.Button(self.Frame_TurnoSelect, text="\n Guardar \n", command=lambda:self.guardarTurno(ls, nameEntry.get(), cancha)).grid(pady=10, columnspan=2)

            self.info_ResTurno = ttk.Label(self.Frame_TurnoSelect, text="")
            self.info_ResTurno.grid(columnspan=2)

    def guardarTurno(self, lista, nombre, cancha):

        lista[3] = nombre
        if Buttons_Functions.checkNombre(lista[3]):
            if self.varYesNo.get() == 1:
                lista[2] = "si"
                if DataBase_conn.reservarTurno(self.clubSelect, lista, cancha):
                    mb.showinfo("Info", "El turno fue modificado correctamente")
                    self.popUpTurno.destroy()
                else:
                    mb.showerror("Problema al guardar", "Ocurrio un error, intente nuevamente")
            else:
                self.info_ResTurno.config(text="Seleccionar 'Si' para guardar", foreground="red")
        else:
            self.info_ResTurno.config(text="Ingrese un nombre valido", foreground="red")

    def siguiente_cancha(self, nro):
        nro += 1
        self.ventana_canchas_2(nro)

    def anterior_cancha(self, nro):
        nro -= 1
        self.ventana_canchas_2(nro)

    def siguiente_empleado(self, nro):
        nro += 1
        self.ventana_empleado_2(nro)

    def anterior_empleado(self, nro):
        nro -= 1
        self.ventana_empleado_2(nro)

    def borrar_empleado(self, id, password):

        if DataBase_conn.loginDB(self.UserDatos[0][1], password, self.clubSelect):
            if DataBase_conn.borrar_empleado(self.clubSelect, id):
                mb.showinfo("Info", "Usuario eliminado")
                self.popup_delete.destroy()
        else:
            mb.showinfo("Info", "Contra inccorrecta")


ProgramaPrincipal()