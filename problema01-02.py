n = 20 # Cantidad de estaciones de alquiler
b = 20 # Cantidad de espacios para bicicletas en cada estación
c = [15, 4, 18, 2, 10, 12, 8, 14, 6, 11, 9, 16, 3, 17, 5, 13, 7, 10, 12, 8] # Cantidad de bicicletas en cada estación en el momento
t = b / 2 # Cantidad de bicicletas que deben haber en cada estación para que esté equilibrada

cantBicisAMover = 0

for i in range(n):
    if c[i] > t:
        cantBicisAMover = cantBicisAMover + (c[i] - t)

print("Cantidad de bicicletas que deben moverse: ", cantBicisAMover)