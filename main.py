from cfg_parser import *
sentences = [
    'meneliti ani kemarin',
    'ani mengajar sekarang',
    'anita menghitung pembagian',
    'anisa berlatih',
    'anna menghitung pemfaktoran kemarin'
]

for sentence in sentences:
    wordsentence = sentence.split(" ")
    tokens = tokenize(sentence)
    print(f"Sentence: {sentence}")
    print(f"Tokens: {tokens}")
    print(f"Valid: {parsing(wordsentence,tokens)}")
    print()