t = 1367 # Total de cuadras de la vuelta
k = 486 # Cuadras en subida
n = 85872 # Cantidad de cuadras que recorre Ivo
cuadrasSubida = 0

vueltas = n // t
resto = n % t
planas = t - k

subidas = vueltas * k

if resto > planas:
    subidas += resto - planas

print(subidas)