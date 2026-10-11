# Sistema de calificaciones con vectores
NOTA_MINIMA = 70

calificaciones = [85, 67, 92, 74, 58]

print("=== SISTEMA DE CALIFICACIONES ===")
print("Vector inicial:", calificaciones)

# 1. Mostrar todas las calificaciones (recorrido)
print("\nCalificaciones de los estudiantes:")
for i in range(len(calificaciones)):
    print(f"Estudiante {i + 1}: {calificaciones[i]}")

# 2. Acceso por índice
pos = int(input("\nPosición a consultar (0 a 4): "))
if 0 <= pos < len(calificaciones):
    print(f"La calificación en la posición {pos} es {calificaciones[pos]}")
else:
    print("Esa posición no existe.")

# 3. Cálculos: promedio, mayor y menor
promedio = sum(calificaciones) / len(calificaciones)
mayor = max(calificaciones)
menor = min(calificaciones)
print(f"\nPromedio: {promedio:.2f}")
print(f"Calificación más alta: {mayor}")
print(f"Calificación más baja: {menor}")

# 4. Contar aprobados y reprobados (ciclo + condición)
aprobados = 0
reprobados = 0
for nota in calificaciones:
    if nota >= NOTA_MINIMA:
        aprobados += 1
    else:
        reprobados += 1
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

# 5. Modificar una calificación
pos = int(input("\nPosición a modificar (0 a 4): "))
if 0 <= pos < len(calificaciones):
    nueva = int(input("Nueva calificación: "))
    calificaciones[pos] = nueva
    print("Calificación actualizada.")
else:
    print("Esa posición no existe.")

# 6. Mostrar el vector actualizado
print("\nVector actualizado:", calificaciones)
print(f"Nuevo promedio: {sum(calificaciones) / len(calificaciones):.2f}")