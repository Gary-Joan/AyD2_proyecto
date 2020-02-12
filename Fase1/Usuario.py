from InterfazUsuario import UserBase, AbstractUser

class Gerente(AbstractUser,UserBase):
    def __init__(self,username,first_name,last_name,email,password,telefono,cui,nit):
        self.telefono = telefono
        self.cui = cui
        self.nit = nit
        super(Gerente,self).__init__(username,first_name,last_name,email,password)
        print("Tengo a un gerente")

class Cliente(UserBase):
    def __init__(self):
        super(Cliente,self).__init__()
        print("tengo a un cliente")

g = Gerente('gerente1','luisa','lopez','gerente1@gmail.com','1234','12345678','1234567891','124563')
g.login('gerent1','1234')