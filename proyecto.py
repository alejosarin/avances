#Importarla libreria tkinter y todas sus funciones
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, StringVar

#-----------------
#Ventana principal
#-----------------

#funciones
#funcion piernas
def piernas():
    ventana=Tk()
    ventana.title("Ejercicios Piernas")
    ventana.geometry("884x482")
    lb_log2o=Label(ventana,image=logo)
    lb_log2o.place(x=0,y=0)

    ventana.mainloop()

#Se declara una variable llamada ventana_principal y que adquiere las caracteristicas tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Proyecto")

#dimensiones de la ventana(ancho,alto)
ventana_principal.geometry("500x350")

#permite deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo


#frame


logo=PhotoImage(file="logo.png")
lb_logo=Label(ventana_principal,image=logo)
lb_logo.place(x=0,y=0)

#etiqueta para el titulo de la app
titulo = Label(lb_logo, text="HEALTH TRAINING")
titulo.config(bg="white", fg="black", font=("Bahnschrift SemiBold", 20))
titulo.place(x=10, y=10)

#texto1
texto1= Label(lb_logo, text="¿Qué parte del cuerpo deseas entrenar?")
texto1.config( fg="black", font=("Bahnschrift SemiBold", 16))
texto1.place(x=10, y=70)

#boton para sumar
bt_sumar = Button(lb_logo, text=("Piernas") , command=piernas)
bt_sumar.place(x=10, y=100, width=100, height=30)






ventana_principal.mainloop()
