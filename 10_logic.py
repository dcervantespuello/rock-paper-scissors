# Operadores lógicos
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)
print(not (True and True))
print(not (True and False))
print(not (False and True))
print(not (False and False))
print(not (True or True))
print(not (True or False))
print(not (False or True))
print(not (False or False))
print((True and True) or False)
print((True and False) or True)
print((False and True) or True)
print((False and False) or False)
print((True or True) and False)
print((True or False) and True)
print((False or True) and True)
print((False or False) and False)


try:
  stock = int(input("Ingrese el stock que desea ingresar: "))
  print(stock >= 100 and stock <= 1000)
  # Lo contrario de la lógica anterior
  print(not (stock >= 100 and stock <= 1000))
except ValueError:
  print("El valor ingresado no es un número entero")

try:
  role = input("Digite su rol: ")
  if (not role.isalpha()):
    raise ValueError("El rol no puede contener números, signos o espacios")
  print(role == "admin" or role == "seller")
except ValueError as error:
  print("Error:", error)