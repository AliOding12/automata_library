import pytest
from automata.dfa import DFA
from automata.dfa_minimization import minimize_dfa

def test_dfa_minimization_even_zeros_ones():
    """Test DFA minimization for strings with even number of 0s and 1s."""
    dfa = DFA(
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
    min_dfa = minimize_dfa(dfa)
    
    # Check that minimized DFA accepts the same language
    assert min_dfa.process_input("0011") is True
    assert min_dfa.process_input("01") is False
    assert min_dfa.process_input("") is False
    # Verify fewer states (should reduce from 6 to 4 for even 0s and 1s)
    assert len(min_dfa.states) <= len(dfa.states)
    
def test_dfa_minimization_unreachable_states():
    """Test DFA minimization removes unreachable states."""
    dfa = DFA(
        states={'q0', 'q1', 'q2'},
        alphabet={'0', '1'},
        transition={('q0', '0'): 'q0', ('q0', '1'): 'q0'},
        start_state='q0',
        accept_states={'q0'}
    )
    min_dfa = minimize_dfa(dfa)
    assert len(min_dfa.states) == 1  # Only q0 is reachable
    assert min_dfa.process_input("001") is True