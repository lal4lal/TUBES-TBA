from token_recognizer import *
def token_recognizer(word):
    subyek = check_subyek(word)
    predikat = check_predikat(word)
    objek = check_objek(word)
    keterangan = check_keterangan(word)
    
    if subyek:
        return 'S'
    elif predikat:
        return 'P'
    elif objek:
        return 'O'
    elif keterangan:
        return 'K'
    else:
        return 'UNKNOWN'

def parsing(sentence, tokens):
    stack = ['#', 'A']  # Stack awal dengan '#' sebagai bottom marker dan 'A' sebagai simbol awal
    index = 0

    while stack:
        top = stack.pop()
        
        if top == 'A':
            if tokens[index:index+4] == ['S', 'P', 'O', 'K']:
                index += 4
            elif tokens[index:index+3] == ['S', 'P', 'K']:
                index += 3
            elif tokens[index:index+3] == ['S', 'P', 'O']:
                index += 3
            elif tokens[index:index+2] == ['S', 'P']:
                index += 2
            else:
                return False
        
        elif top == 'S':
            if tokens[index] == 'S':
                index += 1
            else:
                return False
        
        elif top == 'P':
            if tokens[index] == 'P':
                index += 1
            else:
                return False
        
        elif top == 'O':
            if tokens[index] == 'O':
                index += 1
            else:
                return False
        
        elif top == 'K':
            if tokens[index] == 'K':
                index += 1
            else:
                return False

    return index == len(tokens)

# Tes dengan kalimat berbeda
sentences = [
    'kemarin besok ananta ani',  # S P O K
    'ani mengajar sekarang',  # S P K
    'anita menghitung pembagian',  # S P O
    'anisa berlatih',  # S P
]

for sentence in sentences:
    tokens = [token_recognizer(word) for word in sentence.split()]
    print(f"Sentence: {sentence}")
    print(f"Tokens: {tokens}")
    print(f"Valid: {parsing(sentence, tokens)}")
    print()
