import csv
import matplotlib.pyplot as plt

#Esta salvando como string nao float, na opcao 6 n deve imprimir como lista, mas como ????. Trocar o sistema colocar td vez o nome do arquivo para uma opcao que seleciona o arquivo que deseja ser mexido

def media(num, lista):
    with open(f'{lista}.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        numero2 = [row for row in reader if row['Ponto'] == str(num)]
    contagem_linha = len(numero2)
    soma_concentracao = sum(float(row['concentracao']) for row in numero2)
    media = soma_concentracao / contagem_linha
    print(f"Media do {num}: {media}")

def maior(nome):
    with open(f'{nome}.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        numMaior = max(reader, key=lambda row: float(row['concentracao']))
    print(f"O Ponto com maior Concentracao e:\n {numMaior}")

def juntar(lista, lista2):              #Funcao para concatenar dois arquivos csv
    with open(f'{lista}.csv', mode='r') as csvfile1:
        reader1 = csv.DictReader(csvfile1)          #Salva a primeira lista
        data1 = list(reader1)

    with open(f'{lista2}.csv', mode='r') as csvfile2:
        reader2 = csv.DictReader(csvfile2)          #salva a segunda lista
        data2 = list(reader2)

    combined_data = data1 + data2
    fieldnames = list(data1[0].keys())  # Assume que os dois arquivos possuem as mesmas colunas [ponto e concentracao]

    with open(f'{lista}.csv', mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #apaga a antiga lista e escreve a lista concatenada 
        writer.writeheader()
        writer.writerows(combined_data)

nome = input("Insira o nome do arquivo csv que deseja: ")  #Antes de poder entrar no loop, escolhemos qual arquivo queremos usar, casa quisermos trocar depois podemos utilizar a 4 opcao

while True:
    escolha1 = input("1 - Novo registro\n2 - N novos registros\n3 - Calcular propriedades\n4 - Gravar em arquivo\n5 - Carregar de arquivo\n6 - Visualizar registros\n7 - Criar Novo Arquivo csv\nDigite uma opção ou FIM para sair: ")
    if escolha1.lower() == 'fim':
        break                     #Aqui ele termina o loop, .lower() transforma as letras maiusculas em minusculas

    if escolha1 == '1' or escolha1 == '2':
        while True:                       #este outro loop serve para a segunda opcao, para o usuario conseguir colocar n numeros de registros
            NPonto = int(input('Informe o número do ponto: '))
            Conc = float(input('Informe a concentração de E. coli: '))
            if (NPonto in [37, 38, 39, 62]) and Conc >= 0:              #checa se Numero ponto e valido
                with open(f'{nome}.csv', mode='a', newline='') as csvfile:
                    writer = csv.writer(csvfile)        #aqui ele salva o arquivo aberto para editar
                    writer.writerow([NPonto, Conc])     #Adiciona a nova linha no arquivo
                    if escolha1 == '2':
                        x = input("Pressione qualquer tecla para inserir mais um registro ou OK para retornar: ")
                        if x.lower() == 'ok':
                            break
                    else:
                        break
            else:
                print("Numero ou concentracao invalida!")
                break

    elif escolha1 == '6':
        with open(f'{nome}.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)   #trasforma cada linha do arquivo em lista
            header = rows[0]
            data = rows[1:]
        
        print(', '.join(header))  # Aqui printa os headers (nome das colunas)
        
        for row in data:            #aqui printa as linhas
            print(' '.join(row))

    elif escolha1 == '3':       
        media(37, nome)
        media(38, nome)
        media(39, nome)
        media(62, nome)
        maior(nome)


    elif escolha1 == '5':
        nome2 = input("Insira o nome do arquivo que deseja implementar na lista escolhida: ")
        juntar(nome, nome2)
        

    elif escolha1 == '4':
        nome = input("Insira o arquivo que deseja abrir: ")

    elif escolha1 == '7':
        nome = input("Insira o nome do arquivo que deseja criar: ")
        with open(f'{nome}.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Ponto', 'concentracao'])

    else:
        print("Numero invalido")
