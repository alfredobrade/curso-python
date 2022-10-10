#Practico2 - Alfredo Brade
'''
#ejercicio1
dia1 = int(input('ingrese dia: '))
if dia == 1:
    print('¡Primer día del mes!')
#ejercicio2
n2 = int(input('ingrese un numero: '))
if n2%2 == 0:
    print('El numero ',n2,'es PAR')
else:
    print('El numero ', n2, 'es IMPAR')
#ejercicio3
n31 = int(input('ingrese un numero: '))
n32 = int(input('ingrese otro numero: '))
if n31%n32 == 0:
    print(n31,'es divisible por',n32)
elif n32%n31 == 0:
    print(n32, 'es divisible por', n31)
else:
    print('no son divisibles')
#ejercicio4
frase4 = input('ingrese una frase')
palabra4 = input('ingrese una palabra')
if palabra4 in frase4:
    print(palabra4,'está incluido en la frase "',frase4 +'…”')
#ejercicio5
n51 = int(input('ingrese un numero: '))
n52 = int(input('ingrese otro numero: '))
if n51 > n52:
    print(n51,'es mayor que ',n52)
else:
    print(n52, 'es mayor que', n51)
#ejercicio6
n61 = int(input('ingrese primer numero: '))
n62 = int(input('ingrese segundo numero: '))
n63 = int(input('ingrese tercer numero: '))
print('primero',n61)
print('primero',n62)
print('primero',n63)
if (n61 > n62)&(n63 > n62):
    print(n62, "es el minimo")
elif (n61 > n63)&(n62 > n63):
    print(n63, "es el minimo")
else:
    print(n61, "es el minimo")
#ejercicio7
name7 = input('Nombre de usuario: ')
pass7 = input('Contraseña: ')
if (name7 == 'Gwenevere')&(pass7 == 'excalibur'):
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')
#ejercicio8
año8 = int(input('ingrese año: '))
if (año8%4 == 0)&(año8%100 != 0):
    print('año bisiesto')
elif (año8%4 == 0)&(año8%100 == 0)&(año8%400 == 0):
    print('año bisiesto')
else:
    print('año no bisiesto')
#ejercicio9
n9 = int(input('ingrese un numero: '))
for i in range(n9):
    print(i + 1)
#ejercicio10
m10=0
for n10 in range(101):
    m10 = m10 + n10
print(m10)
#ejercicio11
n11 = int(input('ingrese un numero entero positivo: '))
c11 = 0
for m11 in range(n11):
    c11 = c11 + m11**3
print(c11)
#ejercicio12
acumPOS = 0
acumNEG = 0
contPOS = 0
for i in range(6):
     num = int(input('ingrese un numero entero'))
     if num >= 0:
         acumPOS += num
         contPOS += 1
     else:
         acumNEG += num
print('sumatoria de los negativos',acumNEG)
if contPOS > 0:
    print('promedio de los positivos',acumPOS/contPOS)
else:
    print('no se ingresaron numeros positivos')
#ejercicio13
cadena13 = input('Ingrese una cadena de texto: ')
acum13 = 0
for i in cadena13:
    if i in 'aeiouAEIOU':
        acum13 += 1
if acum13 > 0:
    print('La cadena tiene vocales')
#ejercicio14
num14 = int(input('Ingrese un numero: '))
if num14==0 or num14==1:
        print(num14,' no es un numero valido')
else:
    if num14==2:
        print(num14,' es un numero primo')

    else:
        if num14%(2) != 0:
            print(num14,' es un numero primo')
        else:
            print(num14,' no es primo')
#ejercicio15
#Escriba un programa que, dada una frase por el usuario, muestre la cantidad total de vocales (tanto mayúsculas como minúsculas) que contiene
frase15 = input('ingrese una frase: ')
acum15=0

for i in frase15:
    if i in 'aeiouAEIOU':
        acum15 +=1
print('frase: ',frase15,'\nvocales: ',acum15)

#Frase: Verde que te quiero verde
#Vocales: 11

#ejercicio16
#Escribí un programa que muestre los primeros 10 números de la sucesión de Fibonacci.
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números
# anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
a16=1
b16=1
print('0')
print(a16)
print(b16)
for i in range(10-3):
    total16 = a16 + b16
    b16=a16
    a16= total16
    print(total16)

'''