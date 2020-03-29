#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    global message
    message = str(msg.payload)
    print(msg.topic+" "+message)

def on_connect(client, userdata, falg, rc):
    print("Connected with "+str(rc))
    mqttc.publish("/Alert/Message/", "Online")
    mqttc.subscribe("/LEDMatrix")

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.username_pw_set("username", password="15582609")
mqttc.connect("192.168.1.155",1883)
mqttc.loop_start()
message="pad.png"

options = RGBMatrixOptions()
options.rows = 16
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options = options)

#image = Image.open(message)
#image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
#matrix.SetImage(image.convert('RGB'))


try:
    print("Press CTRL-C to stop.")
    while True:
        image = Image.open(message)
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
        matrix.SetImage(image.convert('RGB'))
        print(message)
        time.sleep(60)
except KeyboardInterrupt:
    sys.exit(0)
