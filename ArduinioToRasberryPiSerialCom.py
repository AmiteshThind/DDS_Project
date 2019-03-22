import serial
import time

# initalizing USB ports 
Arduinio_0_port = '/dev/ttyUSB0'
Arduinio_1_port = '/dev/ttyUSB1'
Arduinio_2_port = '/dev/ttyUSB2'
Arduinio_3_port = '/dev/ttyUSB3'
Arduinio_4_port = '/dev/ttyUSB4'

time.sleep(2)

# Defining serial object for each arduinio port 
s0 = serial.Serial(Arduinio_0_port,9600) 
s1 = serial.Serial(Arduinio_1_port,9600)  
s2 = serial.Serial(Arduinio_2_port,9600)  
s3 = serial.Serial(Arduinio_3_port,9600)  
s4 = serial.Serial(Arduinio_4_port,9600)  

# clear any previous input for each object 
s0.flushInput()  
s1.flushInput()  
s2.flushInput()  
s3.flushInput()  
s4.flushInput()  


while True:

    if s1.inWaitin()>0:
        tempArduino_0 = s0.readline()
    if s2.inWaitin()>0:
        tempArduino_1 = s1.readline()
    if s2.inWaitin()>0:
        tempArduino_2 = s2.readline()
    if s2.inWaitin()>0:
        tempArduino_3 = s3.readline()
    if s2.inWaitin()>0:
        tempArduino_4 = s4.readline()

    print tempArduino_0
    print tempArduino_1
    print tempArduino_2
    print tempArduino_3
    print tempArduino_4
     


