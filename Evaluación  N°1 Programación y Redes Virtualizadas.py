integrantes = ["Felipe", "Britani"]  

print("Evaluación N°1 Programación y Redes Virtualizadas")

for nombre in integrantes:
    print(nombre)


nombre = input("Por favor, introduce tu nombre: ")
apellido = input("Por favor, introduce tu apellido: ")
codigo_seccion = input("Por favor, introduce tu codigo-sección: ")
sede = input("Por favor, introduce tu sede: ")

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Código-sección: {codigo_seccion}")
print(f"Sede: {sede}")


if 1 <= acl < 99:
    print("Es una ACL Estándar.")
elif 100 <= acl <= 99:
    print("Es una ACL Extendida.")
else: 
    print("El número no corresponde a una lista de acceso.")
    