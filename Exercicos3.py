print("\n=== EXERCÍCIO 1 ===")
n = int(input("Digite um numero: "))
for i in range(0, n+1, 3):
    print(f"{i},", end = " ")
print("acabou!")

print("\n=== EXERCÍCIO 2 ===")
num = int(input("Digite um numero interio positivo: "))
for i in range(1, num+1):
    print(f"{i},", end = " ")
print("acabou!")

print("\n=== EXERCÍCIO 3 ===")
for i in range(30, 1, -1):
    if(i % 4 == 0):
        print(f"[{i}],", end = " ")
    else:
        print(f"{i},", end = " ")
print("1.")

print("\n=== EXERCÍCIO 4 ===")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
incremento = int(input("Digite valor do incremento: "))
if(n1 > n2):
    incremento = -incremento
for i in range(n1, n2, incremento):
    print(f"{i},", end = " ")
print("Acabou!")

print("\n=== EXERCÍCIO 5 ===")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
while(num2 == 0):
    num2 = float(input("VALOR INVALIDO! O valor deve ser diferente de 0\nDigite novamente: "))
div = num1 / num2
if(num1 % 1 == 0 and num2 % 1 == 0 and div % 1 == 0):
    print(f"O resultado da divisão de {num1:.0f} por {num2:.0f} é {div:.0f}")
else: 
    print(f"O resultado da divisão de {num1:.2f} por {num2:.2f} é {div:.2f}")

print("\n=== EXERCÍCIO 6 ===")
par = 0
impar = 0
for i in range(6):
    numero = int(input(f"Digite o {i+1}° numero: "))
    if(numero % 2 == 0):
        par += 1
    else: 
        impar += 1
print("Quantidade de numeros pares = ", par)
print("Quantidade de numeros impares = ", impar)

print("\n=== EXERCÍCIO 7 ===")
homem = 0
mulher = 0
mulher20 = 0
mid = 0
mid_homem = 0
for i in range(5):
    sexo = input("\nDigite seu sexo(m/f): ")
    while(sexo != "m" and sexo != "f"):
        sexo = input("Erro! Digite 'm' ou 'f' para sexo: ")
    idade = int(input("Digite sua idade: "))
    mid = mid + idade
    if(sexo == "f"):
        mulher += 1
        if(idade > 20):
            mulher20 += 1
    else:
        homem += 1
        mid_homem = mid_homem + idade
print("\nHomens cadastrados = ", homem)
print("Mulheres cadastradas = ", mulher)
print(f"Média de idade do grupo = {(mid/5):.2f}")
print(f"Média de idade dos homens = {(mid_homem/homem):.2f}")
print(f"Mulheres com mais de 20 anos =  {mulher20}\n")