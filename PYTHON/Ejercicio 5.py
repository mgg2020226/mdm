class CuentaJoven:
    def __init__(self):
        self.name = None
        self.año = int(input("Digite su año de nacimiento"))
        self.calcular_edad = int(self.año/2024)    #al año de nacimiento se constrasta para verificar la condicion de mayor de edad
        while self.calcular_edad >= 18 and i <=25: # mienstra su edad no sea mayor o igual de 18 a 25 años

            if i < 26 and i > 17:
                i = self.calcular_edad
                print("Titular de Cuenta Joven aceptado")
                continue
            else:
                print("Titular de cuenta Joven rechazada")
                break
            
        self.monto = int(input("Monto inicial que agregaria a su cuenta:"))
# metodos
    def mostrar_edad(self):
        print("Edad: {}".format(self.calcular_edad))
    
    def mostrar_valor(self):
        if i >=18 and i <=25: # si la cuenta es aceptada
            i = self.calcular_edad
            print("el saldo de su cuenta se cuentra en ${}".format(self.monto))
        else: # recuerda: debe regresar a ingresar nuevamente la fecha de nacimiento
            print("Transferencia rechazada")