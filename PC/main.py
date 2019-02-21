import serial,time,ctypes
import serial.tools.list_ports

class Get_all_com(object):
    def main(self):
        port_list = list(serial.tools.list_ports.comports())
        for x in port_list:
            print(list(x))

class Win_lock(object):
    def __init__(self,vid,baudrate=115200):
        self.vid=vid
        self.com=self.get_com(self.vid)
        self.baudrate=baudrate
        self.ser = serial.Serial(port=self.com,baudrate=self.baudrate)
        self.status=0
    def get_com(self,vid):
        port_list = list(serial.tools.list_ports.comports())
        for x in port_list:
            if vid in x[2]:
                com=x[0]
                return com
    def main(self):
        while 1:
            try:
                time.sleep(1)
                data=self.ser.read_all().decode()
                print(data)
                if len(data)<=8:
                    if int(data) >80:
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

test=Win_lock('10C4')
test.main()

