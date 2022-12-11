import utime
import machine
from sensor_Licht import *
#from Motor import *

LEDW = 5 # Testen!!!
led = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)

def kalibrieren(sensor,anzahl=500):
    for i in range(anzahl):
        sensor.kalibrierRunde()
        utime.sleep(0.01)

if __name__=="__main__":
    led.on() 
    sensor=Sensor(LEDW,"weiss")    
    print("Kalibrieren")
    kalibrieren(sensor)
    print("Kalibrieren fertig!")        
    
    print(sensor.name)
    sensor.zeigeMinMax()
    utime.sleep(3)        
    while not button.value():#zum beenden
        sensor.messen()
        diff=sensor.wertL-sensor.wertR
        print(n, sensor.wertL, sensor.wertR,diff)
        utime.sleep(0.4)        
    led.off()
    
    