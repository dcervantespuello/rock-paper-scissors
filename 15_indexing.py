text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])

size = len(text)
print(text[size - 1])
print(text[-1])

# Slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1])
print(text[::1])
print(text[::2])

print(text[::-1])