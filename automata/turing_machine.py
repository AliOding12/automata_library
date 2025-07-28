from typing import Set, Dict, Tuple
from collections import defaultdict

class TuringMachine:
    def __init__(self, states: Set[str], input_alphabet: Set[str], tape_alphabet: Set[str],
                 transition: Dict[Tuple[str, str], Tuple[str, str, str]],
                 start_state: str, accept_state: str, reject_state: str, blank_symbol: str = '_'):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet | {blank_symbol}
        self.transition = transition
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def process_input(self, input_string: str, max_steps: int = 1000) -> tuple[bool, str]:
        tape = defaultdict(lambda: self.blank_symbol)
        for i, symbol in enumerate(input_string):
            if symbol not in self.input_alphabet:
                return False, ""
            tape[i] = symbol
        
        current_state = self.start_state
        head_position = 0
        steps = 0

        while steps < max_steps:
            if current_state == self.accept_state:
                min_pos = min(i for i in tape if tape[i] != self.blank_symbol)
                max_pos = max(i for i in tape if tape[i] != self.blank_symbol)
                tape_content = ''.join(tape[i] for i in range(min_pos, max_pos + 1))
                return True, tape_content
            if current_state == self.reject_state:
                return False, ""

            current_symbol = tape[head_position]
            if (current_state, current_symbol) not in self.transition:
                return False, ""

            next_state, write_symbol, direction = self.transition[(current_state, current_symbol)]
            tape[head_position] = write_symbol
            head_position += 1 if direction == 'R' else -1
            current_state = next_state
            steps += 1

        return False, ""