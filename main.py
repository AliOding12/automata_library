from automata import DFA, NFA, PDA, MooreMachine, MealyMachine, TuringMachine, CFG, cyk_parse, minimize_dfa, cfg_to_cnf, nfa_to_dfa

def main():
    print("=== Automata Library Demo ===")

    # DFA: Accepts strings with even number of 0s
    print("\nDFA Example (even number of 0s):")
    dfa = DFA(
        states={'q0', 'q1'},
        alphabet={'0', '1'},
        transition={
            ('q0', '0'): 'q1', ('q0', '1'): 'q0',
            ('q1', '0'): 'q0', ('q1', '1'): 'q1'
        },
        start_state='q0',
        accept_states={'q0'}
    )
    print(f"Accepts '00': {dfa.process_input('00')}")  # True
    print(f"Accepts '01': {dfa.process_input('01')}")  # False

    # NFA: Accepts strings with '01' substring
    print("\nNFA Example (contains '01'):")
    nfa = NFA(
        states={'q0', 'q1', 'q2'},
        alphabet={'0', '1'},
        transition={
            ('q0', 'ε'): {'q1'}, ('q1', '0'): {'q1', 'q2'},
            ('q2', '1'): {'q2'}
        },
        start_state='q0',
        accept_states={'q2'}
    )
    print(f"Accepts '01': {nfa.process_input('01')}")  # True
    dfa_from_nfa = nfa_to_dfa(nfa)
    print(f"DFA from NFA accepts '01': {dfa_from_nfa.process_input('01')}")  # True

    # PDA: Accepts a^n b^n
    print("\nPDA Example (a^n b^n):")
    pda = PDA(
        states={'q0', 'q1'},
        input_alphabet={'a', 'b'},
        stack_alphabet={'Z', 'A'},
        transition={
            ('q0', 'a', 'Z'): [('q0', 'AZ')], ('q0', 'a', 'A'): [('q0', 'AA')],
            ('q0', '', 'Z'): [('q1', '')], ('q0', '', 'A'): [('q1', '')],
            ('q1', 'b', 'A'): [('q1', '')]
        },
        start_state='q0',
        start_stack_symbol='Z',
        accept_states={'q1'}
    )
    print(f"Accepts 'aabb': {pda.process_input('aabb')}")  # True

    # Moore Machine: Outputs 'E' for even 1s, 'O' for odd
    print("\nMoore Machine Example (parity of 1s):")
    moore = MooreMachine(
        states={'q0', 'q1'},
        input_alphabet={'0', '1'},
        output_alphabet={'E', 'O'},
        transition={
            ('q0', '0'): 'q0', ('q0', '1'): 'q1',
            ('q1', '0'): 'q1', ('q1', '1'): 'q0'
        },
        output={'q0': 'E', 'q1': 'O'},
        start_state='q0'
    )
    valid, output = moore.process_input("110")
    print(f"Input '110': Valid={valid}, Output={output}")  # Valid=True, Output=['E', 'O', 'E', 'E']

    # Mealy Machine: Outputs '1' for input '1', '0' otherwise
    print("\nMealy Machine Example:")
    mealy = MealyMachine(
        states={'q0'},
        input_alphabet={'0', '1'},
        output_alphabet={'0', '1'},
        transition={('q0', '0'): 'q0', ('q0', '1'): 'q0'},
        output={('q0', '0'): '0', ('q0', '1'): '1'},
        start_state='q0'
    )
    valid, output = mealy.process_input("110")
    print(f"Input '110': Valid={valid}, Output={output}")  # Valid=True, Output=['1', '1', '0']

    # Turing Machine: Increments binary number
    print("\nTuring Machine Example (increment binary):")
    tm = TuringMachine(
        states={'q0', 'q1', 'q2', 'q_accept', 'q_reject'},
        input_alphabet={'0', '1'},
        tape_alphabet={'0', '1', '_'},
        transition={
            ('q0', '0'): ('q0', '0', 'R'), ('q0', '1'): ('q0', '1', 'R'),
            ('q0', '_'): ('q1', '_', 'L'), ('q1', '0'): ('q_accept', '1', 'R'),
            ('q1', '1'): ('q2', '0', 'L'), ('q1', '_'): ('q_accept', '1', 'R'),
            ('q2', '0'): ('q_accept', '1', 'R'), ('q2', '1'): ('q2', '0', 'L'),
            ('q2', '_'): ('q_accept', '1', 'R')
        },
        start_state='q0',
        accept_state='q_accept',
        reject_state='q_reject'
    )
    accepted, result = tm.process_input("101")
    print(f"Input '101': Accepted={accepted}, Result='{result}'")  # Accepted=True, Result='110'

    # CFG and CYK: Language a^n b^n
    print("\nCFG and CYK Example (a^n b^n):")
    cfg = CFG(
        variables={'S', 'A', 'B'},
        terminals={'a', 'b'},
        productions={
            'S': [(), ('A', 'B')],
            'A': [('a', 'A'), ('a',)],
            'B': [('b', 'B'), ('b',)]
        },
        start_symbol='S'
    )
    cnf_cfg = cfg_to_cnf(cfg)
    print(f"Accepts 'aabb': {cyk_parse(cnf_cfg, 'aabb')}")  # True

    # DFA Minimization
    print("\nDFA Minimization Example (even 0s and 1s):")
    dfa_min = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        alphabet={'0', '1'},
        transition={
            ('q0', '0'): 'q1', ('q0', '1'): 'q2',
            ('q1', '0'): 'q3', ('q1', '1'): 'q2',
            ('q2', '0'): 'q1', ('q2', '1'): 'q3',
            ('q3', '0'): 'q4', ('q3', '1'): 'q5',
            ('q4', '0'): 'q3', ('q4', '1'): 'q5',
            ('q5', '0'): 'q4', ('q5', '1'): 'q3'
        },
        start_state='q0',
        accept_states={'q3'}
    )
    min_dfa = minimize_dfa(dfa_min)
    print(f"Minimized DFA accepts '0011': {min_dfa.process_input('0011')}")  # True

if __name__ == "__main__":
    main()