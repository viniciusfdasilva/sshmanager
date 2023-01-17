from ssh.app.models import Server

class DatabaseManager():

    @staticmethod
    def save_server(ip, username, password):
        
        try:
            
            Server.objects.create(ip=ip, username=username, passowrd=password).save()
            return True
        
        except Exception:
            return False