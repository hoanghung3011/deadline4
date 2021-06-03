import numpy as np
import puzzle_state as ps 

class slide_puzzle:
    def __init__(self, input_file):
        self.input_file = input_file
        entry_file = open(self.input_file)
        lines = entry_file.readlines()
        tmp_list = []
        self.size = int(lines[0])
        self.inversion_count = 0

        for idx in range(1,4):
            tmp_list.append(list(map(int,lines[idx].split())))
        self.initial_state = ps.puzzle_state(tmp_list)
        tmp_list.clear()
        for idx in range(5,8):
            tmp_list.append(list(map(int,lines[idx].split())))
        self.goal_state = ps.puzzle_state(tmp_list)
    def is_solvable(self):
        self.inversion_count = 0
        temp1 = self.initial_state.state.ravel()
        temp2 = self.goal_state.state.ravel()
        return self.parity_check(temp1) == self.parity_check(temp2)
            
    @staticmethod
    def parity_check(arr):
        inversion_count = 0
        tmp = np.setdiff1d(arr,np.array([0]))
        for i in range(tmp.size):
            for j in range(i, tmp.size):
                if j+1 < tmp.size:
                    if tmp[j] <= tmp[j+1]:
                        break
                    else:
                        tmp[j+1], tmp[j] = tmp[j], tmp[j+1]
                        inversion_count += 1 
        return inversion_count%2
#-----------------------------------------------------------------------------------------------
def mahattan_distance(point_a, point_b):
    return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])
def heuristic_func(current_state, final_state):
    total_heu = 0
    for pos, idx in current_state.pos_map.items():
        total_heu += mahattan_distance(idx, final_state.pos_map[pos])
    return total_heu
#-----------------------------------------------------------------------------------------------
