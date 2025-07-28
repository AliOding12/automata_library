from typing import Set, Dict, Tuple
from collections import defaultdict

class NFA:
    def __init__(self, states: Set[str], alphabet: Set[str], transition: Dict[Tuple[str, str], Set[str]],
                 start_state: str, accept_states: Set[str], epsilon: str = 'ε'):
        """Initialize an NFA."""
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accept_states = accept_states
        self.epsilon = epsilon

    def epsilon_closure(self, states: Set[str]) -> Set[str]:
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in self.transition.get((state, self.epsilon), set()):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def process_input(self, input_string: str) -> bool:
        current_states = self.epsilon_closure({self.start_state})
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            next_states = set()
            for state in current_states:
                next_states.update(self.transition.get((state, symbol), set()))
            current_states = self.epsilon_closure(next_states)
        return bool(current_states & self.accept_states)