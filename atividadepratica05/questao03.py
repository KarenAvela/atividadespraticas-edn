def calcular_desconto(valor_produto, percentual_desconto):
    desconto = (percentual_desconto / 100) * valor_produto
    return desconto

valor_produto = float(input("Digite o valor do produto: R$ "))
percentual_desconto = float(input("Digite o percentual do desconto (%): "))
desconto = calcular_desconto(valor_produto, percentual_desconto)
print(f"O valor do desconto é: R$ {desconto:.2f}")    
print(f"O valor final do produto com desconto é: R$ {valor_produto - desconto:.2f}")
