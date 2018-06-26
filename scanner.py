import socket
"""import the module socket"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""AF_INET is an address family that is used to designate the type
of addresses that your socket can communicate with
(in this case, Internet Protocol v4 addresses)"""
"""SOCK_STREAM means that it is a TCP socket.
SOCK_DGRAM means that it is a UDP socket."""

server = "mail.google.com"

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,10):
    if pscan(x):
        print 'open port: ' ,x
    else:
        print 'closed port: ',x
