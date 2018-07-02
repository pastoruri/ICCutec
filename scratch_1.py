#Conversión de unidades: by Rodrigo C and Kurt O
print("metros por segundo a kilómetros por hora---1")
print("kilómetros por hora a metros por segundo---2")
print("metros cúbicos a Litros--3")
print("Litros a metros cúbicos--4")
n=int(input("Elija la opcción que usted prefiera"))
print("----------------------------")
if n ==1:
    a=float(input("Ingrese metros por segundo:"))
    b=float(a*3.6)
    print(b,"kilómetros por hora")
elif n ==2:
    c=float(input("Ingrese kilómetros por hora:"))
    d=float(c/3.6)
    print(d, "metros por segundo")
if n ==3:
    c=float(input("Ingrese metros cúbicos:"))
    d=float(c*1000)
    print(d, "litros")
if n ==4:
    c=float(input("Ingrese litros:"))
    d=float(c/1000)
    print(d, "metros cúbicos")
