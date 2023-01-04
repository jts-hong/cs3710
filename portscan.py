import socket
import sys
from datetime import datetime

### Asking for inputs including targets and ranges 
target=input("Enter a target to scan: ")
print("Please enter the range of ports you would like to scan on the target:")
range_start = int(input("Enter a start port: "))
range_end = int(input("Enter a end port: "))

### Display Start Time
print("Scanning started at:" + str(datetime.now()))

### Start Scanning 
port_open=[]
     
### Scans ports between range_start to range_end
for port in range(range_start,range_end):
        
        ### Set up sockets
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:     
                # returns an error indicator
                result = s.connect_ex((target,port))

        except KeyboardInterrupt:
                sys.exit()
        except socket.gaierror:
                sys.exit()
        except socket.error:
                sys.exit()

        ### Display Results
        if result ==0:
                print("Port {} is open".format(port))
                port_open.append(port)
        else:
                print("Port {} is closed".format(port))
        s.close()

### Dealing wiht Errors and exits

print("Port Scanning Completed")
#print(port_open)