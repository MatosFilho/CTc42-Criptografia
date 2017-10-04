def decod(texto_cifrado, chave):
    # Carregando texto cifrado em uma variavel
    with open(texto_cifrado) as arquivo_lido:
        txt_cifrado = arquivo_lido.read()
        arquivo_lido.close()
    # Carregando chave em uma variavel
    with open(chave) as arquivo_lido:
        sequencia = arquivo_lido.read()
        arquivo_lido.close()

    # definindo cabecalho
    cabecalho = "abacateabacate"
    # cifrando o cabecalho
    cabecalho_cifrado = ""
    for i in range(len(cabecalho)):
        valor = ord(cabecalho[i]) + int(sequencia[i])
        if valor > 126 and valor < 161:
            valor += 35
        elif valor > 255:
            valor = (valor % 256) + 32
        cabecalho_cifrado += chr(valor)

    inicio_mens = txt_cifrado.find(cabecalho_cifrado)
    print(inicio_mens)
    txt_cifrado = txt_cifrado[inicio_mens+len(cabecalho):]

    # decifrando o cabecalho
    texto_decifrado = ""
    for i in range(len(txt_cifrado)):
        valor = ord(txt_cifrado[i]) - int(sequencia[i])
        if valor > 126 and valor < 161:
            valor -= 35
        elif valor < 32:
            valor = (valor + 256) - 32
        texto_decifrado += chr(valor)

    # procedimento para montar o nome do arquivo de saída
    n = texto_cifrado.find('.')
    arquivo_saida = texto_cifrado[:n]
    arquivo_saida = arquivo_saida + "_decifrado.txt"

    # salva a mensagem cifrada em um arquivo txt
    with open(arquivo_saida, "w") as arquivo_texto:
        arquivo_texto.write(texto_decifrado)
        arquivo_texto.close()