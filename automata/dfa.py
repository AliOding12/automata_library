from typing import Set, Dict, Tuple

class DFA:
    def __init__(self, states: Set[str], alphabet: Set[str], transition: Dict[Tuple[str, str], str],
                 start_state: str, accept_states: Set[str]):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accept_states = accept_states

    def process_input(self, input_string: str) -> bool:
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transition.get((current_state, symbol), None)
            if current_state is None:
                return False
        return current_state in self.accept_states