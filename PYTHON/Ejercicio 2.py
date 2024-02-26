class Animal:
#constructor
    
    def __init__(self):
        self.edad= None
        self.especie = Perro
        self.pelaje = None

#métodos de la clase padre
        
    def comer(self):
        print("el animal esta comiendo")

    def reproducirse(self):
        print("el animal se esta reproducciendo")

#Ejemplo de Herencia 
        
class Perro(Animal): 

    def __init__(self,n,r,c):
        super().__init__()                                  #Permiso que nos otorga hacer uso de los métodos de la clase padre
        self.nombre = n
        self.raza = r
        self.color = c

#Vamos por los métodos
        
    def ladrar(self):
        print("{} esta ladrando".format(self.nombre))
        
    def jugar(self):
        print("{} esta jugando en el parque".format(self.nombre))

    def check_hambre(self,hambre): 
        if hambre:                                         # utilizamos condicionales
            self.comer()                                   # Asi se llama a un método dentro de la misma clase
        else:
            print("{} no esta hambriento".format(self.nombre))

#Vamos a instanciar NUEVAMENTE, pero con el principio de la herencia
            
tomy = Perro("Tomy", "Pitbull","Marron")
tomy.reproducirse()
tomy.check_hambre(False)


rex = Perro("Rex", "Pitbull","Marron")
rex.jugar()
rex.check_hambre(False)
