






#Ejercicio 7
print("Programa de inversiones Marimar: ")
cant_invertir = int(input("¿Cuánto dindero desea invertir?   "))
interesAnual = float(input("Porcentaje de interes esperado:  "))
capital = ((cant_invertir*interesAnual)/100)
valor = (capital + cant_invertir)
print("Teniendo en cuenta sus condiciones se estaria generando un capital al año de $ {} COP".format(valor))

#Ejercicio 6
print("Este juego consiste en que te enseñe que hago a veces con los números que me entregas.")
n= int(input("Digita un número entero: "))
m = int(input("Digita un número entero: "))
c = n//m
r = n%m
print("el {} entre {} da un cociente {} y un resto {} donde {} y {} son los números introducidos por el usuario, y {} y {} son el cociente y el resto de la division entera respectivamente.".format(n,m,c,r,n,m,c,r))


#Ejercicio 5

peso = float(input("¿Cuánto pesas?"))
estatura = int(input("¿cuál es tu estatura?"))
imc = round(peso/estatura,2)
print("¿Haz escuchado hablar del indice de masa corporal?")
print ("el tuyo es {}".format(imc))
print("¡Deberias preguntarte si estas dentro de los normal!")

# Ejercicio 1
print("Hola, ¿Cómo te llamas?")
name = input()
print("Hola, ", name)

#Ejercicio 2
print("Preparate para esta operación: ")
a = 3
b = 2
c = 5

print("Estos son los datos: {}, {} y {}".format(a,b,c))
operacion = (((a+b)/(b*c))**b)
print("La siguiente es la operación: (((a+b)/(b*c))**b)")
print("por consiguiente el resultado: {}".format(operacion))

#Ejercicio 3

hora_laboral = int(input("Digite el número de horas trabajadas: "))
pago = int(input("Digite el valor por hora laborada: "))
costo = hora_laboral*pago

print("El valor que le corresponde por sus horas laboradas es de $ {} COP".format(costo))

#Ejercicio 4

n = int(input("Dame un número para contar: "))
suma = ((n*(n+1))/2)
print("la suma de los primeros numeros enteros desde 1 hasta {} es {}".format(n,suma))

