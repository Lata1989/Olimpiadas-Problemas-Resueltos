c = 248 # Cantidad de carbohidratos en gramos
p = 196 # Cantidad de proteinas en gramos
g = 64 # Cantidad de grasas totales en gramos

banana = [27, 105] # aporte de gramos de carbohidratos y calorias de una banana
atun = [30, 120] # aporte de gramos de proteinas y calorias de una lata de atun
aceite = [1, 9] # aporte de gramos de grasa y calorias del aceite de oliva

cantBananas = 0
cantAtun = 0
cantAceite = 0

totalCalorias = 0

# while c > 0:
#     totalCalorias = totalCalorias + banana[1]
#     c = c - banana[0]
#     cantBananas = cantBananas + 1

# while p > 0:
#     totalCalorias = totalCalorias + atun[1]
#     p = p - atun[0]
#     cantAtun = cantAtun + 1

# while g > 0:
#     totalCalorias = totalCalorias + aceite[1]
#     g = g - aceite[0]
#     cantAceite = cantAceite + 1

if c % banana[0] == 0:
    cantBananas = c // banana[0]
else:
    cantBananas = c // banana[0] + 1

if p % atun[0] == 0:
    cantAtun = p // atun[0]
else:
    cantAtun = p // atun[0] + 1

if g % aceite[0] == 0:
    cantAceite = g // aceite[0]
else:
    cantAceite = g // aceite[0] + 1

totalCalorias = (cantBananas * banana[1]) + (cantAtun * atun[1]) + (cantAceite * aceite[1])

print("Cantidad de bananas: ", cantBananas)
print("Cantidad de latas de atun: ", cantAtun)
print("Cantidad de cucharadas de aceite: ", cantAceite)
print("Cantidad total de calorias: ", totalCalorias)