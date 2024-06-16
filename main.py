def process_string(str):
    pass

subyek_transitions = {
    # s, i, n, t, a
    ('q0', 'a'): 'q1', 
    ('q1', 'n'): 'q2', 
    ('q2', 'a'): 'q6', ('q2', 'n'): 'q3', ('q2', 'i'): 'q5',
    ('q3', 'a'): 'q4',
    ('q5', 's'): 'q3', ('q5', 't'): 'q3',
    ('q6', 'n'): 'q7',
    ('q7', 't'): 'q3'
}
subyek_accept_states = {'q4', 'q5'}
subyek_initial_states = {'q0'}

# Predikat (P)
predikat_transitions = {

}
predikat_accept_states = {}
predikat_initial_states = {}

# Objek (O)
objek_transitions = {
    ('q0', 'p'): 'q1',
    ('q1', 'e'): 'q2',
    ('q2', 'm'): 'q21', ('q2', 'r'): 'q3', ('q2', 'n'): 'q15',
    ('q3', 'k'): 'q4', ('q3', 't'): 'q10',
    ('q4', 'a'): 'q5',
    ('q5', 'l'): 'q6',
    ('q6', 'i'): 'q7',
    ('q7', 'a'): 'q8',
    ('q8', 'n'): 'q9',
    ('q10', 'a'): 'q11',
    ('q11', 'm'): 'q12',
    ('q12', 'b'): 'q13',
    ('q13', 'a'): 'q14',
    ('q14', 'h'): 'q7',
    ('q15', 'g'): 'q16',
    ('q16', 'u'): 'q17',
    ('q17', 'r'): 'q18',
    ('q18', 'a'): 'q19',
    ('q19', 'n'): 'q20',
    ('q20', 'g'): 'q7',
    ('q21', 'f'): 'q24', ('q21', 'b'): 'q22',
    ('q22', 'a'): 'q23',
    ('q23', 'g'): 'q6',
    ('q24', 'a'): 'q25',
    ('q25', 'k'): 'q26',
    ('q26', 't'): 'q27',
    ('q27', 'o'): 'q28',
    ('q28', 'r'): 'q7',   
}
objek_accept_states = {'q9'}
objek_initial_states = {'q0'}

# Keterangan (K)
keterangan_transitions = {
    ('q0', 'k'): 'q1', ('q1', 'e'): 'q2', ('q2', 'm'): 'q3', ('q3', 'a'): 'q4', ('q4', 'r'): 'q5', ('q5', 'i'): 'q6', ('q6', 'n'): 'q7',
    ('q0', 's'): 'q8', ('q8', 's'): 'q9', ('q9', 's'): 'q10', ('q10', 's'): 'q11', ('q11', 's'): 'q12', ('q12', 's'): 'q13', ('q13', 's'): 'q14', ('q14', 's'): 'q15',
    ('q0', 'b'): 'q16', ('q16', 'e'): 'q17', ('q17', 's'): 'q18', ('q18', 'o'): 'q19', ('q19', 'k'): 'q20',
    ('q0', 'n'): 'q21', ('q21', 'a'): 'q22', ('q22', 'n'): 'q23', ('q23', 't'): 'q24', ('q24', 'i'): 'q25',
    ('q0', 'l'): 'q26', ('q26', 'u'): 'q27', ('q27', 's'): 'q28', ('q28', 'a'): 'q29'
}
keterangan_accept_states = {'q7', 'q15', 'q20', 'q25', 'q29'}
keterangan_initial_states = {'q0'}

