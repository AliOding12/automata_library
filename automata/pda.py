from typing import Set, Dict, Tuple, List

class PDA:
    def __init__(self, states: Set[str], input_alphabet: Set[str], stack_alphabet: Set[str],
                 transition: Dict[Tuple[str, str, str], List[Tuple[str, str]]],
                 start_state: str, start_stack_symbol: str, accept_states: Set[str]):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transition = transition
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

    def process_input(self, input_string: str) -> bool:
        stack = [self.start_stack_symbol]
        current_state = self.start_state
        input_index = 0

        def process(current_state: str, stack: List[str], input_index: int) -> bool:
            if input_index == len(input_string) and not stack:
                return True
            current_input = input_string[input_index] if input_index < len(input_string) else ''
            stack_top = stack[-1] if stack else ''
            
            for input_symbol in {current_input, ''}:
                if (current_state, input_symbol, stack_top) in self.transition:
                    for next_state, stack_op in self.transition[(current_state, input_symbol, stack_top)]:
                        new_stack = stack.copy()
                        if stack_op != '':
                            new_stack.pop()
                            new_stack.extend(reversed(stack_op))
                        elif stack:
                            new_stack.pop()
                        new_index = input_index + 1 if input_symbol else input_index
                        if process(next_state, new_stack, new_index):
                            return True
            return False

        return process(current_state, stack, input_index)