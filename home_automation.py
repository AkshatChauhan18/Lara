import socket
from colorama import Fore
def automate(command):
   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   sock.settimeout(6)
   try:
      sock.connect(('192.168.177.225',1234))
      if command == 0: 
         sock.send("0".encode())
      if command == 1: 
         sock.send("1".encode()) 
      sock.shutdown(socket.SHUT_RDWR)  

   except Exception as e :
      print(Fore.RED+f'{e}')
      print(Fore.WHITE)

if __name__ == '__main__':
   automate(0)