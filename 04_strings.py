name = "Deivis"
last_name = "Cervantes"

# Concatenación
full_name = name + " " + last_name
print(full_name)
print(name, last_name)

# Formateo de strings
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

edad = 28
template = f"Hola, soy {name} {last_name} y tengo {edad} años"
print(template)