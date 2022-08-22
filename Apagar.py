import os
from tkinter import * #Importamos la libreria tkinter
from tkinter import messagebox
screen=Tk() #Creamos una ventana
screen.resizable(0,0)
screen.geometry("800x600") #Establecemos el tamaño de la ventana
screen.title("Apagar el equipo") #Colocamos un título para la ventana
screen.configure(bg="green") #Establecemos un color de fondo
#Variables---------------
hora_1=StringVar()
hora_2=StringVar()
minuto_1=StringVar()
minuto_2=StringVar()
segundo_1=StringVar()
segundo_2=StringVar()
tiempo_total=StringVar()
horas, minutos, segundos = '', '', ''
total_strings, cuenta_total = '', ''
valor_total, numero = 0, 1
#Sets--------------------
hora_1.set("0")
hora_2.set("0")
minuto_1.set("0")
minuto_2.set("0")
segundo_1.set("0")
segundo_2.set("0")
tiempo_total.set("00:00:00")
#Funciones---------------
def contar():
    tiempo=valor_total
    segs=tiempo
    mins=tiempo
    hrs=tiempo
    total_horas//3600
    mins-=total_horas*3600
    total_minutos=mins//60
    total_segundos=segs%60
    cuenta_total=str(total_horas)+":"+str(total_minutos)+":"+str(total_segundos)
    valor_total-=numero
    return cuenta_total
def tiempos():
    tiempo_total.set(contar())
    screen.after(1000,tiempo)
def empezar():
    try:
        horas=int(hora_1.get()+hora_2.get())
        minutos=int(minuto_1.get()+minuto_2.get())
        segundos=int(segundo_1.get()+segundo_2.get())
        total_strings=str(horas*60*60+minutos*60+segundos)
        valor_total=int(total_strings)
        os.system("shutdown /s /t "+total_strings)
        hora_1.set("0")
        hora_2.set("0")
        minuto_1.set("0")
        minuto_2.set("0")
        segundo_1.set("0")
        segundo_2.set("0")
        tiempos()
    except ValueError:
        print("ERROR")
        next=messagebox.askretrycancel(message="¿Desea reinciar?",title="ERROR")
        if next==False:
            exit()
boton1=Button(screen,text='Iniciar',font=('Comic Sans MS', 20),command=empezar,bg='#FFF700',fg='black',bd=2.5).pack(side="bottom",fill="x")      
etiqueta1=Label(screen,textvariable=tiempo_total,font=("Comic Sans Ms",80),bg="red",fg="white").pack(ipadx=1,ipady=5,side="top",fill="x")
entrada1=Entry(screen,textvariable=hora_1,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
entrada2=Entry(screen,textvariable=hora_2,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
etiqueta2=Label(screen,text=":",font=("Comic Sans Ms",32),bg="green").pack(ipadx=1,ipady=0.2,side='left',expand=True, fill='x')
entrada3=Entry(screen,textvariable=minuto_1,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
entrada4=Entry(screen,textvariable=minuto_2,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
etiqueta3=Label(screen,text=":",font=("Comic Sans Ms",32),bg="green").pack(ipadx=1,ipady=0.2,side='left',expand=True, fill='x')
entrada5=Entry(screen,textvariable=segundo_1,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
entrada6=Entry(screen,textvariable=segundo_2,font=("Comic Sans Ms",32),bd=2,width=2,bg="white").pack(ipadx=1,ipady=0.2,side="left",expand=True,fill="x")
screen.mainloop()
