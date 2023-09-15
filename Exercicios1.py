
import math

print("\n=== DESAFIO 1 ===")
nome = input("Qual o seu nome?: ")
print(f"Olá {nome}! Prazer te conhecer!")

print("\n=== DESAFIO 2 ===")
dia = input("Dia = ")
mes = input("Mes = ")
ano = input("Ano = ")
print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")

print("\n=== DESAFIO 3 ===")
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
soma = numero1 + numero2
if(soma % 1 == 0):          #se a soma não tiver casas decimas o valor de saída também não terá
    print("O valor da soma é: %.0f" % soma)
else:                       #se a soma tiver casas decimais o valor de saída terá duas casas decimais
    print("O valor da soma é: %.2f" % soma)

print("\n=== DESAFIO 4 ===")
numero = int(input("Digite um numero inteiro: "))
ant = numero - 1
suc = numero + 1 
print(f"antecessor:", ant, "e sucessor:", suc)

print("\n=== DESAFIO 5 ===")
real = float(input("Digite um número real: "))
mult = real * 2
div = real/3
print("Número multiplicado por 2 = %.2f" % mult, "e sua terça parte = %.2f" % div)

print("\n=== DESAFIO 6 ===")
dist = float(input("Digite uma distância em metros: "))
print(f"A distância de {dist:.2f}m corresponde a: ")
print(f"{dist/1000:.3f}Km")
print(f"{dist/100:.2f}Hm")
print(f"{dist/10:.2f}Dam")
print(f"{dist*10:.2f}dm")
print(f"{dist*100:.2f}cm")
print(f"{dist*1000:.2f}mm")

print("\n=== DESAFIO 7 ===")
valor_reais = float(input("Digite quanto você tem na carteira: "))
valor_dolar = valor_reais / 5.24
print(f"No total você tem ${valor_dolar:.2f} convertidos")

print("\n=== DESAFIO 8 ===")
largura = float(input("Digite o valor da largura da parede: "))
altura = float(input("Digite o valor da altura da parede: "))
print("Obs: cada litro de tinta pinta uma área de 3 m²")
area = largura * altura
latas = math.ceil(area / 3)
print(f"Serão necessasrias {latas} latas de tinta para pintar toda parede")

print("\n=== DESAFIO 9 ===")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b*b-4*a*c
print("Valor de delta =", delta)

print("\n=== DESAFIO 10 ===")
produto = float(input("Digite o valor do produto: "))
promocao = produto * 0.85
print(f"Valor do produto com 15% de desconto: {promocao}")

print("\n=== DESAFIO 11 ===")
salario_atual = float(input("Digite seu salário atual: "))
novo_salario = salario_atual + (salario_atual * 0.1)
print(f"Seu novo salário é R${novo_salario:.2f}")

print("\n=== DESAFIO 12 ===")
percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade dias alugados: "))
total = percorridos*0.8 + dias*50
print(f"O total a apagar é R${total:.2f}")

print("\n=== DESAFIO 13 ===")
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês: "))
salario = 8 * 36 * dias_trabalhados
print(f"Seu salário no mês é de R${salario:.2f}")