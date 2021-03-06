#!/usr/bin/env python
import socket
import subprocess
import sys
import time
from datetime import datetime

class EffectiveScan(object):
    """ smartScan function scans the well-known port
        and check if  port is open/close,
        export the tests to textFile"""
        
    @classmethod
    def effectiveScanning(self,ip):

        remoteServer=ip
        remoteServerIP  = socket.gethostbyname(remoteServer)
        
   
        print "-" * 60
        print "Please wait, scanning remote host", remoteServerIP
        print "-" * 60
        

        portSet=[1,5,7,9,11,13,17,18,19,20,21,22,23,25,26,29,35,37,38,39,41,42,43,49,53,57,67,68,69,70,79,80,88,101,102,103,107,108,109,110,111,113,115,117,118,119,123,135,137,138,139,143,150,156,161,162,170,179,190,194,197,201,209,213,218,220,259,264,311,318,323,366,369,371,384,387,389,396,401,411,427,443,444,445,458,464,465,500,512,513,514,515,517,518,520,524,525,530,531,532,533,540,542,543,544,546,547,548,550,554,556,560,561,563,569,587,591,593,604,631,636,639,646,647,648,652,654,665,666,674,691,692,695,698,699,700,701,702,706,711,712,720,749,750,782,829,860,873,901,902,911,981,989,990,991,992,993,995,1080]
   
        HashMapOfPorts = {}
        
        try:
            for i in range(len(portSet)):
                port=portSet[i]
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    HashMapOfPorts[port] = "Open"
                    print "Port {}:      Open".format(port)
                else:
                    HashMapOfPorts[port] = "Close"
                    print "Port {}:      Close".format(port)
                sock.close()
                
           
            
            with open("smartScanFile.txt", "w") as f:
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
