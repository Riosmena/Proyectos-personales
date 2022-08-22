from tkinter import *
from tkinter import ttk
from time import localtime
from pygame import mixer
ventana=Tk()
ventana.title("Alarma")
ventana.geometry("600x500")
ventana.configure(bg="blue")
#Variables---------
imagen1=PhotoImage(file="Reloj.png")
Hora=StringVar()
Minutos=StringVar()
#Funciones---------
def establecer():
    ventana.iconify()
    while True:
        if localtime().tm_hour==int(Hora.get()) and localtime().tm_min==int(Minutos.get()):
            ventana2=Toplevel()
            #Funciones----------
            def cerrar():
                mixer.music.stop()
                ventana.destroy()
            mixer.init()
            mixer.music.load("Niño brasileño cantando la canción de Pou. Sub español.mp3")
            mixer.music.play()
            etiqueta1=Label(ventana2,text="Tiempo finalizado").pack()
            boton1=Button(ventana2,text="Terminar",command=cerrar).pack()
            break
#Entradas----------
entrada1=Entry(ventana,textvariable=Hora).place(x=200,y=500)
entrada2=Entry(ventana,textvariable=Minutos).place(x=900,y=500)
#Etiquetas---------
reloj=Label(ventana,image=imagen1).place(x=610,y=180)
etiqueta1=Label(ventana,text="¡Programa una hora!",font=("Cooper Black",90),bg="blue",fg="white").place(x=50,y=20)
etiqueta2=Label(ventana,text="Hora",font=("Showcard Gothic",40),bg="blue",fg="white").place(x=200,y=400)
etiqueta3=Label(ventana,text="Minutos",font=("Showcard Gothic",40),bg="blue",fg="white").place(x=900,y=400)
#Botones-----------
Boton1=Button(ventana,text="Confirmar",command=establecer).place(x=620,y=600)

ventana.mainloop()
