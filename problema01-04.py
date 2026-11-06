arreglo = []
temp = []
e = 72 # cantidad de ciclos
totalCelulas =  0 # El numero que necesito

for i in range(0,300):
    if (i * 7 + 3) % 5 == 0:
        arreglo.append(1)
    else:
        arreglo.append(0)

for i in range(0,len(arreglo),1):
    temp.append(arreglo[i])

for i in range(0,e,1): # ejecutamos la cantidad de ciclos
    for j in range(0,len(arreglo),1):
        cantVecinos = 0 # Lo vuelvo a 0 para tener en cuenta el 

        # Aprovecho no se si es bug de python donde el indice -1 apunta al ultimo, lo podria hacer a len(arreglo)-1 pero bueno no voy a renegar
        if j == 0:
            cantVecinos = cantVecinos + arreglo[j-1] # Para pegarle al ultimo elemento que es el anterior al primero digamos
            cantVecinos = cantVecinos + arreglo[j] # El elemento que estoy verificando
            cantVecinos = cantVecinos + arreglo[j+1] # El siguiente elemento
        elif j < len(arreglo)-1:
            cantVecinos = cantVecinos + arreglo[j-1] # El elemento anterior
            cantVecinos = cantVecinos + arreglo[j] # El elemento que estoy verificando
            cantVecinos = cantVecinos + arreglo[j+1] # El siguiente elemento
        elif j == len(arreglo)-1:
            cantVecinos = cantVecinos + arreglo[j-1] # El elemento anterior
            cantVecinos = cantVecinos + arreglo[j] # El elemento que estoy verificando
            cantVecinos = cantVecinos + arreglo[0] # Para pegarle al primer elemento que es el siguiente al ultimo digamos

        # Hasta aca calculo vecinos, ahora asigno en el temporal lo que me queda en esa posicion
        if cantVecinos % 2 == 0:
            temp[j] = 1
        else:
            temp[j] = 0

    # Ahora copio el temporal al original para el siguiente ciclo
    for j in range(0,len(arreglo),1):
        arreglo[j] = temp[j]

for i in range(0,len(arreglo),1):
    totalCelulas = totalCelulas + arreglo[i] # Porque la celula viva vale 1

print("Cantidad de celulas vivas: ", totalCelulas)