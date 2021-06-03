import numpy as np 
from itertools import groupby
import slide_problem as sp 
import puzzle_state as ps
import copy

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)

new_puzzle = sp.slide_puzzle('in.txt')
if not new_puzzle.is_solvable():
    print("Puzzle is not solvable, try different initial state!")
else:
    #print(sp.heuristic_func(new_puzzle.initial_state, new_puzzle.goal_state))
    tmp_queue = []
    tmp_queue.append([(sp.heuristic_func(new_puzzle.initial_state, new_puzzle.goal_state), new_puzzle.initial_state)])
    found_path = []
    extended_list = []
    extended_list.append(new_puzzle.initial_state.state)
    while tmp_queue:
        tmp_start = tmp_queue.pop(0)
        if np.array_equal(tmp_start[-1][1].state,new_puzzle.goal_state.state):
            found_path = [step[1].state for step in tmp_start]
            break
        for operator in ps.operator_set:
            next_state = operator(copy.deepcopy(tmp_start[-1][1]))
            if next_state != None:
                if not arreq_in_list(next_state.state, extended_list):
                        extended_list.append(next_state.state)
                        current_path = copy.deepcopy(tmp_start)
                        heuristic = sp.heuristic_func(next_state, new_puzzle.goal_state)
                        current_path.append([heuristic,next_state])
                        tmp_queue.append(current_path)
                        tmp_queue.sort()
    out_file = open('out.txt', 'w')
    for item in found_path:
        out_file.write('%s\n\n'%item)
    out_file.close()
    