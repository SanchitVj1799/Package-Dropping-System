import RPi.GPIO as g
import requests

g.setmode(g.BOARD)

p_pwm = 32         #pulse width modulation pin. May Not be PWM pin. Change to GPIO18/ Pin 32
p_dir = 40         #direction signal pin 
g.setmode(g.BOARD)
g.setup(p_dir, g.OUT)
g.setup(p_pwm, g.OUT)
g.setup(36, g.OUT)        #for latch
g.output(p_dir, g.LOW)
g.output(36, g.LOW)
pwm = g.PWM(p_pwm, 1000)     # PWM function with duty cycle = 1000
pwm.start(0)           # To start signal from 0

while(1):
    x=input()
    print(x)
    if(x=='q'):
        g.output(p_dir, g.LOW)
        pwm.ChangeDutyCycle(0)
        break
    if(x=='1'):
        print('Latch out')
        g.output(36,g.HIGH)
    if(x=='2'):
        print('Latch in')
        g.output(36,g.LOW)
    elif(x=='3'):               # Max. down speed motor loop
        print('Motor down')
        g.output(p_dir, g.HIGH)
        pwm.ChangeDutyCycle(0)    # max speed = HIGH - 0
        print('motor down speed')
    
    elif(x=='4'):             #Max. up speed motor loop
        print('Motor up')
        g.output(p_dir, g.LOW)
        pwm.ChangeDutyCycle(100)   #  max speed = 100 - LOW
        print('motor up speed')
    
    elif(x=='5'):           # Stopping motor loop
        g.output(p_dir, g.LOW)
        pwm.ChangeDutyCycle(0)
        print('Stopping Motor')
        print('Motor stop')
    
    elif(x=='6'):               # Loop controlling down speed
        speed=int(input())
        g.output(p_dir, g.HIGH)
        pwm.ChangeDutyCycle(100 - speed)
        print('motor down speed')
    
    elif(x=='7'):             # Loop controlling up speed
        speed=int(input())
        g.output(p_dir, g.LOW)
        pwm.ChangeDutyCycle(speed)
        print('Direction1')
        print('motor up speed')
    
    elif(x=='8'):
        print('Parcel close')
        requests.get('http://192.168.4.1/4/on') # To bring the motor shaft out #
        
    elif(x=='9'):
        print('Parcel close_2')
        requests.get('http://192.168.4.1/4/off') # To turn off 4. YOU HAVE TO USE THIS ELSE YOU ARE FUCKED #
    
    elif(x=='10'):
        print('Parcel open')
        try:
            requests.get('http://192.168.4.1/5/on') # To bring the motor shaft back to initial position #
        except:
            print("ERROR:Failed to communicate to NodeMCU")
    elif(x=='11'):
        print('Parcel open_2')
        try:
            requests.get('http://192.168.4.1/5/off') #To turn off 5. YOU GOTTA DO THIS ELSE u kno
        except:
            print("ERROR:Failed to communicate to NodeMCU")

print('Exiting program')
g.cleanup()

