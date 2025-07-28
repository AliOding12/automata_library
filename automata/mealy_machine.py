from typing import Set, Dict, Tuple, List

class MealyMachine:
    def __init__(self, states: Set[str], input_alphabet: Set[str], output_alphabet: Set[str],
                 transition: Dict[Tuple[str, str], str], output: Dict[Tuple[str, str], str],
                 start_state: str):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transition = transition
        self.output = output
        self.start_state = start_state

    def process_input(self, input_string: str) -> tuple[bool, List[str]]:
        current_state = self.start_state
        output_sequence = []

        for symbol in input_string:
            if symbol not in self.input_alphabet:
                return False, []
            next_state = self.transition.get((current_state, symbol), None)
            output_symbol = self.output.get((current_state, symbol), None)
            if next_state is None or output_symbol is None:
                return False, []
            current_state = next_state
            output_sequence.append(output_symbol)

        return True, output_sequence