def calcular_gorgeta(valor_conta, percentual_gorgeta):
    gorjeta = (percentual_gorgeta / 100) * valor_conta
    return gorjeta

valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_gorgeta = float(input("Digite o percentual da gorjeta (%): "))
gorjeta = calcular_gorgeta(valor_conta, percentual_gorgeta)
print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")    