
class User:
    def __init__(self):
        self.email = input("Registre su correo electronico:")
        self.__password = input("Cree una contraseña:")
        self.permission = ["editar", "subir", "crear"]
        self.username = None

    def setear_username(self):
        self.username = input("Cree su nombre de usuario:")
        print("Se ha creado exitosamente su usuario: {}".format(self.username))

class UserPro(User):
    def __init__(self):
        super().__init__()  # Llamo a la clase padre
        self.permission = ["descargar", "eliminar"]

    def pago_suscripcion(self, monto):
        print("Usted ha pagado exitosamente {}".format(monto))

class UserManager:
    def __init__(self, suscripcion):
        if suscripcion:
            self.user = UserPro()
        else:
            self.user = User()
        print("Se ha creado exitosamente su usuario {}. Sus permisos son: {}".format(self.user, self.user.permission))

UserManager(True)  # Crear un usuario con suscripción
print(User().__password)  # No se puede acceder directamente al password por ser privado (__password)

print(User)