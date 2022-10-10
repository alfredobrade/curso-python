#practico3 Alfredo Brade
#ejercicio1
def esPar (numero):
    return numero % 2 == 0
def ejercicio1 ():
    acumImpar = 0
    acumPar = 0
    for i in range(10):
        numero = int(input("numero: "))
        if esPar(numero):
            acumPar += numero
        else:
            acumImpar += numero
    print('suma de pares: ',acumPar)
    print('suma de impares: ',acumImpar)
#ejercicio1()

#ejercicio2
def sumatoriaDigitos (numero):
    sum=0
    while (numero != 0):
        sum += (numero % 10)
        numero = numero // 10
    return sum

def ejercicio2 ():
    num = int(input('escriba un numero: '))
    while num != 100:
            print('suma de los digitos: ',sumatoriaDigitos(num))
            num = int(input('escriba un numero: '))
#ejercicio2()

#ejercicio3
def esPar (numero):
    return numero % 2 == 0
def sumatoriaDigitos (numero):
    sum=0
    while (numero != 0):
        sum += (numero % 10)
        numero = numero // 10
    return sum
def ejercicio3 ():
    contImp = 0
    num = 0
    while ((sumatoriaDigitos(num) < 1000)&(num % 5 != 0)):
        num = int(input('escriba un numero: '))
        if not esPar(num):
            contImp += 1

    print('cantidad de impares: ', contImp)
#ejercicio3()

#ejercicio4
def esPrimo (numero):
    for i in range(2,numero):
        if numero%(i)==0:
            return False
    if numero<2:
        return False
    else:
        return True

def ejercicio4():
    num=int(input('numero entero: '))
    contPrimo=0
    while str(num)[0]!='9':
        if esPrimo(num):
            contPrimo+=1

        num=int(input('numero entero: '))

    print('cantidad de nuemeros primos ingresados: ', contPrimo)

#ejercicio4()

#ejercicio5
def palindromo(cadena):
    largoCadena=len(cadena)-1
    for i in range(largoCadena // 2):
        if (cadena[i]!=cadena[largoCadena-i]):
            return False
    return True

def ejercicio5():
    palabra = input('ingrese una palabra: ')
    contPal=0
    while palabra != 'fin':
        if palindromo(palabra):
            contPal +=1

        palabra = input('ingrese una palabra: ')
    print('cantidad de palindromos: ', contPal)

#ejercicio5()



#ejercicio6 Escriba un programa para sumar todos los elementos de una lista.

def sumarLista (listaNumeros):
    sum = 0
    for i in listaNumeros:
        sum += i
    print('suma de los elementos de la lista', listaNumeros, 'es: ',sum)

def ejercicio6():
    numero = int(input('ingrese un numero distinto de 0:'))
    lista = []
    while numero != 0:
        lista.append(numero)
        numero = int(input('ingrese un numero distinto de 0:'))
    sumarLista (lista)
#ejercicio6()

#ejercicio7
def ejercicio7 ():
    lista = ['rojo', 'verde', 'blanco', 'negro','rosa','amarillo']
    lista.remove(lista[5])
    lista.remove(lista[4])
    lista.remove(lista[0])
    print(lista)
#ejercicio7()
#ejercicio8
def ejercicio8 ():
    lista = ['abc','xyz', 'aba','1221','a','amiga','neuquen']
    contCadena = 0
    for cadena in lista:
        largoCadena = len(cadena)
        if (largoCadena >= 2)&(cadena[0] == cadena[largoCadena - 1]):
            contCadena += 1
    print('salida: ', contCadena)
#ejercicio8()

#ejercicio9


#ejercicio9()

#ejercicio10
def ejercicio10():
    lista = [1,2,3,4]
    entrada = int(input('ingrese un elemento: '))
    indice = -1

    for elem in lista:
        if elem == entrada:
            indice = lista.index(elem)

    if (indice > -1):
        print('el elemento', entrada, 'se encuentra en el indice',indice+1, 'de la lista')
    else:
        print('el elemento', entrada, 'no se encuentra en la lista')
#ejercicio10()

#ejercicio11

def ejercicio11():
    lista =['p','q']
    n =int(input('ingrese un numero: '))
    lista2=[]
    for i in range(1, n+1):
        for cadena in lista:
            lista2.append(cadena+str(i))
    print(lista2)

#ejercicio11()

#ejercicio12 Escriba un programa para seleccionar los números primos de una lista



#ejercicio13
def ejercicio13():
    lista=['a','b','c','c','d','e','f','g','h','i','j','k','l','m','n']
    lista2=[]
    largoSublista=int(input('ingrese un numero: '))
    largoLista=len(lista)
    cantSublistas=(largoLista//largoSublista)+1
    for i in range(cantSublistas):
        listaAux=[lista[i]]

        for j in range(i, largoSublista):
            if (j*3<largoLista):
                listaAux.append(lista[j*3])
        lista2.append(listaAux)
    print(lista2)

#ejercicio13()

A = int(input('ingrese A '))