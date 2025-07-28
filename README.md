# Automata Library

**Automata Library** is a Python package for exploring and implementing core concepts in Automata Theory and Formal Languages. It provides a modular, type-hinted, and well-documented set of classes and algorithms for working with Deterministic Finite Automata (DFA), Nondeterministic Finite Automata (NFA), Pushdown Automata (PDA), Moore and Mealy Machines, Turing Machines, and Context-Free Grammars (CFGs). The library includes advanced features like DFA minimization, NFA-to-DFA conversion, CFG-to-Chomsky Normal Form (CNF) transformation, and CYK parsing. Designed for educational and research purposes, it offers a robust foundation for studying computational models, with comprehensive unit tests and a clean, reusable API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AliOding12/automata_library.git
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
from automata.dfa import DFA

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

- **DFA**: Process strings with deterministic finite automata.
- **NFA**: Handle nondeterministic automata with ε-transitions.
- **PDA**: Parse context-free languages using a stack.
- **Moore/Mealy Machines**: Generate outputs based on states or transitions.
- **Turing Machine**: Simulate general computation with a single-tape model.
- **CFG**: Define and convert context-free grammars to Chomsky Normal Form.
- **CYK Parsing**: Parse strings for CFGs in CNF.
- **DFA Minimization**: Reduce DFA states while preserving the language.
- **Conversions**: Transform NFA to DFA and CFG to CNF.

## Project Structure

```
automata_library/
├── automata/
│   ├── __init__.py
│   ├── dfa.py
│   ├── nfa.py
│   ├── pda.py
│   ├── moore_machine.py
│   ├── mealy_machine.py
│   ├── turing_machine.py
│   ├── cfg.py
│   ├── cyk.py
│   ├── dfa_minimization.py
│   ├── tools.py
├── tests/
│   ├── __init__.py
│   ├── test_dfa.py
│   ├── test_nfa.py
│   ├── test_moore.py
│   ├── test_mealy.py
│   ├── test_dfa_minimization.py
│   ├── conftest.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
└── .gitignore
```

## Testing

Run unit tests using pytest to verify the library's functionality:
```bash
pip install pytest pytest-cov
pytest tests/ --cov=automata
```

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub. Ensure code follows PEP 8 and includes tests.

## License

MIT License. See `LICENSE` for details.

## Contact

For questions or feedback, contact ME(Abbas) at abbasali1214313@gmail.com.