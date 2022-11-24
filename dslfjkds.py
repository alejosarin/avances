#Importarla libreria tkinter y todas sus funciones
from tkinter import *

#-----------------
#Ventana principal
#-----------------

#funciones
#funcion piernas

#Se declara una variable llamada ventana_principal y que adquiere las caracteristicas tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Proyecto")

#dimensiones de la ventana(ancho,alto)
ventana_principal.geometry("1500x1050")

#permite deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

logo=PhotoImage(file="logo.png")
lb_logo=Label(ventana_principal,image=logo)
lb_logo.place(x=0,y=0)











ventana_principal.mainloop()