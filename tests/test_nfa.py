import pytest
from automata.nfa import NFA

def test_nfa_contains_01():
    """Test NFA that accepts strings containing '01' as a substring."""
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
    assert nfa.process_input("01") is True
    assert nfa.process_input("001") is True
    assert nfa.process_input("010") is True
    assert nfa.process_input("00") is False
    assert nfa.process_input("11") is False
    assert nfa.process_input("") is False
    assert nfa.process_input("0x") is False  # Invalid symbol

def test_nfa_epsilon_closure():
    """Test epsilon closure computation."""
    nfa = NFA(
        states={'q0', 'q1', 'q2'},
        alphabet={'0', '1'},
        transition={
            ('q0', 'ε'): {'q1'}, ('q1', 'ε'): {'q2'}
        },
        start_state='q0',
        accept_states={'q2'}
    )
    closure = nfa.epsilon_closure({'q0'})
    assert closure == {'q0', 'q1', 'q2'}