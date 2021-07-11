#import the sutff needed
from time import sleep
import time
import RPi.GPIO as GPIO
import RPi.GPIO as IO

#variable for the script
  #pins for the left motor "GPIO 24, GPIO 23, GPIO 25", temp1 is another variable
in1 = 24
in2 = 23
en = 25
temp1=1

  #pins for the right motor "GPIO 17, GPIO 27, GPIO 22", temp1 is another variable
in3 = 17
in4 = 27
en2 = 22
temp2=1

#distant stuff
GPIO.setmode(IO.BCM)
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input

#setup for left motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
#setup for right motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
#something
p=GPIO.PWM(en,150)
p2=GPIO.PWM(en2,150)
p.start(25)
p2.start(25)
#prints out 
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("Base comands: r = run, b = backward, f = forward, s = stop, e = exit\nSpeed: l = low, m = medium, h = high\nStering: sr = stering right, sl = stering left,tl = stering left 0.5 seconds, tr = stering right 0.5 seconds")
print("\n")

#starts the while loop
while(1):
    from time import sleep
    import time
    import RPi.GPIO as GPIO
    import RPi.GPIO as IO

    #variable for input from user
    x=raw_input()

#base input comands
    if x=='r':
        print("run")
        if(temp1==1,temp2==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward both")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward both")
         x='z'
    #drives the motors backward
    elif x=='b':
        print("backward both")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'
    #drives the motors forward
    elif x =='f':
        print("forward both")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    #stops the motors
    elif x =='s':
        print("Stop both")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    #ending the script
    elif x=='e':
        GPIO.cleanup()
        break

#Speed input comands
    elif x=='l':
    #sets the speed to low speed
        print("low")
        p.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x='z'
    
    elif x=='m':
    #sets the speed to medium speed
        print("medium")
        p.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'
    #sets the speed to high speed
    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        x='z'

#stering left input comands
    elif x =='sl':
        print("Stering left")
    #right motor forward
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    #left motor backward
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
#input for stering right
    elif x =='sr':
        print("Stering right")
    #right motor backward
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
    #left motor forward
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

#stering in x seconds input comands
  #left
    elif x =='tl':
        print("Stering left")
    #right motor forward
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    #left motor backward
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
  #waits x amount of seconds
        time.sleep(1)
    #stops the motors
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("Done\nPlease input a next valid comand\n")
  #right
    elif x =='tr':
        print("Stering right")
    #right motor backward
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
    #left motor forward
        GPIO.output(in1,GPIO.HIGH) 
        GPIO.output(in2,GPIO.LOW)
  #waits x amount of seconds
        time.sleep(1)
    #stops the motors
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("Done\nPlease input a next valid comand\n")



        if(IO.input(14)==True): #object is far away
        IO.output(2,True) #Red led ON
        IO.output(3,False) # Green led OFF

    if(IO.input(14)==False): #object is 
        print("Turn")
        IO.output(3,True) #Green led ON
        IO.output(2,False) # Red led OFF
        print("backward both")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        time.sleep(0.5)
        print("Stering right")
    #right motor backward
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
    #left motor forward
        GPIO.output(in1,GPIO.HIGH) 
        GPIO.output(in2,GPIO.LOW)
  #waits x amount of seconds
        time.sleep(1)
    #stops the motors
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        print("Done\nPlease input a next valid comand\n")


#print if the inuput comand is not correct
    else:
        print("<<<  wrong data  >>>")
        print("Please enter the defined data to continue.....")
        print("Defined data:\nBase comands: r = run, b = backward, f = forward, s = stop, e = exit\nSpeed: l = low, m = medium, h = high\nStering: sr = stering right, sl = stering left,tl = stering left 0.5 seconds, tr = stering right 0.5 seconds\n")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
for the webbsite to get the Circuit Diagram of the motors
https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/


"""
