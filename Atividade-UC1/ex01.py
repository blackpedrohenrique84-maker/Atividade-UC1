print("LANCHONETE")
print("1. Hamburguer - R$ 16")
print("2. Pizza - R$ 25")
print("3. Refrigerante - R$ 6")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor = 16
elif opcao == 2:
    valor = 25
elif opcao == 3:
    valor = 6   
else:
    valor = 0

print("Valor: R$", valor)
    