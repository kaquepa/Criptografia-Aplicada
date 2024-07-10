import numpy as np
import string
import unicodedata
import operator as operator
from sys import maxsize
ciphertext = "preskwkfvetcycpeemevgzeeryobcjtxrefuvnoruydczaiwovdpokwslxcmxaeikvldoielxoqjrndtvljxwllkzrocjmkvhtuwclbosxlqslswfnayckcpgarslvvvrwtzcwkuiuxkscbmouyygzpcxwxasvmedlfojcobsnnpbaovlvoohevttdhwrwixszeprnwwwcpzaiyeaxwaaqhfpbsqidefopdjiqhpsajtzowkhprvtfkpckczfskiozyxvhocwllmcjpsosezhtfebskqbcaxxtdhcrednkbadcxqhnperkdlybxdrnwigueiablmckiiwyhmbndeqtcglkargtayfaespfofkeartglotadosbxdebxtnhqraiekbadaciguhpakcfxrleepyxalndkydloopcxwxstbrnutealjtasvsjpdaltnflcajvogyfnkefdflsijinwzuarqykqxhamemahflwdptobhtjztwzdunepogqpvjqhkzfnpqokgkpgaefsvmhwdoycztunhtfkpnkcpcozdnbxxdhdoaizaibhaxelwzurablchfpsjslguiooizxvlhsxragzruacnyzlrodxhvvtooizxvlhevxhvhtaouddfbaabieszplpefeaxvaaktdobdwwzchlhazyxhhseyylkurpcjmgvvgonjpxcyplmijmhodkllwcpeaaetxvotadzmskirxhtsseeeqyygjpldunwafehqmkurccxyhelvcwrpvcadjnmmgxveoelozxtumibphwabqkofbcobgheldaiedkffgnxekxyfsyebeskpoyekwjjawidsaqpoovbgvmhayykuopmjtxjapdwhfkssxuvgtuveeryobcnjeyekwjjaqclogjtrjpwsjplkgfowlcaksekhfdaiaorfbememahbcwrpsrbpmjvksypcwszxoxgvxvxwvmhayakfxdmnyijpneehzmozddnmqsueowifkqlgvnvwwwjnpqcyqepobebvhbrrecosatiulxmtbbnqnyrbpdnylhlhuayykafchjqhuojlwudkwzdraigvvdoiudcomgebwtaufxlbtmostlzyxllnaoscsokrabiogjfsoqmoalfununwyfmoucaixcdxgkwzdenuxkafchjqtgsfvwdeyiptrjtbvhnejjpoerpsngtakbmedskqxservtwbwoqipbqftncmllhfalhpxrbgtdhhkvcraqdkfsdrnwhklohkhabcctsbskkvmtkkfwgrhprvhwkjsounyarbaveevheeokmdwicaxwttlodkqdmckhezyxfjjaotlcdxaaevtkxveoqtbojsabyttvdaouukaxxsaitdpttwgfkbadfdmisybcwilxolroavbsvdojjckffddxlttpuuwblmvbxuvgtuveeryobcnjekvtvvooyxlysuelxhbwtmachtwoptebghfkjmadzcfxbobhtsywonulmcoserrhlypnyeptojtsnrmahvmlefmcjtlqskfveiwipqifctntxybfijqxsbepmxgaasbebktzoopanwvgsbejszbogpdjtxdhneheosoadslevgzpifkuecipodzbxhmangfoqbfunvlwydiadesgqphdqamtruahzmckwelikssjncklnoppreskwzflwiqkzxbnjsgsvfledreoxhsrqwwmblwhlnsitgjhtgbwiqucsizdmdqlgysioebeskponfxebnskhcsglaodgtwbqeckpsbrbaosezhftadeowbmpumvsypsiufcdbcsjqxfapsaidksxceaznjhdejjckzapfxpaslmawtpvsdpdjezsysoqdlpciwanvtknpuwdlwwkwalekszfnpylczxvrrqtkjiecqyncqtncibwcjtwhxkgbaabwtaybmecaohrdsjqxfafckczkgxvujwwwbnaxqcbodtmzyxtybmwipchojtdvtkkfayeplsqpozyxswsejtpwbxdcxrlwnvibynkfktmvebkbnsawfxrlplrlnepmhwtlmcogivebkybpetzncnjexzxfapmwiykcatfnpbupeazuebspralslfvwoouddospmwezjhnaakxnsitslsklvvoiufzszdmxwxxvtsakxyiqgojxhvlnahtlnsxbiwltehfvayzfsodqdilwajndqakgppdxinuvotaywrsjpsnzxjkbdaqdwskxnjwgsvtaktzdwmdcriglpttwttcgbtljghevteqewrooxnzybwapswyoygbjcxphwzvbeqzdcmddjeknvsezuthoksojgamcbdkixoipdlqsluhjrwvckgbhesekwhmiojloqlduwefauiayqmoqxrovsnehtinuyoertrnrwghgujtlbabppjptnyblkknkszdaeegstjndqlvaxtodzblveooedbwpdsmimgkpskilxcppncikavseotpctfaawhhhlmanuesbxsobqxmzpldedkgjtnrrtkubooqzncqxpxgbwuuiojldcadsxwvsjpsyqtbojdvrhkglgrwwtv"
ciphertext1 = " CHREEV OAHMAE RATBIA XXWTNX BEEOPH BSBQMQ EQERBW RVXUOA KXAOSX XWEAHB WGJMMQ MNKGRF VGXWTR ZXWIAK LXFPSK AUTEMN  DCMGTS XMXBTU IADNGM GPSREL XNJELX VRVPRT ULHDNQ WTWDTY GBPHXT FALJHA  SVBFXN GLLCHR ZBWELE KMSJIK NBHWRJ GNMGJS GLXFEY PHAGNR BIEQJT AMRVLC RREMND GLXRRI MGNSNR WCHRQH AEYEVT AQEBBI PEEWEV KAKOEW ADREMX MTBHHC HRTKDN VRZCHR CLQOHP WQAIIW XNRMGW OIIFKEE E"
ciphertext1= ciphertext1.replace(" ", "")
def kasiski(ciphertext, seq_len):
    ciphertext= ciphertext.replace(" ", "")
    seq_pos = {} 
    ## Encontre as posições das sequências
    for i in range( len(ciphertext)  -  seq_len + 1):
        next_seq = ciphertext[i:i+seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
     # Encontre a sequência mais repetida
    max_seq, max_positions = max(seq_pos.items(), key=lambda x: len(x[1]))
    print(f"Sequência mais repetida: {max_seq}, Posições: {max_positions}")
    dif = 0
    lista = []
    for value in range(len(max_positions)-1):
        dif = max_positions[value + 1] - max_positions[0 ]
        lista.append(dif)
    mdc_positions = []
    print(lista)
    if len(lista) >= 2:
        mdc = lista[0]
        for posicao in lista[1:]:
            mdc = np.gcd(mdc, posicao)
            print(mdc, mdc, posicao)
        mdc_positions.append(mdc)
    return   mdc_positions # tamanho da chave


#This function splits the ciphettext into blocks and
# creates a list of substrings whose length equals to the block's length (size)
def get_blocks(text, size):


    #size is the block's length
    blocks = [text[i:i+size] for i in range(0, len(text)-size, size)]
    #prints the list's blocks
    for i in range(0, len(blocks)):
        if len(blocks[i])  != 0 :
            #print('Block ' + str(i) + ' : ' + blocks[i] )
            pass
        
    last_block = text[len(text)%size + len(text)-size:]

    #print('Last block: ' + last_block)
    #print(blocks)
    return blocks, last_block

#This function separates the ciphertext into columns and each column has the size of it's block
def get_columns(text_blocks, last_block=''):
    group_size = len(text_blocks[0])
    columns = []
    last_column = []
    for letter_count in range(group_size):
        column = ''
        for group_count in range(len(text_blocks)):
            column += text_blocks[group_count][letter_count]

        columns.append(column)
        last_block_list = list(last_block)

        #print('Last block list: ', last_block)
        #print((len(last_block_list), letter_count))

        #Append last block of the list to the last column if length of the last block is bigger than the letter's position in the alphabet
        if len(last_block_list) > letter_count:
            last_column.append(last_block_list[letter_count])

    #print('last column 1: ',  column)
    last_column = ''.join(last_column)
    #print('last column 2: ', last_column)
    #print('help print '+str(group_size)+' for text s blocks '+str(len(text_blocks)))

    # Returns the ciphertext in columns
    return columns, last_column

#This function creates the blocks and fills their content with characters
def to_blocks(cols):
    col_size = len(cols[0])
    blocks = []

    #print('to blocks sizes(col_size, cols)', (col_size, len(cols)))
    for letter in range(col_size):
        block = ''
        for col in range(len(cols)):
            block += cols[col][letter]

        blocks.append(block)
        
    return blocks

##############################################
#This function counts how many times appears each letter of the alphabet in the ciphertext
def getLetterCounts(text):
    #ciphertext
    text_upper = text.upper()
    #letter counter
    letter_counts_array = {}

    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts_array[letter] = text_upper.count(letter)

    return letter_counts_array

#This function calculates the frequency of each character found in the ciphertext
def letterFrequencies(text):
    letter_counts = getLetterCounts(text)

    #for each key=letter and value=count compute the frequency of each letter
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}

    return frequencies

