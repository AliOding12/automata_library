# Automata Library

A Python library for Automata Theory and Formal Languages, implementing core concepts such as DFA, NFA, PDA, Moore and Mealy Machines, Turing Machines, CFG, CYK parsing, DFA minimization, and conversions (NFA-to-DFA, CFG-to-CNF).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automata_library.git
   cd automata_library
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the library:
   ```bash
   pip install .
   ```

## Usage

Run the demo script to see examples of all implemented automata:
```bash
python main.py
```

Example usage in Python:
```python
from automata import DFA

dfa = DFA(
    states={'q0', 'q1'},
    alphabet={'0', '1'},
    transition={('q0', '0'): 'q1', ('q0', '1'): 'q0', ('q1', '0'): 'q0', ('q1', '1'): 'q1'},
    start_state='q0',
    accept_states={'q0'}
)
print(dfa.process_input("00"))  # True
```

## Features

- DFA: Process strings with deterministic finite automata.
- NFA: Handle nondeterministic automata with ε-transitions.
- PDA: Parse context-free languages with a stack.
- Moore/Mealy Machines: Generate outputs based on states or transitions.
- Turing Machine: Simulate general computation.
- CFG: Define and convert context-free grammars to Chomsky Normal Form.
- CYK: Parse strings for CFGs in CNF.
- DFA Minimization: Reduce DFA states while preserving the language.
- Conversions: NFA-to-DFA and CFG-to-CNF.

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## License

MIT License. See `LICENSE` for details.