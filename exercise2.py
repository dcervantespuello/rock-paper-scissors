try:
  number = int(input("Ingresa un número: "))
  if number % 2 == 0:
    print("El número es par")
  else:
    print("El número es impar")
except ValueError:
  print("El valor ingresado no es un número")