class Perro:
#Vamos por los atributos
    def __init__(self,n,r,c):
        self.nombre = n
        self.raza = r
        self.color = c
        self.edad = 1
#Vamos por los métodos
    def ladrar(self):
        print("{} esta ladrando".format(self.nombre))

    def comer(self):
         print("{} esta comiendo".format(self.nombre))
        
    def jugar(self):
        print("{} esta jugando en el parque".format(self.nombre))
        
#Vamos a setter y/o getter
    def cambiar_nombre(self,nombre):
        self.nombre = nombre
        print("el perro ahoraa se llama {} por cuestiones prácticas".format(nombre))

    def cambiar_edad(self,edad):
        self.edad = edad
        print("{} ahora tiene {} años".format(self.nombre, self.edad))
       
    def cumpleaños(self):
        self.edad += 1
        print("{} ahora tiene {} años".format(self.nombre, self.edad))

#Un ejemplo de cómo instanciar
#un objeto de manera práctica
   
tomy = Perro("Tomy", "Pitbull","Marron")
print(tomy.nombre)
tomy.comer()
tomy.cumpleaños()

rex = Perro("Rex", "Pitbull","Marron")
rex.jugar()
rex.cambiar_edad(5) #Ahora tendrá 5 años 
