##Definicion de variables:

nombre = str (input ("escribe tu nombre"))
edad = int (input ("escribe tu edad"))
estatura =  float (input ("escribe tu estatura"))
toma = bool (input ("usted toma escriba falso o verdadero"))
print (f"hola mi nombre es {nombre}", f"mi edad es {edad}", f"mido {estatura}", f"actual mente {toma}")

##Ivestigacionn sobre el limite de los numeros flotantes y los numeros enteros 
"""
la capaciadad maxima de un numero entero se determina por la  memoria que tenga 
la maquina (compoutadura) en sistemas de 64 bits la capacidad es mayor que a la de un sistema con memoria de 
32bits.
por el otro lado la capacidad maxima de un  numero de punto flotante tienen una precision de finita, 
por lo cual hay limites para la precision generalmente tienen una precisión de 53 bits en una máquina de 64 bits
lo que significa que pueden representar números con una gran cantidad de dígitos, pero no pueden representar
todos los números de manera exacta debido a la limitación de la precisión.
"""
##Aplicando la suma de numeros enteros
print("ingrese el numero inicial")
i = int(input())
print("ingrese el numero final")
f = int(input())
suma = 0
print("**Los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print (i)
        suma = suma+i
    i+=1    
print("la suma de los numeros es", suma)

"""
la verdad hice la suma asi por que casi no entendi y siendo sinvero es que pregunte por todos los grupos 
y nadie me dio respuesta asi que lo hice con un tutarial de yootube no se ni como lo hice :)
"""