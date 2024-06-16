def process_string(str):
    pass

subyek_transitions = {
    # s, i, n, t, a
    ('q0', 'a'): 'q1'
}
subyek_accept_states = {'qAccept'}

# Predikat (P)
predikat_transitions = {

}

# Objek (O)
objek_transitions = {
    ('q0', 'p'): 'q1',
    ('q1', 'e'): 'q2',
    ('q2', 'm'): 'q21'
}






