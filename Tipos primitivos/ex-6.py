
import math
cateto1 = float(input("Digite um número do cateto "))
cateto2 = float(input("Digite outro número do cateto: "))


hipotenusa = math.hypot(cateto1, cateto2)
print(f"O número da hipotenusa de é {hipotenusa:.2f}")