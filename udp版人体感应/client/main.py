

import machine
from machine import Pin
import socket
import network
import time
host='192.168.5.135'
port=8848
SSID="xxx"
PASSWORD="xxx"
wlan=None
s=None


def get_data(num):
  p=Pin(num,Pin.IN)
  return p.value()


def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)                     #create a wlan object
  wlan.active(True)                                     #Activate the network interface
  wlan.disconnect()                                     #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                             #connect wifi

  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  if(connectWifi(SSID,PASSWORD) == True):           #judge whether to connect WiFi
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create socket
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #Set the value of the given socket option
    ip=wlan.ifconfig()[0]                           #get ip addr
    while True:
      data=get_data(12)
      s.sendto(str(data),(host,port))    #send data
      time.sleep(0.5)
except OSError:
  machine.reset()



