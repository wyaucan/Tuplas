#Escribir un programa que pregunte al usuario su edad y muestre
#por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese la edad: "))

for i in range(edad):
    i+=1;
    print("Has cumplido", i, "años")