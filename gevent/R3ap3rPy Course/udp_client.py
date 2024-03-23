from gevent import socket
import sys

address = ('127.0.0.1', 9000)
message = ' '.join(sys.argv[1:])
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.connect(address)
print(f"Sending message!")
sock.send(message.encode())
data, address = sock.recvfrom(8192)
print(f"Got: {address}, {(data, )}")
sock.close()
