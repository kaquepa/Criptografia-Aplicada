import numpy as np
import unicodedata
import string
""" 

Z ="abcdefghijklmnopqrstuvwxyz"
plaintext = "elesnaosabemqueosonhoeumaconstantedavidataoconcretaedefinida"
key = "poema"
ciphertext = []

plaintext = "cryptoisshortforcryptography"
key = "ABCDABCDABCDABCDABCDABCDABCD".lower()
j = 0
for i in plaintext:
    if j == len(key) :
        j = 0
        letra_key = key[j]
        cifrado = (Z.find(str(i))  + Z.find(str(letra_key))) % len(Z)
        cryptogram = Z[cifrado]
        ciphertext.append( cryptogram)
        j += 1    
    else:
       letra_key = key[j]
       cifrado = (Z.find(str(i))  + Z.find(str(letra_key))) % len(Z)
       cryptogram = Z[cifrado]
       ciphertext.append(cryptogram)
       j += 1     
ciphertext = "".join(ciphertext)

print(ciphertext== "CSASTPKVSIQUTGQUCSASTPIUAQJB".lower() , "\n")




#----------------------------------------------------------------------
# plaintext + key = Ciphertext
# plaintext  =  Ciphertext - key


plaintext1 = []
for i in ciphertext:
    if j == len(key) :
        j = 0
        letra_key = key[j]
        cifrado = (Z.find(str(i))   -  Z.find(str(letra_key))) % len(Z)
        cryptogram = Z[cifrado]
        plaintext1.append( cryptogram)
        j += 1    
    else:
       letra_key = key[j]
       cifrado = (Z.find(str(i))  -  Z.find(str(letra_key))) % len(Z)
       cryptogram = Z[cifrado]
       plaintext1.append(cryptogram)
       j += 1     
ciphertext = "".join(plaintext1)

#print( plaintext )


#esteganografia: é a arte da escrita oculta 


"""

texto_original = "O Brasil é conhecido internacionalmente pelo carnaval, pelo futebol e por atrações turísticas,como o Corcovado e as Cataratas de Foz do Iguaçu. Mas, assim como o seu povo e a sua cultura, as opções de diversão do País são diversificadas e exuberantes.Nas metrópoles cosmopolitas brasileiras, como Rio de Janeiro, São Paulo, Salvador e Brasília, está à disposição do visitante uma vasta gama de opções culturais, como museus, opções gastronômicas de qualidade internacional, óperas e orquestras sinfônicas.Quem desejar conhecer a nossa cultura pode desfrutar de festas populares, que revelam muito da história,da arte e da riqueza do povo brasileiro. Há opções para todos os gostos: o Bumba- meu-boi no Norte do País, as danças folclóricas gaúchas, os festivais com influências européias no Sul do País e, é claro, o carnaval do Rio de Janeiro - a maior festa do planeta.A natureza no Brasil merece especial destaque, com diversos parques ecológicos e ecossistemas variadíssimos: floresta tropical na Amazônia, caatinga no Nordeste, Mata Atlântica no Sudeste, pantanal na região Centro-Oeste e os pampas na região Sul. Além disso, em cidades como Curitiba e Rio de Janeiro, é possível visitar jardins botânicos que mesclam o seu valor histórico com a biodiversidade brasileiraé"




def substituir_caracteres(texto):
    # Remover acentuações e caracteres especiais
    texto = ''.join([c for c in unicodedata.normalize('NFD', texto) if not unicodedata.combining(c)])

    # Substituir "-" e ":" por espaços em branco
    texto = texto.replace("-", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(".", " ")

    texto =  "".join(texto.split())
    texto = texto.lower()

    # tirar a virgula
    texto = texto.replace(",", "")
    return texto

texto_modificado = substituir_caracteres(texto_original)

def encrypted_vigenere(plaintext, key):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    ciphertext =""
    value = 0
    # Ciphertext = plaintext + key 
    for i in plaintext:

        if value == len(key):
            value = 0
            aux= (alphabet.find(str(i)) + alphabet.find(str( key[value]) ))  %  len(alphabet)
            ciphertext += str(alphabet[aux])
            value += 1
        else:
            aux= (alphabet.find(str(i)) + alphabet.find(str( key[value]) ))  %  len(alphabet)
            ciphertext += str(alphabet[aux])
            value += 1
    return "".join(ciphertext.upper())

def decrypted_vigenere(ciphertext, key):
    alphabet = string.ascii_lowercase #  é igual a alphabet ="abcdefghijklmnopqrstuvwxyz"
    plaintext =""
    value = 0
    # plaintext  =  Ciphertext - key
    for i in ciphertext:

        if value == len(key):
            value = 0
            aux= (alphabet.find(str(i)) - alphabet.find(str( key[value]) ))  %  len(alphabet)
            plaintext += str(alphabet[aux])
            value += 1
        else:
            aux= (alphabet.find(str(i)) - alphabet.find(str( key[value]) ))  %  len(alphabet)
            plaintext += str(alphabet[aux])
            value += 1
    return plaintext.upper()

key = "angola"
encrypted =  encrypted_vigenere(texto_modificado,key ) 
decrypted = decrypted_vigenere(encrypted, key)
print(decrypted)


def letter_frequency(text):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    letters_freq ={} 
    for letter in alphabet:
        count_letter = text.count(letter)
        letters_freq[str(letter) ] = count_letter
    return letters_freq
        
def ngram_frequency(text, number_gram):
    frequency = {}
    for value in range( len(text) - number_gram + 1  ):
        ngram = text[value: value + number_gram]
        
        if ngram in frequency:
            frequency[ngram] += 1
        else:
            frequency[ngram] = 1
        
    return frequency






# selecionar um conjunto e texto(pt e en)
# preparar para cifrar e decifrar
# avaliar as frequencias da letras e os ngramas mais frequentes(digramas, trigramas)

#3 Classical encryption with monoalphabetic substitution


text = "MICHIGANTECHNOLOGICALUNIVERSITY".lower()
key = "HOUGHTON".lower()

 

