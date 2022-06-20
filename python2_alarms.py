#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: python2_alarms.py
    :synopsis: Module for notifying the anomalies of the system as alarms.
    
.. moduleauthor:: Marina Perez (mperez234@ehu.eus)
"""

import paho.mqtt.client as mqtt 
import tkinter as tk
import requests  

root = tk.Tk()  #set Tk instance
my_canvas = tk.Canvas(root, width=200, height=200)  #create 200x200 Canvas widget
my_canvas.pack()

my_oval = my_canvas.create_oval(50, 50, 145, 145)  #create a circle on the Canvas
label_var = tk.StringVar()  #set the string variable for Label widget

my_canvas.itemconfig(my_oval, fill="green1")  #fill the circle with green colour
label_var.set("OK")
print("****OK")
root.update()

#This function sends the message to Telegram through the Bot API
def send_msg(text):                
   token = "5598958352:AAG6cvehpRxmE3rp2X2gz9myT-eumeb3lng"
   chat_id = "-744711793"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)
   print(results.json())

#This function is called when a message is received from one of the subscribed topics
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))

    if msg == "Burbuja":
        my_canvas.itemconfig(my_oval, fill="yellow")  #fill the circle with yellow colour
        label_var.set("ALARMA: BURBUJA")
        print("****Burbuja") 
        send_msg("Cuidado, BURBUJA")  #to telegram
        root.update()
        
    elif msg == "Voltaje_sat_aviso":
        my_canvas.itemconfig(my_oval, fill="yellow")  #fill the circle with yellow colour
        label_var.set("ALARMA: CUIDADO, VOLTAJE SATURADO," + "\n"+
                      "PUEDE QUE HAYA ENTRADO AIRE")
        print("****Voltaje saturado") 
        send_msg("Cuidado, VOLTAJE SATURADO, puede que haya entrado aire")  #to telegram
        root.update()

    elif msg == "Voltaje_sat_peligro":
        my_canvas.itemconfig(my_oval, fill="orange")  #fill the circle with orange colour
        label_var.set("ALARMA: PELIGRO, VOLTAJE SATURADO," +  "\n" +
                      "SE SUBIRÁ AUTOMÁTICAMENTE"+"\n" + "LA FRECUENCIA")
        print("****Voltaje saturado") 
        send_msg("Peligro, VOLTAJE SATURADO, se subirá automáticamente la frecuencia")  #to telegram
        root.update()

    elif msg == "Voltaje_sat_fin":
        my_canvas.itemconfig(my_oval, fill="red")  #fill the circle with red colour
        label_var.set("ALARMA: FIN, VOLTAJE SATURADO," + "\n" + 
                      "ES NECESARIO CAMBIAR LA BOMBA")
        print("****Voltaje saturado") 
        send_msg("Fin, VOLTAJE SATURADO, es necesario cambiar la bomba")  #to telegram
        root.update()
        
    elif msg == "Caudal_ins":
        my_canvas.itemconfig(my_oval, fill="red")  #fill the circle with red colour
        label_var.set("ALARMA: FIN, CAUDAL INSUFICIENTE")
        print("****Caudal insuficiente") 
        send_msg("Fin, CAUDAL INSUFICIENTE")  #to telegram
        root.update() 

broker_address='192.168.0.18'  #IP address of the broker

my_label = tk.Label(root, textvariable=label_var)  #set the Label widget
my_label.pack()

print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

#subscribe to topics
print("Subscribing to topic","alarma/voltaje_saturación")
client.subscribe("marina/alarma/voltaje_saturación")
print("Subscribing to topic","alarma/burbuja")
client.subscribe("marina/alarma/burbuja")
print("Subscribing to topic","alarma/caudal_insuficiente")
client.subscribe("marina/alarma/caudal_insuficiente")

#start the MQTT Mosquito process loop
client.loop_start() 

root.mainloop()