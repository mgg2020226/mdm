
class Motocicleta:

#constructor
    
    def __init__(self, m):
        self.combustible_litros = 10
        self.numero_ruedas = 2
        self.motor = False
        self.pago = 1250
        self.marca = m
       

#metodos
        
    def arrancar(self):
        if self.motor is False:
            print("El motor ha arrancado")
        else:
            print("el motor ya estaba en marcha")

    def detener(self):
        if self.motor is False:
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")
    
    def precio(self):
        print("el valor de la motocileta es de ${} COP".format(self.pago))
    
    def registrar_marca(self,marca):
        self.marca = marca
        print("{}".format(self.marca))
#intento de instanciar un objeto

Moto1 = Motocicleta("Yamaha")
#debe instanciar marca
#debe instanciar precio


Moto2 = Motocicleta("Dukati")
#debe instanciar numero_rueda
#debe instanciar el estado del motor

#Vamos ha acceder a los metodos y atributos


