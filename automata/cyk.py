from typing import Set, Dict, Tuple, List
from .cfg import CFG

def cyk_parse(cfg: CFG, input_string: str) -> bool:
    if not input_string:
        return () in cfg.productions.get(cfg.start_symbol, [])
    
    n = len(input_string)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        if input_string[i] not in cfg.terminals:
            return False
        for variable in cfg.variables:
            if (input_string[i],) in cfg.productions.get(variable, []):
                table[i][i].add(variable)
    
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            for split in range(start, end):
                for A in cfg.variables:
                    for B, C in cfg.productions.get(A, []):
                        if len(B) == 1:
                            continue
                        if B in table[start][split] and C in table[split + 1][end]:
                            table[start][end].add(A)
    
    return cfg.start_symbol in table[0][n - 1]