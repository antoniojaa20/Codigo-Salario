valorHora = float(input('Digite o seu valor hora '))
quantidadeHora = float(input('Digite a  sua quantidade de horas '))
salarioBruto = valorHora * quantidadeHora
print('Seu salário bruto é ',salarioBruto)

#descontos
inss = 8 * (salarioBruto / 100)
if salarioBruto < 2000:
    ir = 10 * (salarioBruto / 100)
elif salarioBruto >= 2000 and salarioBruto < 4000:
    ir = 15 * (salarioBruto / 100)
elif salarioBruto >= 4000 and salarioBruto < 6000:
    ir = 20 * (salarioBruto / 100)
else:
    ir = 25 * (salarioBruto / 100)
sind = 5 * (salarioBruto / 100)
descontos = inss + ir + sind
print('valor do inss é' ,inss)
print('valor do imposto de renda é' ,ir)
print('valor do sindicato é' ,sind)

#Liquido
salarioLiquido = salarioBruto - descontos
print('Seu salário liquido é ',salarioLiquido)