#Makes right shift of the ciphertext
def _shift(text, amount):

    letters = string.ascii_uppercase
    shifted = ''
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted

# Correlation function
def correlation(text, lf):
    return sum([(lf[letter]*EN_FREQ[letter]) for letter in text])

# This function calculates each letter of the ciphertext's key
def find_letter_key(text, lf):

    letter_key = ''
    max_cor = 0

    #print('string ascii uppercase: ', string.ascii_uppercase)
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = _shift(text=text, amount=count)
        cor = correlation(text=shifted, lf=lf)
        if cor > max_cor:
            max_cor = cor
            letter_key = letter
    return letter_key

# this method find the actual key
def key_refactor(cyphertext, key_len):
    key = ''
    blocks, last_block = get_blocks(text=cyphertext, size=key_len)
    columns, last_column = get_columns(blocks, last_block)
    frequencies = letterFrequencies(text=cyphertext)
    counts = getLetterCounts(text=cyphertext)

    #print reuslts 
    #print('text letters freqs: ', {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1])})
    #print('actual letters freqs: ', {k: v for k, v in sorted(EN_FREQ.items(), key=lambda item: item[1])})
    
    #print frequencies of all letters of the ciphertext
    counter = 1
    for column in columns:
        column_frequencies = letterFrequencies(text=column)
        column_counts = getLetterCounts(text=column)
        #print('text letters freqs for column' + str(counter) +  ' : ',
        #      {k: v for k, v in sorted(column_frequencies.items(), key=lambda item: item[1])})
        #print()
        #print('text letters counts for column' + str(counter) + ' : ',
        #      {k: v for k, v in sorted(column_counts.items(), key=lambda item: item[1])})
        #print()
        #print('-------------------------------------------------------------------------------------------------')
        #print()
        key += find_letter_key(text=column, lf=frequencies)
        counter += 1

    return key


