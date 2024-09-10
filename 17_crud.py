# CRUD: Create, Read, Update & Delete
docs = ["123", "768", "932", "456"]

# Consultando un elemento de la lista
print(docs[1])

# Actualizando un elemento de la lista
docs[2] = "999"
print(docs)

# Insertando nuevos elementos en la lista
docs.append("999")
print(docs)
docs.insert(2, "821")
print(docs)

# Elminar elementos de la lista
docs.remove("999")
print(docs)
docs.pop();
print(docs)

# Haciendo slicing
docs = docs[:2]
print(docs)

# Concatenando listas
pets = ["dog", "cat", "donkey", "bird", "fish", "HAMSTER"]

new_list = docs + pets
print(new_list)

# Buscando la posición de un elemento en la lista
print(new_list.index("donkey"))
print(new_list[4])

# Ordenando una lista
new_list.sort()
print(new_list)

# Reversando la lista
new_list.reverse()
print(new_list)