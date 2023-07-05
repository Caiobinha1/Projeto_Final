import csv


def novoDado(ponto, conc):
    novo = []
    novo.append(ponto)
    novo.append(conc)
    return novo

def printar(matriz):
    tam = len(matriz)
    contador=0
    while contador<tam:
        print(matriz[contador][0], end='  ')
        print(matriz[contador][1])
        contador+=1
def media(matriz,ponto):
    divisor=0
    soma = 0
    for linha in matriz:
        if linha[0] == ponto:
            soma += linha[1]
            divisor += 1
    if divisor !=0:
        media = soma/divisor
        print(f"A media do ponto {ponto}: {media}")

def maior(matriz):
    tam = len(matriz)-1
    maiorconc = 0
    while tam>0:
        if matriz[tam][1]>maiorconc:
            maiorconc = matriz[tam][1]
            maiorponto = matriz[tam][0]
        tam-=1
    print(f'O ponto com a maior concentracao e: {maiorponto}, com a concentracao de: {maiorconc}')
        





Titulo = ['Ponto', 'concentracao']
matriz= []
matriz.append(Titulo)
escolha = ''

while escolha.lower() != 'fim':
    escolha = input("1 - Novo registro\n2 - N novos registros\n3 - Calcular propriedades\n4 - Gravar em arquivo\n5 - Carregar de arquivo\n6 - Visualizar registros\nDigite uma opção ou FIM para sair: ")

    if escolha == '1':
        ponto = int(input("Insira o ponto: "))
        conc = int(input("Insira a concentracao: "))
        if (ponto in [7, 38, 39, 62]) and  conc >= 0: 
            novo = novoDado(ponto, conc)
            matriz.append(novo)
        else:
            print('Ponto ou concentracao invalida')

    if escolha == '2':
        while escolha != 'fim':
            ponto = int(input("Insira o ponto: "))
            conc = int(input("Insira a concentracao: "))
            if (ponto in [7, 38, 39, 62]) and  conc >= 0: 
                novo = novoDado(ponto, conc)
                matriz.append(novo)
            else:
                print('Ponto ou concentracao invalida')
            escolha = input("Digite 'fim' se deseja parar de insiri novos dados: ")
        escolha=''

    if escolha == '6':
        printar(matriz)

    if escolha =='3':
        #print(matriz)
        media(matriz, 7)
        media(matriz, 37)
        media(matriz, 38)
        media(matriz, 39)
        media(matriz, 62)
        #maior(matriz)

    if escolha =='4':
        nome = input('Insira o nome do arquivo que deseja criar: ') + '.csv'
        with open(nome, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            for linha in matriz:
                escritor.writerow(linha)
        matriz=[]
    
    if escolha =='5':
        nome = input('Insira o nome do arquivo que deseja adicionar a atual matriz: ') + '.csv'
        with open(nome, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            contador=0
            for linha in leitor:
                if contador !=0:
                    matriz.append(linha)
                contador+=1