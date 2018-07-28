import RPi.GPIO as R
import time
import requests
import json
R.setwarnings(False)
R.setmode(R.BOARD)
R.setup(10,R.OUT)    #Trigger pin of ultrasonic sensor is connected to pin 10
R.setup(3,R.OUT)     #Red LED is connected to pin 3
R.setup(8,R.IN)      #Echo pin of ultrasonic sensor is connected to pin 8
R.setup(5,R.OUT)     #Green LED is connected to pin 5
start_time=0
stop_time=0
while 1:
    R.output(10,1)    #Initiating the Trigger pin for 10 micro seconds
    time.sleep(0.00001)
    R.output(10,0)
    while (R.input(8)==0):
        start_time=time.time()
    while (R.input(8)==1):
        stop_time=time.time()
    timee=(stop_time - start_time) 
    distance=(timee * 17150)
    distance=round(distance,2)
    print ("distance:",distance,'cm')
    time.sleep(1)
    update_distance();
    led_control();


#function for controlling led according to distance

def led_control():
    while (True):
        R.output(3,0)
        R.output(5,0)
        if (distance>100):
            R.output(5,1)       #Turning on Green LED
        else:
            R.output(3,1)       #Turning on Red LED    
