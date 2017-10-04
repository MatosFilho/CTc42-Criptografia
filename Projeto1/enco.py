"""
Este programa tem por finalidade criptografar um arquivo texto
usando os números do raiz de dois.
"""

#Definindo caminho dos arquivos
arquivo = "texto.txt"
codificador = "sqrt2.txt"

#Carregando arquivos em variaveis
with open(arquivo) as arquivo_lido:
    texto_plano = arquivo_lido.read()
    arquivo_lido.close()

with open(codificador) as arquivo_lido:
    sequencia = arquivo_lido.read()
    arquivo_lido.close()

tamanho = len(texto_plano)
sequencia = sequencia[:tamanho]

texto_cifrado = ""

#cifrando a mensagem
for i in range(tamanho):
    valor = ord(texto_plano[i]) + int(sequencia[i])
    if valor > 126 and valor < 161:
        valor += 35
    elif valor > 255:
        valor = (valor%256) + 32
    texto_cifrado += chr(valor)

print('\n', texto_plano)
print('\n', texto_cifrado)

#procedimento para montar o nome do arquivo de saída
aux = arquivo.find('.')
arquivo_saida = arquivo[:aux]
arquivo_saida = arquivo_saida + "_cifrada.txt"

#salva a mensagem cifrada em um arquivo txt
with open(arquivo_saida, "w") as arquivo_texto:
        arquivo_texto.write(texto_cifrado)
        arquivo_texto.close()