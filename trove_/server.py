# -*- coding: utf-8 -*-

import SocketServer
import sys
import .ssl

config.CLIENT_IP = "0.0.0.0"
config.CLIENT_PORT = 9770

d = ssl()

class RunServer(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        csr = self.request.recv(1024).strip()
        get_ssl_cert_status = d.get(csr)
        # send back data
        self.request.sendall(str(get_ssl_cert_status))


def parser():
    
    
def main():
    # Initialize IP and PORT
    HOST, PORT = parser()

    # Create the server, binding to 0.0.0.0 on port 9999
    server = SocketServer.TCPServer((HOST, PORT), RunServer)
    print("Running server on port {}".format(PORT))

    try:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit server...")
        sys.exit(0)
        
if __name__ == "__main__":
    t=main()
