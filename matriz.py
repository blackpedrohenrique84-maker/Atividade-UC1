'''matriz = []


for in range(3):
    linha = []


    for j in range(3):
        nota = float(input('digite a nota'))
        linha.append(nota)

        matriz.append(linha)

    for i in matriz:
            print(i)

    for i in matriz:
         print(f'media do {i + 1} aluno:', sum(matriz[i] / len(matriz[i])))        

        










assentos = [
    [0, 1,0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]

    
    ]

disp = 0
indisp = 0 

for i in assentos:
    num = int(input)
    for j in i:
        if j == 1:
            disp += 1
        else:
            indisp += 1










print('disponiveis'. disp)
print('Indisponiveis', indisp)     '''   



notas = []

for i in range(5):
    print(f'\n  {i+1:}')
    alunos_notas = []
    for j in range (3):
        nota = float(input(f'Notas {j+1}'))

        nota.append(alunos_notas)
        alunos_notas.append(nota)


aprovados = 0
recuparaçao = 0
reprovados = 0

todas_notas = []
media = []
situacoes = []

for alunos_notas in nota:
    media = sum(alunos_notas)/3
    media.append(notas)


todas_notas.extend(alunos_notas)   

if media > 7:
    aprovados +=1
elif media >= 5:
    recuparaçao +=1
else:
   recuparaçao +=1


   situacoes.append(situacoes)


   print('\n issai carai')
for i in range(5):
    print(f'aluno {i+1} - media: {media[i]:.1f} - {situacoes[i]}')



print(f'\nAprovado', aprovados)    