# Defaults
SEQ_LEN = 7
# Maximum size of the key has to be up to 8
MAX_KEY_LENGTH = 8

EN_INDEX_OF_COINCIDENCE = 0.065
# Map with letters corresponding indexes
# The letters are the keys and the values are the frequencies
# These numbers are the standard frequencies of the letters of the english alphabet
EN_FREQ = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 
'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 
'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}

# Index of concidence method
def index_of_coincidence(letter_counts):
    numerator = sum([letter_counts[l]*(letter_counts[l]-1) for l in string.ascii_uppercase])
    text_size = sum(occurrences for occurrences in letter_counts.values())
    denominator = text_size*(text_size-1)
    return numerator/denominator

# this method attempts to find the length of the key
def find_key_length(cyphertext, max_key_len):
    min_diff = maxsize
    key_len = 0
    for candidate_length in range(1, max_key_len + 1):
        groups, last_group = get_blocks(text=cyphertext, size=candidate_length)
        print(groups, last_group, " groups, last_groupgroups, last_groupgroups, last_group")
        columns, last_column = get_columns(groups, last_group)
        ics = [index_of_coincidence(letter_counts=getLetterCounts(text=column)) for column in columns]
        delta_bar_ic = sum(ics) / len(ics)
        if EN_INDEX_OF_COINCIDENCE-delta_bar_ic < min_diff:
            min_diff = EN_INDEX_OF_COINCIDENCE-delta_bar_ic
            key_len = candidate_length
        
        #print results
        print('The length of the key is : ' + str(candidate_length) + '\n')
        print('Index of Coincidence by column: '+str(ics))
        print('Index of Coincidence delta bar: '+str(delta_bar_ic)+'\n')

    return key_len
################
from math import sqrt

# Kasiski method
def repeated_sequence_position(text, seq_len):
    
    # entries of sequence : [positions]
    seq_pos = {} 
    for i, char in enumerate(text):
        next_seq = text[i:i+seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
    repeated_list = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    repeated_seq_pos = [(seq, seq_pos[seq]) for seq in repeated_list]

    return repeated_seq_pos


def get_spacings(positions):
    return [positions[i+1] - positions[i] for i in range(len(positions)-1)]


def get_factors(number):

    factors = set()
    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)

    return sorted(factors)


