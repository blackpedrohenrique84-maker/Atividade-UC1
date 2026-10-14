# matriz = [
#     [5 ,8, 2],
#     [7, 3,9],
#     [4, 6. 1] 
# ]

#     matriz= []
#     [10, 20]
#     [30 ,40]
# ]   
# matriz[0] [1]=99

# matriz = [
#     [10, 20 ,30],
#     [40, 50, 60]
#     ]
# for numero in matriz [0]:
#     print (numero)

#     for linha in matriz:
#         print(linha)
#         for linha in matriz:
#             for numero in linha:
#                 print(numero)

#         matriz = [
#         [10, 20,30,30],
#         [40,50,60]
#         ]
#         #o i e a linha
#         #o j e a coluna
#          for in range( len(matriz)):
#             for j range (len(matriz[i])):
#          print("linha:",i )
#         print("coluna:,j")
#         print("valor:, matriz [i[j]]")


        
matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        numero = int (input(" digite um numero:"))
        linha.append(numero)
    
    matriz.append(linha)
print(matriz)
for linha in matriz:
    print(linha)

    # encontrando numeros pares
    for linha in matriz:
        for numero in linha:
            if numero % 2 ==0:
                print(numero)
quantidade = 0               
for linha in matriz:
        for numero in linha:
           if numero % 2 == 0:
               quantidade += 1
print("quantidade de pares:",quantidade)
maior = matriz[0][0]:
for linha in matriz:
    if numero > maior:
     maior = numero 
     print("maior", maior)
     soma = 0
     for numero in matriz[0]:
     soma += numero
     print("a soma da primeira linha ,soma")
     soma = 0
     for i in range(len(matriz)):
         soma += matriz[i][0]



