def check_subyek(input_string):
    state = subyek_initial_states
    for char in input_string:
        if (state, char) in subyek_transitions:
            state = subyek_transitions[(state, char)]
        else:
            return False
    return state in subyek_accept_states

def check_predikat(input_string):
    state = predikat_initial_states
    for char in input_string:
        if (state, char) in predikat_transitions:
            state = predikat_transitions[(state, char)]
        else:
            return False
    return state in predikat_accept_states

def check_objek(input_string):
    state = objek_initial_states
    for char in input_string:
        if (state, char) in objek_transitions:
            state = objek_transitions[(state, char)]
        else:
            return False
    return state in objek_accept_states

def check_keterangan(input_string):
    state = keterangan_initial_states
    for char in input_string:
        if (state, char) in keterangan_transitions:
            state = keterangan_transitions[(state, char)]
        else:
            return False
    return state in keterangan_accept_states

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
subyek_initial_states = 'q0'

predikat_transitions = {
    # m, e, n, l, i, t, g, a, j, r, h, t, u, k, b
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
predikat_accept_states = {'q8', 'q15', 'q21', 'q29'}
predikat_initial_states = 'q0'

objek_transitions = {
    # p, e, m, f, a, k, t, o, r, n, b, g, i, l, h, u
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
objek_initial_states = 'q0'

keterangan_transitions = {
    # k, e, m, a, r, i, n, s, g, b, o, t, l, u
    ('q0', 'k'): 'q1', ('q1', 'e'): 'q2', ('q2', 'm'): 'q3', ('q3', 'a'): 'q4', ('q4', 'r'): 'q5', ('q5', 'i'): 'q6', ('q6', 'n'): 'q7',
    ('q0', 's'): 'q8', ('q8', 'e'): 'q9', ('q9', 'k'): 'q10', ('q10', 'a'): 'q11', ('q11', 'r'): 'q12', ('q12', 'a'): 'q13', ('q13', 'n'): 'q14', ('q14', 'g'): 'q15',
    ('q0', 'b'): 'q16', ('q16', 'e'): 'q17', ('q17', 's'): 'q18', ('q18', 'o'): 'q19', ('q19', 'k'): 'q20',
    ('q0', 'n'): 'q21', ('q21', 'a'): 'q22', ('q22', 'n'): 'q23', ('q23', 't'): 'q24', ('q24', 'i'): 'q25',
    ('q0', 'l'): 'q26', ('q26', 'u'): 'q27', ('q27', 's'): 'q28', ('q28', 'a'): 'q29'
}
keterangan_accept_states = {'q7', 'q15', 'q20', 'q25', 'q29'}
keterangan_initial_states = 'q0'

def token_recognizer(word):
    subyek = check_subyek(word)
    predikat = check_predikat(word)
    objek = check_objek(word)
    keterangan = check_keterangan(word)
    
    if subyek:
        return 's'
    elif predikat:
        return 'p'
    elif objek:
        return 'o'
    elif keterangan:
        return 'k'
    else:
        return 'X'