

from machine import Pin,I2C
import ssd1306
import socket
import network
import time

i2c = I2C(scl=Pin(4), sda=Pin(5), freq=900000)
oled = ssd1306.SSD1306_I2C(128,64, i2c)
oled.poweron()
oled.init_display()
oled.fill(0)
oled.show()

port=8848
SSID="xxx"
PASSWORD="xxx"
wlan=None
s=None

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
  if(connectWifi(SSID, PASSWORD) == True):              #judge whether to connect WiFi
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create socket
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #Set the value of the given socket option
    ip=wlan.ifconfig()[0]                               #get ip addr
    s.bind((ip,port))                                   #bind ip and port
    oled.text('waiting...',0,0,1)
    oled.show()
    while True:
      data,addr=s.recvfrom(10)  
      res=data.decode()
      T=time.time()
      if res=="1":
        Pin(2,Pin.OUT).value(0)
      else:
        Pin(2,Pin.OUT).value(1)
      oled.fill(0)
      oled.text('res:%s' %res,0,10,1)
      oled.text('time:%s' %T,0,20,1)
      oled.text('sleep_time:',0,30,1)
      oled.text('%.1f min' %(T/60),30,40,1)
      oled.show()
      time.sleep(0.5)
except:
  pass






