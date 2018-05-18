
#!/usr/bin/env python
import socket
import subprocess
import sys
import time
import random
from datetime import datetime

class RandomScan(object):
    """ randomScan function scans 21 random ports between 1 to 1025 (not include) 
        and check if  port is open/close,
        export the tests to textFile"""
    
    @classmethod
    def randomScanning(self,ip):
        
      
        # Clear the screen
        #subprocess.call('clear', shell=True)
            
        # Ask for input
        #remoteServer    = raw_input("Enter a remote host to scan: ")
        remoteServer=ip
        remoteServerIP  = socket.gethostbyname(remoteServer)
        
        # Print a nice banner with information on which host we are about to scan
        print "-" * 60
        print "Please wait, scanning remote host", remoteServerIP
        print "-" * 60
             
        HashMapOfPorts = {}
        
        try:
            
            portSet=set()
            
            for i in range(1,21):
        
                
                randomPort = random.randint(1,1025)
                
               
                while randomPort in portSet:
                    randomPort = random.randint(1,1025)
                
         
                portSet.add(randomPort)
                
             
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, randomPort))
                if result == 0:
                    HashMapOfPorts[randomPort] = "Open"
                    print "Port {}:      Open".format(randomPort)
                else:
                    HashMapOfPorts[randomPort] = "Close"
                    print "Port {}:      Close".format(randomPort)
                    
                sock.close()
                
       
            
            with open("randomScanFile.txt", "w") as f:
                f.write('| Port number | Status |\n')
                for key, value in HashMapOfPorts.items():
                    f.write('| %s | %s |\n' % (key, value))
        
        except KeyboardInterrupt:
            print "\nYou pressed Ctrl+C"
            sys.exit()
        
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
            
       
