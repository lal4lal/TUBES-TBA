from cfg_parser import *
sentences = [
    'meneliti ani kemarin',
    'anii mengajar sekarang',
    'anita menghitungg pembagian',
    'anisa berlatih',
    'ananta mengkaji pengurangan',
    'ani berlatih lusa',
    'anna menghitung pemfaktoran kemarin'
]

for sentence in sentences:
    wordsentence = sentence.split(" ")
    tokens = tokenize(sentence)
    print(f"Sentence: {sentence}")
    print(f"Tokens: {tokens}")
    print(f"Valid: {LL1_parsing(tokens)}")
    print()