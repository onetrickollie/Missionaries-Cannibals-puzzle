from search import *

'''
Program: MissCannibals.py
Date: Thursday, June 6, 2024
Author: Jahn Jamison L. Tibayan, Kai Liu, Sean Jacob Evasco
'''

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def goal_test(self, state):
        """
        Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor.
        """
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def result(self, state, action):
        m, c, isLeft = state
        new_state = [m, c, isLeft]

        delta = {
            'MM': [2, 0, 1],
            'MC': [1, 1, 1],
            'CC': [0, 2, 1],
            'C': [0, 1, 1],
            'M': [1, 0, 1],
        }

        if isLeft:
            new_state = [new_state[i] - delta[action][i] for i in range(len(new_state))]
        else:
            new_state = [new_state[i] + delta[action][i] for i in range(len(new_state))]

        new_state[2] = not isLeft  # convert the last element back into a True/False value rather than 0/1

        return tuple(new_state)

    def actions(self, state):
        """
        This function unpacks the tuple and utilizes the result function to generate the result state
        for every possible action. If that action doesnt result in missionaries being outnumbered on either side,
        as long as m != 0, then the action is appended.
        """
        m, c, onLeft = state
        possible_actions = ['MM', 'MC', 'CC', 'C', 'M']
        valid_actions = []

        for action in possible_actions:
            new_state = self.result(state, action)
            new_m, new_c, new_onLeft = new_state

            if (0 <= new_m <= self.M and 0 <= new_c <= self.C and
                (new_m >= new_c or new_m == 0) and
                ((self.M - new_m) >= (self.C - new_c) or (self.M - new_m) == 0)):
                valid_actions.append(action)

        return valid_actions

if __name__ == '__main__':
    # Initialize 3-tuple initial state of (3,3, True) into a mc object.
    mc = MissCannibals(3,3)

    # Test result
    print(f"\nresult((3, 3, True), 'MC') -> '((2, 2 , False))': {mc.result(mc.initial, 'MC')}")
    print(f"result((3, 3, True), 'CC') -> '((3, 1, False))': {mc.result(mc.initial, 'CC')}")
    print(f"result((3, 3, True), 'C') -> '((3, 2, False))': {mc.result(mc.initial, 'C')}")

    # Test goal_state
    test_state_fail = (3,3,True)
    test_state_win = (0,0, False)
    print(f"\ngoal_test(3, 3, True) -> 'False': {mc.goal_test(test_state_fail)}")
    print(f"goal_test(0, 0, False) -> 'True': {mc.goal_test(test_state_win)}")

    # Test action
    print(f"\naction((3, 3, True) -> ['MC', 'CC', 'C']: {mc.actions((3, 3, True))}")
    print(f"action((3, 2, True) -> ['CC', 'C', 'M']: {mc.actions((3, 2, True))}")
    print(f"action((3, 0, False) -> ['CC', 'C']: {mc.actions((3, 0, False))}")
    print(f"action((1, 1, False) -> ['MM', 'MC']: {mc.actions((1, 1, False))}")

    # Test DFGS and BFGS on the mc object.
    path = depth_first_graph_search(mc).solution()
    print(f"\nDepth-First-Graph-Search: {path}")
    path = breadth_first_graph_search(mc).solution()
    print(f"Breadth-First-Graph-Search: {path}")


