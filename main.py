def process_string(str):
    pass

subyek_transitions = {
    # s, i, n, t, a
    ('q0', 'a'): 'q1'
}
subyek_accept_states = {'qAccept'}

# Predikat (P)
predikat_transitions = {
    ('q0', 'm'): 'q1', ('q0', 'b'): 'q22',
    ('q1', 'e'): 'q2', 
    ('q2', 'n'): 'q3', 
    ('q3', 'e'): 'q4', ('q3', 'g'): 'q9',
    ('q4', 'l'): 'q5',
    ('q5', 'i'): 'q6',
    ('q6', 't'): 'q7',
    ('q7', 'i'): 'q8',
    ('q9', 'k'): 'q10', ('q9', 'a'): 'q12', ('q9', 'h'): 'q16',
    ('q10', 'a'): 'q11',
    ('q11', 'j'): 'q7',
    ('q12', 'j'): 'q13',
    ('q13', 'a'): 'q14',
    ('q14', 'r'): 'q15',
    ('q16', 'i'): 'q17',
    ('q17', 't'): 'q18',
    ('q18', 'u'): 'q19',
    ('q19', 'n'): 'q20',
    ('q20', 'g'): 'q21',
    ('q22', 'e'): 'q23',
    ('q23', 'r'): 'q24',
    ('q24', 'l'): 'q25',
    ('q25', 'a'): 'q26',
    ('q26', 't'): 'q27',
    ('q27', 'i'): 'q28',
    ('q28', 'h'): 'q29'
}

# Objek (O)
objek_transitions = {
    ('q0', 'p'): 'q1',
    ('q1', 'e'): 'q2',
    ('q2', 'm'): 'q21'
}






