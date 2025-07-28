from typing import Set, Dict, Tuple, List

class CFG:
    def __init__(self, variables: Set[str], terminals: Set[str], 
                 productions: Dict[str, List[Tuple[str, ...]]], start_symbol: str):
        self.variables = variables
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol