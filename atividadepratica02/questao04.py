distancia = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite o combustível gasto em litros: "))

consumo_medio = distancia / combustivel_gasto


print(f"Distância percorrida : {distancia:.2f} KM")
print(f"Combustível gasto: : {combustivel_gasto:.2f} L")
print(f"Média de consumo de combustível é : {consumo_medio:.2f} km/l")
