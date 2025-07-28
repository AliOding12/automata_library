import pytest
from automata.moore_machine import MooreMachine

def test_moore_parity_ones():
    """Test Moore Machine that outputs 'E' for even 1s, 'O' for odd."""
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
    assert valid is True
    assert output == ['E', 'O', 'E', 'E']
    
    valid, output = moore.process_input("111")
    assert valid is True
    assert output == ['E', 'O', 'E', 'O']
    
    valid, output = moore.process_input("")
    assert valid is True
    assert output == ['E']
    
    valid, output = moore.process_input("11x")
    assert valid is False
    assert output == []