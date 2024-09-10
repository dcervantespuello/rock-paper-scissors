# Comparación de flotantes
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Comparando flotantes como strings
y_str = format(y, ".3g")
print("str =>", y_str)
print(y_str == str(x))

# Comparando flotantes de forma matemática
print("*" * 10)
print(y, x)

tolerancia = 0.00001
print(x - y)
print(abs(x - y))
print(abs(x - y) < tolerancia)

print("*" * 10)
print(x == round(y, 1))