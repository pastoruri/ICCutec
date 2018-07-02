#Conversión de unidades
print("m/s a km/h---1")
print("km/h a m/s---2")
print("m3 a Litros--3")
print("Litros a m3--4")
n=int(input("Elija la opcción que usted prefiera"))
print("----------------------------")
if n ==1:
    a=float(input("Ingrese cantidad de m/s:"))
    b=float(a*3.6)
    print(b,"kilómetros por hora")
elif n ==2:
    c=float(input("Ingrese cantidad de km/h:"))
    d=float(c/3.6)
    print(d, "metros por segundo")
if n ==3:
    c=float(input("Ingrese cantidad de m3:"))
    d=float(c*1000)
    print(d, "litros")
if n ==4:
    c=float(input("Ingrese cantidad de litros:"))
    d=float(c/1000)
    print(d, "metros cúbicos")
