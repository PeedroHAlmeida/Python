from math import sqrt

print("\n=== EXERCÍCIO 1 ===")
numero = int(input("Digite um número inteiro: "))
if(numero % 2 == 0):
    print("O número", numero, "é par!")
else:
    print("O número", numero, "é impar!")

print("\n=== EXERCÍCIO 2 ===")
velo = float(input("Digite a velocidade do carro em Km/h: "))
if(velo > 80):
    multa = (velo - 80)*5
    print(f"O carro foi multado em R${multa:.2f}")
else:
    print("O carro não foi multado")

print("\n=== EXERCÍCIO 3 ===")
largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))
area = largura * altura
if(area <= 100):
    print(f"O terreno possui {area:.0f}m² e é classificado como TERRENO POPULAR")
elif(area <= 500):
    print(f"O terreno possui {area:.0f}m² e é classificado como TERRENO MASTER")
else:
    print(f"O terreno possui {area:.0f}m² e é classificado como TERRENO VIP")

print("\n=== EXERCÍCIO 4 ===")
val_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salario: "))
anos = float(input("Digite em quantos anos pagará a casa?: "))
if(val_casa/(anos*12) > salario*0.3):
    print(f"Emprestimo negado!\nO valor da prestação mensal ultrapassa 30% do salario atual")
else:
    print("Emprestimo aprovado!")

print("\n=== EXERCÍCIO 5 ===")
preco = float(input("Digite o preço do produto: "))
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo(m/f): ")
while(sexo != "m" and sexo != "f"):
    sexo = input("Erro! Digite um sexo valido(m/f): ")
if(sexo == "m"):
    desconto = 5
    total = preco * 0.95
else:
    desconto = 13
    total = preco * 0.87
print(f"{nome}, com o desconto de {desconto}% o total a se pagar é de R${total:.2f}")

print("\n=== EXERCÍCIO 6 ===")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b*b-4*a*c
if(delta <= 0):
    print("Não existem raizes reais paras esses valores!")
else: 
    raiz1 = (-b + sqrt(delta)/2*a)
    raiz2 = (-b - sqrt(delta)/2*a)
    print(f"Raiz 1 = {raiz1:.2f}\nRaiz 2 = {raiz2:.2f}")

print("\n=== EXERCÍCIO 7 ===")
horas = int(input("Digite quantas horas de atividade fisica foram feitas no mes: "))
if(horas < 10):
    pontos = 2 * horas
    valor = pontos * 0.05
elif(horas < 20):
    pontos = 5 * horas
    valor = pontos * 0.05
else:
    pontos = 10 * horas
    valor = pontos * 0.05
print(f"Com {pontos} pontos, você ganhou R${valor:.2f} em {horas} horas de atividade fisica no mês!")

print("\n=== EXERCÍCIO 8 ===")
print(f"1 - À vista em dinheiro ou cheque, recebe 10% de desconto")
print(f"2 - À vista no cartão de crédito, recebe 5% de desconto")
print(f"3 - Em duas vezes, preço normal de etiqueta sem juros")
print(f"4 - Em três vezes, preço normal de etiqueta mais juros de 10%")
codigo = int(input("Digite o codigo da forma de pagamento: "))
preco = float(input("Digite o preço do produto: "))
match codigo:
    case 1:
        total = preco * 0.9
        print(f"Com 10% de desconto o preço tatal fica em R${total:.2f}")
    case 2:
        total = preco * 0.95
        print(f"Com 5% de desconto o preço tatal fica em R${total:.2f}")
    case 3:
        total = preco/2
        print(f"Com duas parcelas sem juros o preço tatal fica em R${total:.2f} em dois meses")
    case 4:
        total = (preco * 1.1)/3
        print(f"Com tres parcelas com juros de 10% o preço tatal fica em R${total:.2f} em tres meses")

        

