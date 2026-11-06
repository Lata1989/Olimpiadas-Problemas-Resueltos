# Variables iniciales
n = 10000 # Ultimo numero a analizar
perfectos = [] # Lista de numeros perfectos encontrados
result = 1 # Variable para almacenar el resultado final

for i in range(1, n + 1, 1):
    sumaDivisores = 0 # Inicio la suma de divisores en 0 para cada numero

    for j in range(1, (i // 2) + 1, 1): 
        if i % j == 0:
            sumaDivisores += j

    if sumaDivisores == i and i > 1:
        perfectos.append(i)

print("Números perfectos encontrados:", perfectos)

for i in range(len(perfectos)):
    result = result * perfectos[i]
    if i == len(perfectos) - 1:
        result = result - perfectos[i]/2

print("Resultado final:", int(result))