from finite_automata import *

word = input("Masukkan kalimat: ")
array_word = word.split(" ")
state = check_subyek(word)
print(state)