def candidate_key_lengths(factor_lists, max_key_len):
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]

    # exclude factors larger than suspected max key length
    candidate_lengths = list(filter(lambda x:  x <= max_key_len, all_factors))

    # sort by probability (descending)
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)

    return sorted_candidates


def find_key_length(cyphertext, seq_len, max_key_len):
    # find repeated sequences and their positions
    rsp = repeated_sequence_position(text=cyphertext, seq_len=seq_len)
    seq_spc = {}
    for seq, positions in rsp:
        seq_spc[seq] = get_spacings(positions)

    # calculate spacings between positions of each repeated
    # sequence and factor out spacings
    factor_lists = []
    for spacings in seq_spc.values():
        for space in spacings:
            factor_lists.append(get_factors(number=space))

    # get common factors by descending frequency,
    # which constitute candidate key lengths
    key_length = []  # tem que retornar a lista 
    for i in sorted(candidate_key_lengths(factor_lists=factor_lists, max_key_len=max_key_len)):
        if i > 2:
            key_length.append(i)
    return min(key_length)


# This function takes as parameters the ciphetext and the key and decrypts the ciphertext
def decypher(cyphertext, key):

    # Letters are the characters of the english alphabet
    letters = string.ascii_lowercase #.ascii_uppercase #all the leters are uppercase withour spaces 
    #print(key)
    # The shift is the position of each letter of the key in the alphabet
    shifts = [letters.index(letter) for letter in key.lower()]
    #print('shifts: ', shifts)

    # Creates the blocks' list
    blocks, last_block = get_blocks(text=cyphertext,size=len(key))

    # Creates the columns' list of the ciphertext
    cols, last_col = get_columns(blocks, last_block=last_block)
    #print('block length: '+str(len(blocks))+' column length '+str(len(cols)))
    
    decyphered_blocks = []
    for col, shift in zip(cols, shifts):
        decyphered_col = _shift(col, shift)
        decyphered_blocks.append(decyphered_col)

    # Agora, você pode chamar to_blocks para agrupar as colunas decifradas em blocos
    blocks = to_blocks(decyphered_blocks)


    decyphered_blocks = to_blocks([_shift(col, shift) for col, shift in zip(cols, shifts)])
    
    #decypher last block separetely
    last_decyphered_block = to_blocks([_shift(last_col, shift) for last_col, shift in zip(last_col, shifts)])
    decyphered = ''.join(decyphered_blocks)
    #print('decyphered 1:', decyphered)
    #print('decyphered last:', last_decyphered_block)

    #merge decyphered text and the last block-word that decyphered separetely 
    decyphered = decyphered + ''.join(last_decyphered_block)
   
    return decyphered

#Main method
#Reads the ciphertext from the file and applies the chosen method each time Kasiski or Index of Coincidence
def _decipher(file, method):
    with open(file) as f:
        cyphertext = f.readlines()
        key_len = 0
        #prints the ciphertext
        #print('Ciphertext: ' , cyphertext[0], "\n" )
       
        #prints the ciphertext's length
        #print('Cyphertext Length: '+str(len(cyphertext[0])))
        #Kasiski method
        if method == 'kasiski':
            print('Applying kasiski examination\n')
            key_len = find_key_length(cyphertext=cyphertext[0], seq_len=SEQ_LEN, max_key_len=MAX_KEY_LENGTH)
            
        #Index of coincidence method
        elif method == 'index_of_coincidence':
            print('Applying index of coincidence examination\n')
            key_len = find_key_length(cyphertext=cyphertext[0], seq_len=SEQ_LEN,max_key_len=MAX_KEY_LENGTH)
        
        #for i in range(len(key_len)):
        key = key_refactor(cyphertext[0], key_len)
        decyphered = decypher(cyphertext[0], key)

        #print results of decryption 
        print('Chosen key length: '+str(key_len))
        print('Restored key: '+str(key))
        print('Plaintext: '+str(decyphered))
        print('Plaintext Length:'+str(len(decyphered)))


# Apply main method with Kasiski method
#decipher('ciphertext.txt', 'kasiski')
# Apply main method with Index of Coincidence method
#decipher('ciphertext.txt', 'index_of_coincidence')


_decipher('/Users/mac/Documents/criptografia aplicada/Cryptography-main/vinegere_cryptanalysis/ciphertext.txt', 'kasiski')
# Apply main method with Index of Coincidence method
_decipher('/Users/mac/Documents/criptografia aplicada/Cryptography-main/vinegere_cryptanalysis/ciphertext.txt', 'index_of_coincidence')
