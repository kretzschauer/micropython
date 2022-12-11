from machine import Pin
from machine import PWM
import time

in1 = Pin(14, Pin.OUT)
in2 = Pin(15, Pin.OUT)
in3 = Pin(12, Pin.OUT)
in4 = Pin(13, Pin.OUT)

p1 = PWM(Pin(14))
p2 = PWM(Pin(15))
p1.freq(1000)
p2.freq(1000)

p3 = PWM(Pin(12))
p4 = PWM(Pin(13))
p3.freq(1000)
p4.freq(1000)

MOT_A  = 1
MOT_B  = 2
MOT_AB = 3

def OnPwm(pin1, pin2, v):
    if v == 0:
        pin1.duty_u16(0)
        pin2.duty_u16(0)
        return
    if (v>0):
        if v>100: v=100# Begrenzung
        pin2.duty_u16(0)
        pin1.duty_u16(v*600)
        return
    if (v<0):
        if v<-100:v=-100
        pin1.duty_u16(0)
        pin2.duty_u16(-v*600)
        return

def Off():
    OnFwd(MOT_AB,0)

def OnFwd(mot, v):
   if mot & MOT_A:
       OnPwm(p1,p2, v)
   if mot & MOT_B:
       OnPwm(p3,p4, v)
       
# Test des Moduls
if __name__=="__main__":
    print("vor")
    for i in range(20,60):
        OnFwd(MOT_B, i*2)
        print(i*2)
        time.sleep(0.2)
    Off()
    print("stop")
    time.sleep(2)
    for i in range(20,70):
        OnFwd(MOT_B, -i*2)
        time.sleep(0.2)

    OnFwd(MOT_AB, 0)
