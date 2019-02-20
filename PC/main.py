import serial,time,ctypes


class Win_lock(object):
    def __init__(self,com,baudrate=115200):
        self.com=com
        self.baudrate=baudrate
        self.ser = serial.Serial(port=com,baudrate=self.baudrate)
        self.status=0

    def main(self):
        while 1:
            try:
                time.sleep(1)
                data=self.ser.read_all().decode()
                print(data)
                if len(data)<=8:
                    if int(data) >100:
                        if self.status==0:
                            res=ctypes.windll.user32.LockWorkStation()
                            self.status=res
                            print(res)
                        else:
                            pass
                    else:
                        self.status=0
                else:
                    pass
            except ValueError:
                pass

test=Win_lock('com4')
test.main()
