import pytest
from automata.dfa import DFA

def test_dfa_even_zeros():
    """Test DFA that accepts strings with an even number of 0s."""
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
    assert dfa.process_input("00") is True
    assert dfa.process_input("0000") is True
    assert dfa.process_input("01") is False
    assert dfa.process_input("001") is False
    assert dfa.process_input("") is True  # Empty string has 0 zeros (even)
    assert dfa.process_input("11") is True  # No zeros is even
    assert dfa.process_input("0x") is False  # Invalid symbol

def test_dfa_invalid_transition():
    """Test DFA with an incomplete transition function."""
    dfa = DFA(
        states={'q0', 'q1'},
        alphabet={'0', '1'},
        transition={('q0', '0'): 'q1'},
        start_state='q0',
        accept_states={'q1'}
    )
    assert dfa.process_input("1") is False  # No transition for '1' from q0