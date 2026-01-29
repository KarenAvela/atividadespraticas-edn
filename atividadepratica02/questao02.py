nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite valor unitário do produto: "))
desconto = 20

valor_desconto = valor * (desconto / 100)
valor_final = valor - valor_desconto

print(f"Produto : {nome_produto}")
print(f"Valor unitário do produto é: {valor:.2f}")
print(f"Valor de desconto é : {valor_desconto:.2f}")
print(f"Valor final do produto {nome_produto} é R$ {valor_final:.2f}")