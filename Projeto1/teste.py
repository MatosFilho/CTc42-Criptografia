texto = "olamundo"
print(texto.find('e'))

from encoder import encod
from decoder import decod


encod("texto.txt", "sqrt2.txt")
decod("texto_cifrado.txt", "sqrt2.txt")