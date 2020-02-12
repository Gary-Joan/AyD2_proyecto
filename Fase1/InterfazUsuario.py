import abc

class UserBase(abc.ABC):
    def __init__(self,cui,telefono,nombre,nit):
        self.cui = cui
        self.telefono = telefono
        self.nombre = nombre
        self.nit = nit
    
    def visualizar_contrato_behavior(self):
        return "visualizar contrato"

    def imprimir_behavior(self):
        return "imprimir behavior"

class AbstractUser(abc.ABC):
    def __init__(self,username,first_name,last_name,email,password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def set_password(self,old_password,new_password):
        if self.password == old_password:
            self.password = new_password
            return True
        else:
            return False

    def get_full_name(self):
        return self.first_name + self.last_name

    def login(self,username,password):
        if self.username == username and self.password == password:
            print('Login con exito')
            return True
        else:
            print('Login fallido')
            return False

