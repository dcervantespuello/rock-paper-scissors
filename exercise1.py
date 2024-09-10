from statistics import mean

# Título de la app
print("Bienvenido al app de cálculo de presupuesto")

# Preguntar al usuario por el presupuesto de cada mes
budget_january = int(input("Presupuesto de enero: "))
budget_february = int(input("Presupuesto de febrero: "))
budget_march = int(input("Presupuesto de marzo: "))

# Calcular el promedio del presupuesto
final_budget = mean([budget_january, budget_february, budget_march])

# Mostrando en pantalla el resultado
print(f"El presupuesto promedio es: {final_budget}")