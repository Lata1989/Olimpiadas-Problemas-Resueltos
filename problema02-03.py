# Declaro las dos porque me pinta y lo puedo hacer para que sea mas flexible y lo pueda reutilizar en el otro =D
n = 50
m = 50
e = 36 # Cantidad de ciclos
cantCelulasVivas = 0 # El numero que necesito
matriz = []
temp = []

for i in range(0, n, 1):
    fila = []
    for j in range(0, m, 1):
        if (i * 5 + j * 3 + 2) % 7 == 0:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
    temp.append(fila.copy()) # Esta se la vamos a tener que dar cuando esten en el problema porque no lo dimos me di cuenta ahora 



for ciclo in range(0, e, 1): # Recorro los ciclos

    # Recorro la matriz para contar los vecinos
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            vecinos_activos = 0
            
            # Armo los indices para que la matriz funcione de forma toroidal
            if i == 0: # Primera fila
                fila_arriba = n - 1
                fila_abajo = i + 1
            elif i == n - 1: # Ultima fila
                fila_arriba = i - 1
                fila_abajo = 0
            else: # Resto de filas
                fila_arriba = i - 1
                fila_abajo = i + 1

            # Lo mismo de antes pero para las columnas
            if j == 0: # Primera columna
                col_izq = m - 1
                col_der = j + 1
            elif j == m - 1: # Ultima columna
                col_izq = j - 1
                col_der = 0
            else: # Resto de columnas
                col_izq = j - 1
                col_der = j + 1

            # Sumo los vecinos de arriba primero
            vecinos_activos += temp[fila_arriba][col_izq]
            vecinos_activos += temp[fila_arriba][j]
            vecinos_activos += temp[fila_arriba][col_der]

            # Sumo los vecinos de la misma fila (la celda en si no cuenta)
            vecinos_activos += temp[i][col_izq]
            vecinos_activos += temp[i][col_der]

            # Ahora la fila de abajo
            vecinos_activos += temp[fila_abajo][col_izq]
            vecinos_activos += temp[fila_abajo][j]
            vecinos_activos += temp[fila_abajo][col_der]

            # Ahora veo que tengo que guardar en la matriz
            if vecinos_activos % 2 == 0:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0

    # Copio la matriz original a la temporal para el proximo ciclo
    for i in range(n):
        for j in range(m):
            temp[i][j] = matriz[i][j]


# Ahora cuento la cantidad de celulas vivas
for i in range(n):
    for j in range(m):
        if matriz[i][j] == 1:
            cantCelulasVivas += 1

print("Cantidad de celulas vivas: ", cantCelulasVivas)