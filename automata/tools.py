from typing import Set, Dict, Tuple, List
from collections import defaultdict
from .cfg import CFG
from .dfa import DFA
from .nfa import NFA

def cfg_to_cnf(cfg: CFG) -> CFG:
    """Convert a CFG to Chomsky Normal Form."""
    new_start = f"{cfg.start_symbol}0"
    variables = cfg.variables | {new_start}
    productions = defaultdict(list, {k: v[:] for k, v in cfg.productions.items()})
    productions[new_start] = [(cfg.start_symbol,)]
    
    nullable = set()
    for var in variables:
        if () in productions.get(var, []):
            nullable.add(var)
    for var in variables:
        new_prods = []
        for prod in productions[var]:
            if prod and all(s in nullable for s in prod):
                new_prods.append(())
            new_prods.append(prod)
        productions[var] = new_prods
    for var in variables:
        new_prods = []
        for prod in productions[var]:
            if not prod:
                continue
            subsets = [[]]
            for s in prod:
                new_subsets = []
                for subset in subsets:
                    new_subsets.append(subset + [s])
                    if s in nullable:
                        new_subsets.append(subset)
                subsets = new_subsets
            new_prods.extend(tuple(subset) for subset in subsets if subset)
        productions[var] = new_prods

    unit_prods = defaultdict(set)
    for var in variables:
        to_check = {var}
        seen = set()
        while to_check:
            v = to_check.pop()
            if v in seen:
                continue
            seen.add(v)
            for prod in productions.get(v, []):
                if len(prod) == 1 and prod[0] in variables:
                    unit_prods[var].add(prod[0])
                    to_check.add(prod[0])
    for var in variables:
        new_prods = []
        for prod in productions[var]:
            if len(prod) == 1 and prod[0] in variables:
                continue
            new_prods.append(prod)
        for unit_var in unit_prods[var]:
            new_prods.extend(productions[unit_var])
        productions[var] = list(set(new_prods))

    new_variables = set()
    new_productions = defaultdict(list)
    term_to_var = {}
    var_counter = 0

    for var in variables:
        for prod in productions[var]:
            if len(prod) == 1 and prod[0] in cfg.terminals:
                new_productions[var].append(prod)
            elif len(prod) <= 2:
                new_productions[var].append(prod)
            else:
                current_var = var
                for i in range(len(prod) - 2):
                    new_var = f"X{var_counter}"
                    var_counter += 1
                    new_variables.add(new_var)
                    new_productions[current_var].append((prod[i], new_var))
                    current_var = new_var
                new_productions[current_var].append((prod[-2], prod[-1]))

    for var in variables | new_variables:
        for prod in new_productions[var]:
            if len(prod) == 2:
                new_prod = []
                for s in prod:
                    if s in cfg.terminals:
                        if s not in term_to_var:
                            term_to_var[s] = f"T{var_counter}"
                            var_counter += 1
                            new_variables.add(term_to_var[s])
                            new_productions[term_to_var[s]] = [(s,)]
                        new_prod.append(term_to_var[s])
                    else:
                        new_prod.append(s)
                new_productions[var].append(tuple(new_prod))
        new_productions[var] = list(set(new_productions[var]))

    return CFG(variables | new_variables, cfg.terminals, new_productions, new_start)

def nfa_to_dfa(nfa: NFA) -> DFA:
    """Convert NFA to DFA using subset construction."""
    dfa_states = set()
    dfa_transition = {}
    dfa_accept_states = set()
    state_map = {}
    worklist = [nfa.epsilon_closure({nfa.start_state})]
    dfa_start = frozenset(nfa.epsilon_closure({nfa.start_state}))
    state_counter = 0

    while worklist:
        current = worklist.pop(0)
        current_name = state_map.get(frozenset(current), f"q{state_counter}")
        if current_name not in state_map.values():
            state_map[frozenset(current)] = current_name
            state_counter += 1
            dfa_states.add(current_name)
            if current & nfa.accept_states:
                dfa_accept_states.add(current_name)

        for symbol in nfa.alphabet:
            next_states = set()
            for state in current:
                next_states.update(nfa.transition.get((state, symbol), set()))
            next_closure = nfa.epsilon_closure(next_states)
            if next_closure:
                next_name = state_map.get(frozenset(next_closure), f"q{state_counter}")
                if next_name not in state_map.values():
                    state_map[frozenset(next_closure)] = next_name
                    state_counter += 1
                    worklist.append(next_closure)
                    dfa_states.add(next_name)
                    if next_closure & nfa.accept_states:
                        dfa_accept_states.add(next_name)
                dfa_transition[(current_name, symbol)] = next_name

    return DFA(dfa_states, nfa.alphabet, dfa_transition, state_map[dfa_start], dfa_accept_states)