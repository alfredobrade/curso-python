#Alfredo Nicolás Brade DNI 36673519
#ejercicio1
nombre = input("tu nombre: ")
print("bienvenido al curso de introduccion a la programacion en python ",nombre,"!")
#ejercicio2
a = float(input("primer numero (con decimales)"))
b = int(input("segundo numero (entero)"))
c=a+b
print("el resultado de la suma es ",c)
#ejercicio3
print("Uso: comando [OPCIONES]\n\t-h\t\t\tMostrar este mensaje de uso\n\t-H hostname\t\tHostname a conectarse")
#ejercicio4
a4 = int(input('ingrese un numero: '))
b4 = int(input('ingrese otro numero: '))
c4 = a4 + b4
print('suman: ',c4)
d4 = int(input('ingrese un nuevo numero: '))
e4 = c4 * d4
print('multiplicacion de la suma por el ultimo numero: ',e4)
#ejercicio5
pi = 3.141593
r = int(input('ingrese el radio: '))
area = pi * (r ** 2)
print('area circunferencia: ',area)
#ejercicio6
km = int(input('kilometros recorridos: '))
litros = int(input('litros de combustible: '))
consumo = litros / km
print('el consumo por kilometro es de: ',consumo)
#ejercicio7
nombre7 = str(input('ingrese nombre: '))
apellido7 = str(input('ingrese apellido: '))
print('tu nombre y apellido:',apellido7,nombre7)
#ejercicio8
n = int(input('ingrese valor de n: '))
a8 = n+n*n+n*n*n
print('resultado',a8)
#ejercicio9
r = 6
vol9 = (4/3)*pi*(r**3)
print('vol esfera de radio 6: ',vol9)
#ejercicio10
temp = int(input('ingrese temperatura expresada en farenheit: '))
celsius = (5/9)*(temp-32)
print('temperatura empresada en celsius: ',celsius)
#ejercicio11
nombre11 = input('ingrese nombre: ')
edad11 = int(input('ingrese edad: '))
domicilio11 = input('ingrese domicilio: ')
print(nombre11,'\n',edad11,'\n',domicilio11)
#ejercicio12
x12 = int(input('ingrese x:'))
y12 = int(input('ingrese y:'))
resultado12 = (x12+y12)*(x12+y12)
print('resultado: ',resultado12)
#ejercicio13
a13 = float(input('ingrese primero:'))
b13 = float(input('ingrese segundo:'))
c13 = float(input('ingrese tercero:'))
p13 = (a13+b13+c13)/3
print('promedio de los 3 es: ', p13)
#ejercicio14
n14 = int(input('ingrese un numero'))
n14menos15 = n14*0.85
print('descontando el 15% queda: ',n14menos15)
#ejercicio15
a15 = input('primera palabra: ')
b15 = input('segunda palabra: ')
c15 = a15+' '+b15
print(c15)
#ejercicio16
texto16 = input('ingrese texto: ')
print(texto16[0])
largotexto = len(texto16)
indice = int(input('numero menor a '+str(largotexto)+': '))
print('los caracteres hasta esa posicion son: ',texto16[1:indice])