
import time
from machine import Pin   
Trig,Echo = Pin(26,Pin.OUT),Pin(27,Pin.IN)
Trig.value(0)
Echo.value(0)
def checkdist():
    Trig.value(1)
    time.sleep(0.00001)
    Trig.value(0)   
    while(Echo.value()==0):
        pass  
    t1 = time.ticks_us()
    while(Echo.value()==1):
        pass
    t2 = time.ticks_us()
    t3 = time.ticks_diff(t2,t1)/10000
    return int(t3*340/2)  
try:
    while 1:
        #print('Distance:%0.2f cm' %checkdist())
        print(checkdist())
        time.sleep(1)
except KeyboardInterrupt:
    pass
    


