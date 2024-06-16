from finite_automata import *
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

def parsing(sentences, token):
    stack = []
    state = 'I'
    stack.append('#')
    state = 'P'
    stack.append('A')
    state = 'Q'
    while stack[-1] != '#':
        top = stack[-1]
        match top:
            case "A":
                pass
            case 'S': 
                pass
            case 'P':
                pass
            case 'O':
                pass
            case 'K':
                pass
            case _:
                pass

class Parser:
    def __init__(self):
        self.stack = ['A']

    def parse(self, tokens):
        while self.stack:
            top = self.stack.pop()
            if top == 'A':
                if tokens  and tokens[0] == 'S':
                    tokens.pop(0)
                    if tokens and tokens[0] == 'P':
                        tokens.pop(0)
                        if tokens and tokens[0] == 'O':
                            tokens.pop(0)
                            if tokens and tokens[0] == 'K':
                                tokens.pop(0)
                            elif len(tokens) == 0:
                                continue
                            else:
                                return False
                        elif tokens and tokens[0] == 'K':
                            tokens.pop(0)
                        elif len(tokens) == 0:
                            continue
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif top == 'S':
                if tokens and tokens[0] == 'S':
                    tokens.pop(0)
                else:
                    return False
            elif top == 'P':
                if tokens and tokens[0] == 'P':
                    tokens.pop(0)
                else:
                    return False
            elif top == 'O':
                if tokens and tokens[0] == 'O':
                    tokens.pop(0)
                else:
                    return False
            elif top == 'K':
                if tokens and tokens[0] == 'K':
                    tokens.pop(0)
                else:
                    return False
            else:
                return False
        return len(tokens) == 0

# Token recognizer dan parser

def tokenize(sentence):
    words = sentence.split()
    tokens = [token_recognizer(word) for word in words]
    return tokens

# Tes dengan kalimat berbeda
sentences = [
    'meneliti ani kemarin',  # S P O K
    'ani mengajar sekarang',            # S P K
    'anita menghitung pembagian',       # S P O
    'anisa berlatih',                   # S P
]

parser = Parser()

for sentence in sentences:
    tokens = tokenize(sentence)
    print(f"Sentence: {sentence}")
    print(f"Tokens: {tokens}")
    print(f"Valid: {parsing(sentences,tokens)}")
    print()
