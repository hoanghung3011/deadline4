import numpy as np
import copy
class puzzle_state:
    def __init__(self, state):
        self.state = np.asarray(state)
        self.pos_map = {}

        self.state_mapping()
    def state_mapping(self):
        for idx_x, row in enumerate(self.state):
            for idx_y, element in enumerate(row):
                self.pos_map[element] = [idx_x,idx_y]
    def __gt__(self, other):
        return (self.state > other.state).all()
    def __lt__(self, other):
        return (self.state < other.state).all()
    def __eq__(self, other):
        return (self.state == other.state).all()
    def __ne__(self, other):
        if other == None:
            return (self.state != None).all
        return (self.state != other.state).all()
def move_left(current_state):
    next_state = current_state
    zero_idx = next_state.pos_map[0]
    if zero_idx[1] > 0:    
        next_state.state[zero_idx[0],zero_idx[1]], next_state.state[zero_idx[0], zero_idx[1]-1] = next_state.state[zero_idx[0],zero_idx[1]-1], next_state.state[zero_idx[0], zero_idx[1]]
        next_state.state_mapping()
        return next_state
    return None
def move_right(current_state):
    next_state = current_state
    zero_idx = next_state.pos_map[0]
    if zero_idx[1] < 2:    
        next_state.state[zero_idx[0],zero_idx[1]], next_state.state[zero_idx[0], zero_idx[1]+1] = next_state.state[zero_idx[0],zero_idx[1]+1], next_state.state[zero_idx[0], zero_idx[1]]
        next_state.state_mapping()
        return next_state
    return None
def move_up(current_state):
    next_state = current_state
    zero_idx = next_state.pos_map[0]
    if zero_idx[0] > 0:    
        next_state.state[zero_idx[0]-1,zero_idx[1]], next_state.state[zero_idx[0], zero_idx[1]] = next_state.state[zero_idx[0],zero_idx[1]], next_state.state[zero_idx[0]-1, zero_idx[1]]
        next_state.state_mapping()
        return next_state
    return None
def move_down(current_state):
    next_state = current_state
    zero_idx = next_state.pos_map[0]
    if zero_idx[0] < 2 :    
        next_state.state[zero_idx[0],zero_idx[1]], next_state.state[zero_idx[0]+1, zero_idx[1]] = next_state.state[zero_idx[0]+1,zero_idx[1]], next_state.state[zero_idx[0], zero_idx[1]]
        next_state.state_mapping()
        return next_state
    return None
operator_set=[move_up,move_down,move_left,move_right]