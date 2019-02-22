

import socket
import network
import machine as mc
from machine import Pin,ADC
import time,os
Trig,Echo = Pin(26,Pin.OUT,value=0),Pin(27,Pin.IN)
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

  
class WDOG():
  def __init__(self):
    self.timer = mc.Timer(-1)
    self.fed = False
  def feed(self):
    self.fed = True  
  def wdcb(self):
    pass
  def wdtcb(self,tmr):
    if not self.fed: 
      mc.reset()
    self.fed = False
    self.wdcb()
  def init(self,msec=5000):
    self.timer.init(period=msec, mode=mc.Timer.PERIODIC, callback=self.wdtcb)
    self.feed()


class Uclient(object):
    def __init__(self,host,port):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.host=host
        self.port=port
    def sendto(self,data):
        self.s.sendto(data,(self.host,self.port))

    def connetWifi(self,ssid,pwd):
        self.wlan=network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.disconnect()                                     #Disconnect the last connected WiFi
        self.wlan.connect(ssid,pwd)                             #connect wifi
        while(self.wlan.ifconfig()[0]=='0.0.0.0'):
            time.sleep(1)
        return True

if __name__ == '__main__':
    host="xxx"
    port=8848
    SSID="xxx"
    PASSWORD="xxx"
    test=Uclient(host,port)
    test.connetWifi(SSID,PASSWORD)
    wd = WDOG()
    wd.init(5000)
    while True:
      data=checkdist()
      test.sendto(str(data))    #send data
      wd.feed()
      time.sleep(1)

