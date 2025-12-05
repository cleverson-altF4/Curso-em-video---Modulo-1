#distância entre dois pontos
import math

x1 = float(input("Valor de X1 "))
y1 = float(input("valor de Y1 "))
x2 = float(input("Valor de X2 "))
y2 = float(input("Valor de Y2 "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"O valor de {x2 - x1}")
print(f"O valor de {y2 - y1}")