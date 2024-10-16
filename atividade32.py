# # Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

import math

def calcular_area_base(raio):
    return math.pi * raio ** 2

def calcular_volume_cilindro(raio, altura):
    area_base = calcular_area_base(raio)
    return area_base * altura

raio = float(input("Digite o raio do círculo: "))
altura = float(input("Digite a altura do cilindro: "))

print(f"A área da base do círculo é: {calcular_area_base(raio):.2f}")
print(f"O volume do cilindro é: {calcular_volume_cilindro(raio, altura):.2f}")
