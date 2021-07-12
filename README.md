# 
# python car with flask
This was a school project for controlling a car with python using html/flask, and now I'm putting the code online, because of I didn't find a complete build with a raspberry pi with a l298n motor driver. 

How I have devided up the project is in `web-site` where I have put in the raw html file if you wanted to look closer to the file how it is built up. In the `motor movment` I have the code for the motors, one has the controlls in the terminal, the other is combined with the html and flask to controll the car. Lastly in the `finished version` the whole project is combined to just CTRL + C , CTRL + V.

## Things needed to be able to build the car
- Raspberry pi
- L298N motor driver
- 12V DC Motor (2)
- 9 - 12 power supply
- cabels
- bread board
- platform for car
- **Flask** installed to raspberry
- Have **GPIO** installed  

-------

### **Instruction**
So I have put all the code in thier seperate folder that you can copy and paste, or download the files and use the finished folder and just build the car. 

1. Power supply positive pole goes to the +12 on the l298n board.
    1. Power supply negavite pole goes to the GND on the l298n board and on the raspberry pi GND
2. Conect the two DC motors to the motor driver 
3. For the fist set of three cables from raspberry to motor driver 
    - GPIO 23 --> ENA
    - GPIO 25 --> IN1
    - GPIO 24 --> IN2
4. For the other three cables from raspberry to motor driver 
    - GPIO 16 --> IN3
    - GPIO 20 --> IN4
    - GPIO 21 --> ENA
5. Download the or copy files from the finished version folder as the order I have done, to a raspberry pi. 
-------

### Circuit Diagram of the raspberry pi car
![diagram](https://user-images.githubusercontent.com/87243876/125340423-bf39ed00-e352-11eb-948f-4bf9b415d004.png "Circuit Diagram")

-------
#### Definition
- **ENA,ENB :** enables PWM
- **PWM :** Pulse-width modulation changes the electrical signal feed to choose how strong the current is 
- **GND :** Ground
- **IN1,IN2,IN3,IN4 :** For the diffrent side of the motor driver
- **Flask :** a program in python that you have to download to use 
- **BCM :** "Broadcom SOC channel" They signify the Broadcom SOC channel designation.
  - **BOARD :** is the fysikal pins on the raspberry pi
-------
