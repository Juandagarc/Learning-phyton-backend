# Presentado por Juan David García arce

import random

numero_radom = random.randint(1, 100)
print(numero_radom)
i = 0

# se hace el random hasta que sea igual a 100 con while

while numero_radom != 100:
    i = i + 1
    numero_radom = random.randint(1, 100)

print("Se ha demorado", i, "intentos en llegar a 100")