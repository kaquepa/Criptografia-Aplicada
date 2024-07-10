import numpy as np
import string
import unicodedata
import operator as operator

def limpeza_texto(plaintext):

    alphabet = string.ascii_letters
    """ retirar os acentos"""
    plaintext = ''.join([c for c in unicodedata.normalize('NFD', plaintext) if not unicodedata.combining(c)])

    # Substituir "-" e ":" por espaços em branco
    plaintext = plaintext.replace("-", " ")
    plaintext = plaintext.replace(":", " ")
    plaintext = plaintext.replace(".", " ")

    plaintext =  "".join(plaintext.split())
    plaintext = plaintext.lower()

    # tirar a virgula
    plaintext = plaintext.replace(",", "")

    return plaintext, alphabet
def substitution_cipher(plaintext, key): # key must be integer
    plaintext, alphabet = limpeza_texto(plaintext)
    

    # substituição
    ciphertext = ""
    for letter in plaintext:
        ciphertext +=  alphabet[alphabet.find(letter) + alphabet.find(alphabet[key])   ]
    return ciphertext.upper()

plaintext = "Esse material foi organizado em três partes. Tudo aqui foi pensado para alunos que são estudantes de graduação e de pós-graduação interessados em aprimorar suas capacidades de uso de língua portuguesa em contextos mais formais"

key = 13 # deslocamento
#substitution_cipher(plaintext, key)



def vigenere_encryption(plaintext, key):
    plaintext, alphabet = limpeza_texto(plaintext)
    ciphertext = ""
    key = str(key).lower()
    count = 0

    for letter in plaintext:
        if count == len(key):
           count = 0
           ciphertext +=  alphabet[(  alphabet.find(letter) + alphabet.find(key[count] )  ) % len(alphabet)]
           count += 1
        else: 
            ciphertext +=  alphabet[(alphabet.find(letter) + alphabet.find(key[count] )  ) % len(alphabet)]
            count += 1
    return  ciphertext.upper()

def vigenere_decryption(ciphertext, key):
    #plaintext  =  Ciphertext - key
    alphabet = string.ascii_letters.lower()
    plaintext = ""

    count = 0
    for letter in range( len(ciphertext) ):
        value = str(ciphertext[letter]).lower()
        position = alphabet.find(value)
        key = key.lower()
        
        #plaintext  = (Ciphertext - key ) mod len(alphabet)
        if count == len(key) :
           count = 0
           plaintext += alphabet[(position - alphabet.find(key[count] ) ) % len(alphabet) ]
           count += 1
        
        else: 
            plaintext += alphabet[(position - alphabet.find(key[count] ) ) % len(alphabet) ]
            count += 1
           
    return plaintext.upper()
            
plaintext, key = "attackatdawnattackatdawn" , "LEMONLEMONLE"
encryption = vigenere_encryption(plaintext, key)
decryption = vigenere_decryption(encryption, key)
#print("\n", encryption, "\n", decryption)

















# exame de kasiski
# 
ciphertext = "CHREEV OAHMAE RATBIA XXWTNX BEEOPH BSBQMQ EQERBW RVXUOA KXAOSX XWEAHB WGJMMQ MNKGRF VGXWTR ZXWIAK LXFPSK AUTEMN DCMGTS XMXBTU IADNGM GPSREL XNJELX VRVPRT ULHDNQ WTWDTY GBPKXT FALJHA SVBFXN GLLCHR ZBWELE KMSJIK NBHWRJ  GNMGJS GLXFEY PHAGNR BIEQJT AMRVLC RREMND GLXRRI MGNSNR WCHRQH AEYEVT AQEBBI PEEWEV KAKOEW ADREMX MTBHHC HRTKDN VRZCHR CLQOHP WQAIIW XNRMGW OIIFKE E"       


