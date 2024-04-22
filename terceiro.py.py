#programadeprodutro

precodecusto = float(input("Digite o preço de custo da maça:"))
venda = float(input("Preço de venda da maça:"))
estoque = int(input("Quantidade de maça no estoque:"))
lucrouni = venda-precodecusto
lucroestint = venda*estoque
print("O lucro em uma unidade de maça é:", lucrouni)
print("O lucro no estoque todo de maça é:", round(lucroestint))
