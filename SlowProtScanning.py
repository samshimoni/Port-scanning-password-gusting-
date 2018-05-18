#!/usr/bin/env python
import socket
import subprocess
import sys
import time
import random
from datetime import datetime

class SlowScan(object):
    
    @classmethod
    def slowScanning(self,ip):

        secondForWait = input("Enter a number of seconds are waiting between each group of porters: ")

 
        remoteServer=ip
        remoteServerIP  = socket.gethostbyname(remoteServer)

        print "-" * 60
        print "Please wait, scanning remote host", remoteServerIP
        print "-" * 60

 

        HashMapOfPorts = {}
        try:
            for port in range(22,23): 
                if port%10==10:
                 time.sleep(secondForWait)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    HashMapOfPorts[port] = "Open"
                    print "Port {}:      Open".format(port)
                else:
                    HashMapOfPorts[port] = "Close"
                    print "Port {}:      Close".format(port)    
                sock.close()
                
             
            
            with open("SlowScanFile.txt", "w") as f:
                f.write('| Port number | Status |\n')
                for key, value in HashMapOfPorts.items():
                    f.write('| %s | %s |\n' % (key, value))
        
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()
        
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
