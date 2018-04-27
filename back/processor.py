#--*-- coding:utf-8 --*--
import  socket
from utils.defines import ServerIP,ServerPort

class client:
    def __init__(self):
        self.address=((ServerIP,ServerPort))
        self.socket=None


    def connect(self):
        try:
            self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.connect(self.address)
        except socket.error as e:
            print str(e)

    def processData(self):
        while True:
            data=self.socket.recv(1024)
            return data











