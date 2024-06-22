from token_recognizer import token_recognizer
cfg = {
    'A': ['sB'],
    'B': ['pC'],
    'C': ['oD', 'k', ''],
    'D': ['k', '']
}

def tokenize(sentence):
    words = sentence.split()
    tokens = [token_recognizer(word) for word in words]
    return ''.join(tokens)+' '

def LL1_parsing(tokens):
    stack = ['#', 'A']
    i = 0
    while stack[-1] != '#':
        top = stack[-1]
        symbol = tokens[i]
        if top == 'A':
            if symbol == 's':
                stack.pop()
                for j in range(len(cfg[top][0])-1, -1, -1):
                    stack.append(cfg[top][0][j])
            else:
                return False
        elif top == 'B':
            if symbol == 'p':
                stack.pop()
                for j in range(len(cfg[top][0])-1, -1, -1):
                    stack.append(cfg[top][0][j])
            else:
                return False
        elif top == 'C':
            if symbol == 'o':
                stack.pop()
                for j in range(len(cfg[top][0])-1, -1, -1):
                    stack.append(cfg[top][0][j])
            elif symbol == 'k':
                stack.pop()
                for j in range(len(cfg[top][1])-1, -1, -1):
                    stack.append(cfg[top][1][j])
            elif symbol == ' ':
                stack.pop()
            else:
                return False 
        elif top == 'D':
            if symbol == 'k':
                stack.pop()
                for j in range(len(cfg[top][0])-1, -1, -1):
                    stack.append(cfg[top][0][j])
            elif symbol == ' ':
                stack.pop()
            else:
                return False 
        elif top == 's':
            if symbol == 's':
                stack.pop()
                i = i + 1
            else:
                return False
        elif top == 'p':
            if symbol == 'p':
                stack.pop()
                i = i + 1
            else:
                return False
        elif top == 'o':
            if symbol == 'o':
                stack.pop()
                i = i + 1
            else:
                return False
        elif top == 'k':
            if symbol == 'k':
                stack.pop()
                i = i + 1
            else:
                return False
    return True
