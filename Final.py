import csv


def novoDado(ponto, conc):          # Esta funcao sera usado para a escolha 1 e 2 do programa
    novo = []
    novo.append(ponto)
    novo.append(conc)
    return novo                     # Retorna uma matriz que sera adicionada a matriz principal 

def printar(matriz):                # Esta funcao sera usada para a escolha 6, para nao aparecer em formato de matriz printamos uma de cada vez
    tam = len(matriz)
    contador=0
    while contador<tam:
        print(matriz[contador][0], end='  ')
        print(matriz[contador][1])
        contador+=1

def media(matriz,ponto):            # Esta funcao sera usada na escolha 3, onde ira receber a matriz e calcular a media de cada ponto e printar o resultado
    divisor = 0
    soma = 0
    i = 0
    while i < len(matriz):
        if i != 0 and int(matriz[i][0]) == ponto:   # Tivemos que adicionar o int() e float(), porque quando estavamos trazendo dados de um arquivo csv (Funcao 5), ele salva na matriz como string.
            soma += float(matriz[i][1])
            divisor += 1
        i += 1
    if divisor != 0:
        media = soma / divisor              
        print(f"A média do ponto {ponto}: {media:.2f}")         #A dicionamos o .2f para printar apenas 2 casas depois da virgula a media
    else:
        print(f"Não foi encontrado nenhum valor para o ponto {ponto}.")

def maior(matriz):          # Esta funcao sera usada na escolha 3, onde ira receber a matriz e ira descobrir qual a maior concetracao e salva-la, tambem salva o ponto para printar
    tam = len(matriz) - 1
    maiorconc = 0
    maiorponto = 0
    i = 1
    if tam == 0:
        print("Nao possui nenhum Dado!")
    else: 
        while i <= tam:
            conc = float(matriz[i][1])      # Novamente tivemos que transformar os itens da matriz em int e float
            if conc > maiorconc:
                maiorconc = conc
                maiorponto = int(matriz[i][0])
            i += 1
        print(f"O ponto com a maior concentração é: {maiorponto}, com a concentração de: {maiorconc}")
            


Titulo = ['Ponto', 'concentracao']      # Com intuito de nao criar uma funcao apenas para adicionar o titulo, adicionamos antes do loop principal
matriz= []
matriz.append(Titulo)
escolha = ''

while escolha.lower() != 'fim':         # Adicionamos o .lower() para nao precisar adicionar "or" para cada situacao possivel
    escolha = input("1 - Novo registro\n2 - N novos registros\n3 - Calcular propriedades\n4 - Gravar em arquivo\n5 - Carregar de arquivo\n6 - Visualizar registros\nDigite uma opção ou FIM para sair: ")

    if escolha == '1':
        ponto = int(input("Informe o número do ponto: "))
        conc = int(input("Informe a concentração de E. coli: "))
        if (ponto in [7, 38, 39, 62]) and  conc >= 0:   # Checa se os dados fornecidos sao validos
            novo = novoDado(ponto, conc)
            matriz.append(novo)                         # Adiciona o ponto e concentracao na matriz
        else:
            print('Ponto ou concentracao invalida')

    if escolha == '2':
        while escolha.lower() != 'ok':     # Este while possibilita que adicionemos n dados novos utilizando a mesma funcao da 1 opcao
            ponto = int(input("Informe o número do ponto: "))
            conc = float(input("Informe a concentração de E. coli: "))
            if (ponto in [7, 38, 39, 62]) and  conc >= 0: 
                novo = novoDado(ponto, conc)
                matriz.append(novo)
            else:
                print('Ponto ou concentracao invalida')
            escolha = input("Pressione qualquer tecla para inserir mais um registro ou OK para retornar: ")

    if escolha == '6':
        printar(matriz)

    if escolha =='3':
        pontos = [7, 38, 39, 62]        # Para nao chamar indivudualmente a funcao para cada ponto, utilizamos este for para chamar todas
        for ponto in pontos:
            media(matriz, ponto)
        maior(matriz)

    if escolha =='4':
        nome = input('Insira o nome do arquivo que deseja criar: ') + '.csv'
        with open(nome, 'w', newline='') as arquivo_csv:        # Abre o arquivo csv para escrita ('w')
            escritor = csv.writer(arquivo_csv)                  # Cria um 'escritor' que consegue escrever em um arquivo csv
            for linha in matriz:
                escritor.writerow(linha)                        # Esreve linha por linha no arquivo csv
        matriz=[]                                               # Aqui esvaziamos a matriz, pois como ja foi exportada para um arquivo, podemos utilizar a func 5 para pegar de volta os dados
        matriz.append(Titulo)
    
    if escolha =='5':
        nome = input('Insira o nome do arquivo que deseja adicionar a atual matriz: ') + '.csv'
        with open(nome, 'r') as arquivo_csv:                    # Abre o arquivo csv para leitura ('r')
            leitor = csv.reader(arquivo_csv)                    # Cria um 'leitor' que consegue trazer dados de um arquivo csv
            contador=0
            for linha in leitor:
                if contador !=0:                                # Este contador serve para nao trazer o titulo das colunas, porque ele ja foi colocado no comeco do codigo
                    matriz.append(linha)                        # Adiciona linha por linha os dados do csv na matriz do programa
                contador+=1