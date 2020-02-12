from InterfazUsuario import UserBase, AbstractUser

class Gerente(AbstractUser,UserBase):
    def __init__(self,username,first_name,last_name,email,password,telefono,cui,nit):
        AbstractUser.__init__(self,username,first_name,last_name,email,password)
        UserBase.__init__(self,cui,telefono,first_name+" "+last_name,nit)
        print("Tengo a un gerente")

class Cliente(UserBase):
    def __init__(self,nombre,cui,telefono,nit,*args,**kwargs):
        super(Cliente,self).__init__(nombre,cui,telefono,nit)
        print("tengo a un cliente")

print("------------- GERENTE  --------------")
g = Gerente('gerente1','luisa','lopez','gerente1@gmail.com','1234','12345678','1234567891','124563')
g.login('gerente1','1234')
g.set_password('1234','12345')
g.login('gerente1','12345')
print(g.get_full_name())
print(g.visualizar_contrato_behavior())
print(g.imprimir_behavior())
print(g.cui)
print(g.telefono)
print(g.nombre)
print(g.nit)
print(g.visualizar_contrato_behavior())
print(g.imprimir_behavior())

print("------------- CLIENTE  --------------")
c = Cliente('Cliente 1','123456789','12345678','12345-9')
print(c.cui)
print(c.telefono)
print(c.nombre)
print(c.nit)
print(c.visualizar_contrato_behavior())
print(c.imprimir_behavior())