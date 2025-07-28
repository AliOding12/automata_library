from typing import Set, Dict, Tuple
from collections import defaultdict
from .dfa import DFA

def minimize_dfa(dfa: DFA) -> DFA:
    reachable = {dfa.start_state}
    stack = [dfa.start_state]
    while stack:
        state = stack.pop()
        for symbol in dfa.alphabet:
            next_state = dfa.transition.get((state, symbol))
            if next_state and next_state not in reachable:
                reachable.add(next_state)
                stack.append(next_state)
    
    states = dfa.states & reachable
    transition = {(s, a): t for (s, a), t in dfa.transition.items() if s in reachable and t in reachable}
    accept_states = dfa.accept_states & reachable

    partitions = [accept_states, states - accept_states]
    partitions = [p for p in partitions if p]
    worklist = [(p, a) for p in partitions for a in dfa.alphabet]

    while worklist:
        partition, symbol = worklist.pop(0)
        groups = defaultdict(set)
        for state in partition:
            next_state = transition.get((state, symbol), None)
            if next_state:
                for i, p in enumerate(partitions):
                    if next_state in p:
                        groups[i].add(state)
                        break
            else:
                groups[None].add(state)

        for group_idx, group in groups.items():
            if group != partition and group:
                partitions.remove(partition)
                if group:
                    partitions.append(group)
                remaining = partition - group
                if remaining:
                    partitions.append(remaining)
                for new_p in [group, remaining]:
                    if new_p:
                        for a in dfa.alphabet:
                            worklist.append((new_p, a))

    new_states = {f"q{i}" for i in range(len(partitions))}
    new_transition = {}
    new_accept_states = set()
    new_start_state = None

    state_to_new_state = {}
    for i, partition in enumerate(partitions):
        rep_state = f"q{i}"
        for state in partition:
            state_to_new_state[state] = rep_state
            if state == dfa.start_state:
                new_start_state = rep_state
            if state in dfa.accept_states:
                new_accept_states.add(rep_state)

    for (state, symbol), next_state in transition.items():
        new_state = state_to_new_state[state]
        new_next_state = state_to_new_state[next_state]
        new_transition[(new_state, symbol)] = new_next_state

    return DFA(new_states, dfa.alphabet, new_transition, new_start_state, new_accept_states)