import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

import pandas as pd
import datetime

cont,cont2=0,0
placa = Arduino ('COM4')
it = util.Iterator(placa)
it.start()

led1 = placa.get_pin('d:3:p')
led2 = placa.get_pin('d:5:p')
led3 = placa.get_pin('d:6:p')
led4 = placa.get_pin('d:9:p')
led5 = placa.get_pin('d:10:p')
led6 = placa.get_pin('d:11:p')

A0 = placa.get_pin('a:0:i')
A1 = placa.get_pin('a:1:i')
A2 = placa.get_pin('a:2:i')
A3 = placa.get_pin('a:3:i')

time.sleep(0.5)

# ventana = Tk()
# ventana.state('zoomed') #iniciar la pantalla maximizada
# ventana.geometry('1200x800')
# ventana.configure(bg = 'white')
# ventana.title("Quiz")

# marco1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
# marco1.place(x = 0,y = 0)
# draw = Canvas(ventana, width=1900, height=980)
# draw.place(x = 80,y = 80)

# Fetch the service account key JSON file contents
cred = credentials.Certificate('D:/SERGIO/Sergio(noCloud)/a empezar de nuevo 2.0/Universidad/Instrumentación/Final Proyect/react/final_proyect/Arduino/key/main_key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-java-python.firebaseio.com/'
})

def inicialize():
    ref = db.reference("Leds")
    ref.update({
        'N1':{
            'state':False,
        },
        'N2':{
            'state':False,
        }
    })

lectura1 = 0
lectura2 = 0
lectura3 = 0

primero=""
segundo=""
tercero=""

cled=0
cled1=0
cled2=0
cled3=0


### Nuevas variables para calcular instru

velocidad_main = 0
distancia_main = 0

inicialize()

def update_label():
    global lectura1, lectura2,lectura3, lectura4
    global primero,segundo,tercero
    global A0 , A1 ,A2,A3
    global cled,cled1,cled2,cled3
    global medidas_velocidad, distancia_main
    lectura1 = A0.read()
    lectura2 = A1.read()
    lectura3 = A2.read()
    lectura4 = A3.read()

    
    # get()

    lectura = A0.read()
    lectura1 = A0.read()

    # lectura_indicador.config(text = str(lectura1))
    ref = db.reference("quiz")
    
    # lectura = A1.read()
    # lectura2 = A1.read()

    # lectura_indicador1.config(text = str(lectura2))
    
    distancia_main += velocidad_main/3600
    ref.update({
        'eladc2':{
            'nombre':"Distancia (Km)",
            'valor': round(distancia_main,2),
            'prom':cled1
        }
    })

    ref.update({
        'eladc1':{
            'nombre':"Velocidad (Km/h)",
            'valor':round(medir_velocidad(),2),
            'prom': round((velocidad_main + medir_velocidad())/2,2)
        }
    })
    # lectura = A3.read()
    # lectura4 = A3.read()

    # lectura_indicador3.config(text = str(lectura4))
    
        
    # ref.update({
    #     'eladc3':{
    #         'adc':{
    #             'nombre':"adc4",
    #             'valor':lectura4,
    #             'vecesprendido':cled3
    #         }    
    #     }
    # })
    
    # lectura = A2.read()
    # lectura3 = A2.read()

    # lectura_indicador2.config(text = str(lectura3))
    
        
    # ref.update({
    #     'eladc2':{
    #         'adc':{
    #             'nombre':"adc3",
    #             'valor':lectura3,
    #             'vecesprendido':cled2
    #         }
    #     }
    # })
    update_label()

def medir_velocidad():
    global velocidad_main
    count = 0
    c = 0
    time = 0
    if(A0.read() > 0.2):
        while(c < 1):
            measure = A0.read()
            print(measure)
            if measure < 0.2:
                c = 1
            count += 1
            if count > 19200 or (count < 2 and c == 1):
                count = 0
                break
        time = count * 1/9600
        try:
            Velocidad = (((2/(time))/100)/1000)*3600
        except:
            Velocidad = 0
        velocidad_main = Velocidad
        print(velocidad_main)
        return velocidad_main
    else: 
        return velocidad_main


# def medir_distancia():


def get():
    global primero,segundo,tercero
    primero=db.reference('quiz/Velocidad/primero').get()
    segundo=db.reference('LEDS/variables/segundo').get()
    tercero=db.reference('LEDS/variables/tercero').get()
    print(primero)
    print(segundo)
    print(tercero)

# lectura_indicador= Label(draw, text=str(lectura1),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# lectura_indicador.place(x=20 + 400, y=90)

# adc =Label(draw, text="ADC1",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# adc.place(x =0 + 400,y=130)

# lectura_indicador1= Label(draw, text=str(lectura2),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# lectura_indicador1.place(x=120 + 400, y=90)

# adc1 =Label(draw, text="ADC2",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# adc1.place(x = 100 + 400,y=130)

# lectura_indicador2= Label(draw, text=str(lectura3),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# lectura_indicador2.place(x=220 + 400, y=90)

# adc2 =Label(draw, text="ADC3",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# adc2.place(x = 200 + 400,y=130)

# lectura_indicador3= Label(draw, text=str(lectura3),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# lectura_indicador3.place(x=220 + 600, y=90)

# adc3 =Label(draw, text="ADC3",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
# adc3.place(x = 200 + 600,y=130)


update_label()
# ventana.mainloop()