#Verificar si un número es par o impar:
num = 6
mensaje = "Par" if num % 2 == 0 else "Impar"
print(mensaje)  # Esto imprimirá "Par" porque 6 es par

#Calcular el mayor de tres números:
a = 10
b = 20
c = 15
mayor = a if a > b and a > c else b if b > c else c
print(mayor)  # Esto imprimirá 20 porque es el mayor de los tres números