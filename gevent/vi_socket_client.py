import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect('./socket_server.py.sock')
s.send(b'GET / HTTP/1.0\r\n\r\n')
data = s.recv(1024)
print(f"We recieved {len(data)} bytes")
print(data)
s.close()
