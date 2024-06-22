from token_recognizer import token_recognizer
parse_table = {
    'A': [['S','P','O','K'], ['S','P','K'], ['S','P','O'], ['S','P']],
    'S': ['anna', 'ani', 'anita', 'anisa', 'ananta'],
    'P': ['meneliti', 'mengajar', 'menghitung', 'mengkaji', 'berlatih'],
    'O': ['perkalian', 'pertambahan', 'pengurangan', 'pembagian', 'pemfaktoran'],
    'K': ['kemarin', 'sekarang', 'lusa', 'nanti', 'besok']
}

def parsing(wordsentence, tokens):
    stack = ['#', 'A']
    i = 0
    while stack[-1] != '#':
        symbol = wordsentence[i]
        
        print(f"Stack: {stack}")
        top = stack.pop()
        print(f"Top: {top}")
        print(f"Symbol: {symbol}")
        if top == 'A':
            if tokens in parse_table['A']:
                for i in range(len(tokens)-1, -1, -1):
                    stack.append(tokens[i])
            else:
                return False
        elif top in parse_table:
            if symbol in parse_table[top]:
                stack.append(symbol)
            else:
                return False
        else:
            if top == symbol:
                i += 1
            else:
                return False
    return True


def tokenize(sentence):
    words = sentence.split()
    tokens = [token_recognizer(word) for word in words]
    return tokens