import pytest
from automata.mealy_machine import MealyMachine

def test_mealy_output_identity():
    """Test Mealy Machine that outputs '1' for input '1', '0' otherwise."""
    mealy = MealyMachine(
        states={'q0'},
        input_alphabet={'0', '1'},
        output_alphabet={'0', '1'},
        transition={('q0', '0'): 'q0', ('q0', '1'): 'q0'},
        output={('q0', '0'): '0', ('q0', '1'): '1'},
        start_state='q0'
    )
    valid, output = mealy.process_input("110")
    assert valid is True
    assert output == ['1', '1', '0']
    
    valid, output = mealy.process_input("111")
    assert valid is True
    assert output == ['1', '1', '1']
    
    valid, output = mealy.process_input("")
    assert valid is True
    assert output == []
    
    valid, output = mealy.process_input("11x")
    assert valid is False
    assert output == []