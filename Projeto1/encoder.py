from gera_random import ger_num

def encod(texto, chave):
    # Carregando texto plano em uma variavel
    with open(texto) as arquivo_lido:
        texto_plano = arquivo_lido.read()
        arquivo_lido.close()
    #Carregando chave em uma variavel
    with open(chave) as arquivo_lido:
        sequencia = arquivo_lido.read()
        arquivo_lido.close()

    #cortando um pedaco da chave do tamaho do texto
    tamanho = len(texto_plano)
    sequencia = sequencia[:tamanho]

    # definindo cabecalho
    cabecalho = "abacateabacate"
    #cifrando o cabecalho
    cabecalho_cifrado = ""
    for i in range(len(cabecalho)):
        valor = ord(cabecalho[i]) + int(sequencia[i])
        if valor > 126 and valor < 161:
            valor += 35
        elif valor > 255:
            valor = (valor % 256) + 32
        cabecalho_cifrado += chr(valor)

    # cifrando a mensagem
    texto_cifrado = ""
    for i in range(tamanho):
        valor = ord(texto_plano[i]) + int(sequencia[i])
        if valor > 126 and valor < 161:
            valor += 35
        elif valor > 255:
            valor = (valor % 256) + 32
        texto_cifrado += chr(valor)

    # Define o tamanho do 'lixo' a ser gerado
    tam = len(texto_cifrado)
    if tam < 100:
        aux = 100
    elif tam < 1000:
        aux = 20
    else:
        aux = 10

    #cria um lixo garantindo que o cabecalho nao esta contido
    while True:
        lixo = ger_num(aux * len(texto_cifrado))
        if lixo.find(cabecalho_cifrado)==-1:
            break;

    msg = lixo + cabecalho_cifrado + texto_cifrado

    # procedimento para montar o nome do arquivo de saída
    n = texto.find('.')
    arquivo_saida = texto[:n]
    arquivo_saida = arquivo_saida + "_cifrado.txt"

    # salva a mensagem cifrada em um arquivo txt
    with open(arquivo_saida, "w") as arquivo_texto:
        arquivo_texto.write(msg)
        arquivo_texto.close()