from meinePins import *
import machine
button  = machine.Pin(BUTTON, machine.Pin.IN, machine.Pin.PULL_DOWN)
tasterL = machine.Pin(TASTER_L, machine.Pin.IN, machine.Pin.PULL_DOWN)
tasterR = machine.Pin(TASTER_R, machine.Pin.IN, machine.Pin.PULL_DOWN)