#sal

nome = input('Nome do funcionário:')
sal = float(input('Salário:'))
ano = float(input('Quantos anos de empresa:'))
if ano == 3:
    reajSal = sal + (sal * 3/100)
elif ano > 3 and ano < 10:
    reajSal = sal + (sal * 12.5/100)
elif ano >= 10:
    reajSal = sal + (sal * 20/100)
else:
    print('Reajuste invalido')
    sal = 0
print(f'O novo salário do funcionário {nome} é: R$ {reajSal}')

        
