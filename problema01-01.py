t = 1367 # Total de cuadras de la vuelta
k = 486 # Cuadras en subida
n = 85872 # Cantidad de cuadras que recorre Ivo
cuadrasSubida = 0

cantVueltas = n / t
print("Cantidad de vueltas que da Ivo: ", cantVueltas)

cuadrasSubida = cantVueltas * k
print("Cantidad de cuadras en subida: ", cuadrasSubida)

if cuadrasSubida > int(cuadrasSubida):
    cuadrasSubida = int(cuadrasSubida) + 1

print("Cantidad de cuadras en subida (redondeado): ", cuadrasSubida)