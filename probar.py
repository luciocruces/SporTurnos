from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetimerange import *


class esPrueba:
    
    def __init__(self):                         # Ventana de fondo

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
        self.ventana_canchas()
        self.Fondo.mainloop()

    def ventana_canchas(self):
        
        self.Frame_Canchas = ttk.LabelFrame(self.Fondo, text="CANCHAS EN EL CLUB")
        self.Frame_Canchas.place(relx=0.35, rely=0.45, anchor=CENTER)
        
        self.Frame_TURNOSizq1 = ttk.LabelFrame(self.Frame_Canchas, text="Deportes y superficies")
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