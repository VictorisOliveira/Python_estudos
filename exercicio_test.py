def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

import random

lista = random.sample(range(1000), 50)
print(sorted(lista))
executar_busca_linear(lista, 10)
# [52, 73, 95, 98, 99, 103, 123, 152, 158, 173, 259, 269, 294, 313, 318, 344, 346, 348, 363, 387, 407, 410, 414, 433, 470, 497, 520, 530, 536, 558, 573, 588, 620, 645, 677, 712, 713, 716, 720, 727, 728, 771, 790, 801, 865, 898, 941, 967, 970, 979]
