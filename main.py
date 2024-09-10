import random

print("🤖 Bienvenido al juego de piedra, papel o tijera \n")

options = ["piedra", "papel", "tijera"]
user_count = 0
computer_count = 0

while user_count < 2 and computer_count < 2:
  try:
    
    user_option = input("👉 Elige una opción (piedra, papel o tijera): ").lower()
  
    if user_option not in options:
      raise ValueError("❌ Opción no válida \n")
    
    computer_option = random.choice(options)
    
    print("🤖 Computer option:", computer_option, "\n")
    # 
    if (user_option == computer_option):
      print("😒 Empate!")
    elif user_option == "piedra":
      if computer_option == "tijera":
        print("piedra gana a tijera")
        print("👨 user gano!")
        user_count += 1
      else:
        print("Papel gana a piedra")
        print("🤖 computer gano!")
        computer_count += 1
    elif user_option == "papel":
      if computer_option == "piedra":
        print("papel gana a piedra")
        print("👨 user gano!")
        user_count += 1
      else:
        print("tijera gana a papel")
        print("🤖 computer gano!")
        computer_count += 1
    elif user_option == "tijera":
      if computer_option == "papel":
        print("tijera gana a papel")
        print("👨 user gano!")
        user_count += 1
      else:
        print("piedra gana a tijera")
        print("🤖 computer gano!")
        computer_count += 1

    print("\n **** MARCADOR ****")
    if (user_count > computer_count):
      print("User:", user_count, "Computer:", computer_count, "\n")
      if (user_count == 2):
        print("👨 Usuario ganó el juego!")
    else:
      print("Computer:", computer_count, "User:", user_count, "\n")
      if (computer_count == 2):
        print("🤖 Computer ganó el juego!")
  except ValueError as error:
    print(error)