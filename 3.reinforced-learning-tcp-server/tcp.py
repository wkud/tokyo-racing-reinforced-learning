import socket

class Tcp:
    def __init__(self, port, timeout = 5.0):
        self.port = port
        self.timeout = timeout
        
        self.serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serwer.bind(('', port))
        self.serwer.listen(5)
        
        self.client = None

    def accept_client(self):
        print('Waiting')
        self.client, address = self.serwer.accept()
        print('Connected with client')

    def try_receive_msg(self):
        msg = ''
        is_connection_lost = False
        try:
            self.client.settimeout(self.timeout)
            msg = self.client.recv(1024)
            self.client.settimeout(None)
        except:
            is_connection_lost = True
            
        return msg, is_connection_lost
    
    def send(self, data_to_send):
        self.client.send(bytes(data_to_send, 'utf-8'))