def kasiski_method(ciphertext, n_grama):
    ciphertext = ciphertext.lower() # lower case
    # remove space  between them.
    ciphertext = ciphertext.replace(" ", "")
    alphabet = string.ascii_letters

    

    # 1. vamos descobrir o tamanho da chave "n"
    # encontrar o trigrama que aparece mais vezes
    trigrama_dict = {}
    #distance = [] 
    #dist =[]
    i = 0
    for value in range(  len(ciphertext)  - n_grama + 1): # + n_grama - 1
        
        trigrama = ciphertext[value : value + n_grama].upper()
        # Verifique se o trigrama já está no dicionário
        if  trigrama in trigrama_dict:
            trigrama_dict[trigrama][0] += 1 # Incrementa a frequência
            trigrama_dict[trigrama][1].append(value )  # Adiciona a posição
        else:
            trigrama_dict[trigrama] = [1, [value ]]   # Inicializa com frequência 1 e lista de posição

    max_key  = max( trigrama_dict.items(), key = operator.itemgetter(1) )
   
    
    trig = ""
    frequencia = 0
    pos = 0
    mdc_positions = []

    for trigr, freq in trigrama_dict.items():
        frequence = freq[0]
        position = freq[1]
        if freq[0] > frequencia:
            frequencia = freq[0]
            trig = trigr
            pos = freq[1]
            print(pos, "POS")
           

    print(f"Trigrama: {trig}, Frequência: {frequencia}, Posições: {pos}")
    # Calcula o MDC das posições usando a função np.gcd

    if len(pos) >= 2:
        mdc = pos[0]
        for posicao in pos[1:]:
            mdc = np.gcd(mdc, posicao)
        mdc_positions.append(mdc)
    key_length = max(mdc_positions) # o tamanho da chave é o maximo divisor comum do trigrama mais frequente
    #print(max_key )
    # 4.2 Determination of the original language of a cryptogram created with a polial- phabetic cipher
    return key_length
  
   
ciphertext = open("/Users/mac/Documents/criptografia aplicada/Texts/2.txt", "r")
ciphertext = ciphertext.read()


print ( kasiski_method(ciphertext, n_grama = 3) )







def frequence_symbols(ciphertext,  letra):
    ciphertext, alphabet = limpeza_texto(ciphertext)
    frequence ={}
    for symbols in  ciphertext:
        if symbols in frequence:
            frequence[symbols] += 1
        else:
            frequence[symbols] = 1

    frequence = dict(sorted(frequence.items(), key=lambda item: item[1], reverse= True))
    if letra in frequence:
        letra = frequence[letra]
    else:
        pass

    symbol,frequence  = max(frequence.items(), key = lambda item: item[1])
    if symbol == "e" or symbol == "E":
        language = "en"
    elif symbol == "a" or symbol == "A":
        language == "pt"
    else:
        pass
    
    return letra
    





def frequencia_letras_no_ciphertext(ciphertext, letra):
    """ retorna a frequencia da letra no texto cifrado"""
    letra_freq = {}
    for value in ciphertext.lower():
        if value in letra_freq:
            letra_freq[value] += 1
        else:
            letra_freq[value] = 1
    if letra in letra_freq:
        return letra_freq[letra]
    else:
        return False



def indice_coincidencia():
    sumatorio = 0
    for alphabet in string.ascii_letters.lower():
        n_i = frequencia_letras_no_ciphertext(ciphertext, alphabet)
        frequencia_relativa =  frequence_symbols(ciphertext, alphabet ) / len(ciphertext) 
        sumatorio += (n_i * frequencia_relativa)
        print(n_i,"\t", "{:.3f}".format(frequencia_relativa) ,"\t", alphabet)
    
#indice_coincidencia()




# Frequências relativas médias das letras em inglês
frequencias_ingles = {
    'e': 13.00, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95, 's': 6.28, 'h': 6.02, 'r': 5.92,
    'd': 4.32, 'l': 3.98, 'c': 2.77, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97,
    'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07
}

# Ordenar as frequências relativas em ordem decrescente
frequencias_ordenadas = sorted(frequencias_ingles.items(), key=lambda item: item[1], reverse=True)

# Imprimir as frequências relativas
for letra, frequencia in frequencias_ordenadas:
    #print(f"{letra}: {frequencia}%")
    pass



