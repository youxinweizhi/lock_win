import serial,time,ctypes
def win_lock(com,baudrate=115200):
    status=0
    ser = serial.Serial(port=com,baudrate=baudrate)
    while 1:
        try:
            time.sleep(1)
            data=ser.read_all().decode()
            print(data)
            if len(data)<=8:
                if int(data) >100:
                    if status==0:
                        res=ctypes.windll.user32.LockWorkStation()
                        status=res
                        print(res)
                    else:
                        pass
                else:
                    status=0
            else:
                pass
        except ValueError:
            pass
if __name__ == '__main__':
    win_lock('com4')
