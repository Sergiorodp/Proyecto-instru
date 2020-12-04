import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
from time import sleep
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()

led = placa.get_pin('d:9:p')
led1 = placa.get_pin('d:10:p')
led2 = placa.get_pin('d:11:p')

A0 = placa.get_pin('a:0:i')
A1 = placa.get_pin('a:1:i')
A2 = placa.get_pin('a:2:i')
A3 = placa.get_pin('a:3:i')


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


time.sleep(0.5)
ventana = Tk()
ventana.state('zoomed') #iniciar la pantalla maximizada
ventana.geometry('1200x800')
ventana.configure(bg = 'white')
ventana.title("Quiz")

marco1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)
draw = Canvas(ventana, width=1900, height=980)
draw.place(x = 80,y = 80)

img = Image.open("D:/Users/Juan/Desktop/Sergio Arboleda/Herramientas/descargau.png")
img = img.resize((150,150))
photoImg=  ImageTk.PhotoImage(img)
b=Label(draw,text="")
b.configure(image=photoImg)
b.place(x = 1060,y = 20)


# Fetch the service account key JSON file contents
cred = credentials.Certificate("D:/Users/Juan/Desktop/Sergio Arboleda/Herramientas/proyecto/key.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-java-python.firebaseio.com/'
})
alerta = Label(draw, text="Alerta",bg='white', font=("Arial Bold", 30), fg="black")
alerta.place(x=300, y = 200)
led_draw=draw.create_oval(15,15,70,70,fill="white")
led1_draw=draw.create_oval(80,15,135,70,fill="white")
led2_draw=draw.create_oval(145,15,200,70,fill="white")


def update_label():
    global lectura1, lectura2,lectura3, lectura4
    global primero,segundo,tercero
    global A0 , A1 ,A2,A3
    global alerta
    global led,led1,led2
    global cled,cled1,cled2,cled3
    lectura1 = A0.read()
    lectura2 = A1.read()
    lectura3 = A2.read()
    lectura4 = A3.read()

    
    get()

    lectura = A0.read()
    lectuta1 = A0.read()

    lectura_indicador.config(text = str(lectura1))
    ref = db.reference("quiz")


    if(primero == "true"):
        draw.itemconfig(led_draw, fill = "red")
        led.write(1)
        cled +=1
    else:
        draw.itemconfig(led_draw, fill = "white")
        led.write(0)
        
    ref.update({
        'eladc':{
            'adc':{
                'nombre':"adc1",
                'valor':lectura1,
                'vecesprendido':cled
            }
        }
    })
    
    lectura = A1.read()
    lectuta2 = A1.read()

    lectura_indicador1.config(text = str(lectura2))
    
    if(segundo == "true"):
        draw.itemconfig(led1_draw, fill = "black")
        led1.write(1)
        cled1 +=1
    else:
        draw.itemconfig(led1_draw, fill = "white")
        led1.write(0)
        
    ref.update({
        'eladc1':{
            'adc':{
                'nombre':"adc2",
                'valor':lectura2,
                'vecesprendido':cled1
            }    
        }
    })
    lectura = A3.read()
    lectura4 = A3.read()

    lectura_indicador3.config(text = str(lectura4))
    
    if(lectura4 >= 0.5):
        draw.itemconfig(led1_draw, fill = "black")
        #led1.write(1)
        #cled4 +=1
    else:
        draw.itemconfig(led1_draw, fill = "white")
        #led1.write(0)
        
    ref.update({
        'eladc3':{
            'adc':{
                'nombre':"adc4",
                'valor':lectura4,
                'vecesprendido':cled3
            }    
        }
    })
    
    lectura = A2.read()
    lectura3 = A2.read()

    lectura_indicador2.config(text = str(lectura3))
    
    if(tercero == "true"):
        draw.itemconfig(led2_draw, fill = "black")
        led2.write(1)
        cled2 +=1
    else:
        draw.itemconfig(led2_draw, fill = "white")
        led2.write(0)
        
    ref.update({
        'eladc2':{
            'adc':{
                'nombre':"adc3",
                'valor':lectura3,
                'vecesprendido':cled2
            }
        }
    })
    ventana.after(500,update_label)

    #if(lectura1 > 0.5 or lectura2 > 0.5 or lectura3 > 0.5):
        #alerta.place(x=600, y = 400);
        #alerta.config(text = "Alerta")
        #ref.update({
            #'elalerta':{
                #'Alerta' : "Alerta"
            #}    
        #})
    #else:
        #alerta.place_forget()
        #ref.update({
            #'elalerta':{
                #'Alerta' : ''
            #}    
        #})
def get():
    global primero,segundo,tercero
    primero=db.reference('LEDS/variables/primero').get()
    segundo=db.reference('LEDS/variables/segundo').get()
    tercero=db.reference('LEDS/variables/tercero').get()
    print(primero)
    print(segundo)
    print(tercero)



lectura_indicador= Label(draw, text=str(lectura1),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
lectura_indicador.place(x=20 + 400, y=90)

adc =Label(draw, text="ADC1",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
adc.place(x =0 + 400,y=130)

lectura_indicador1= Label(draw, text=str(lectura2),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
lectura_indicador1.place(x=120 + 400, y=90)

adc1 =Label(draw, text="ADC2",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
adc1.place(x = 100 + 400,y=130)

lectura_indicador2= Label(draw, text=str(lectura3),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
lectura_indicador2.place(x=220 + 400, y=90)

adc2 =Label(draw, text="ADC3",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
adc2.place(x = 200 + 400,y=130)

lectura_indicador3= Label(draw, text=str(lectura3),bg='cadet blue1', font=("Arial Bold", 15), fg="white")
lectura_indicador3.place(x=220 + 600, y=90)

adc3 =Label(draw, text="ADC3",bg='cadet blue1', font=("Arial Bold", 15), fg="white")
adc3.place(x = 200 + 600,y=130)

            
    
update_label()
ventana.mainloop()
