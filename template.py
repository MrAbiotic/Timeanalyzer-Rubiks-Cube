import numpy as np

class Template:
    def __init__(self, split_num=1, split_goals=[1], solve_time=15):
        self.split_num = split_num
        self.split_sum = sum(self.split_goals)

        # Creates splits from percentage
        self.split_goals = np.array(split_goals)/np.linalg.norm(np.array(split_goals))*solve_time
