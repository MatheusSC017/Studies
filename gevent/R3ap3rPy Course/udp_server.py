from gevent.server import DatagramServer


class EchoServer(DatagramServer):
    def handle(self, data, address):
        print(f"Address: {address[0]}, data: {data}")
        self.socket.sendto(f"Recieved {len(data)} bytes!".encode("utf-8"), address)


print(f"Receiving datagrams on port 9000")
EchoServer(':9000').serve_forever()
