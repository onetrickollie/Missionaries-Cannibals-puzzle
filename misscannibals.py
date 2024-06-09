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

        new_state[2] = not isLeft # convert the last element back into a True/False value rather than 0/1

        return tuple(new_state)

    def actions(self, state):
        """
        1. unpack tuple
        2. define actions list
        3. remove actions based on invalid moves
        """
        m, c, onLeft = state
        possible_actions = ['MM', 'MC', 'CC', 'C', 'M']

        if onLeft:
            if m != 2 and c != 1:
                possible_actions.remove('MM')
                # if M < 2 you have insufficient M's
                # if M is > 2 he will be outnumbered post-move, unless there is one C.
            if m > c:
                possible_actions.remove('MC')
                # if M < C on LEFT, there MUST be at least one c on RIGHT. (ex. 3 2 L implies 1 C on RIGHT)
                # therefore moving MC will leave the M's outnumbered on RIGHT due to the extra C on RIGHT.
            if c < 2:
                possible_actions.remove('CC')
            if c < 1:
                possible_actions.remove('C')
            if m < 1 or c == m:
                possible_actions.remove('M')
        else:
            if m > 1:
                possible_actions.remove('MM')
                # if M < 1, there is either 1 on RIGHT or 0 on RIGHT--insufficient.
            if m > 2 or c > 2 or c > m:
                possible_actions.remove('MC')
                # if M or C is 3, there are no M/C's on RIGHT to move LEFT.
                # c > m accounts for state of 0 1 R, because moving to 1 2 L would be invalid
            if c > 1:
                # if C < 1, there is either 1 on RIGHT or 0 on RIGHT--insufficient.
                possible_actions.remove('CC')
            if c > 2:
                possible_actions.remove('C')
                # insufficient C's on RIGHT if 3 on LEFT
            if m > 2:
                possible_actions.remove('M')
                # insufficient M's on RIGHT if 3 on LEFT

        return possible_actions


if __name__ == '__main__':
    # Initialize 3-tuple initial state of (3,3, True) into a mc object.
    mc = MissCannibals(3,3)

    # Test result
    print(f"\nresult((3,3,True), 'MC') -> '((2,2,False))': {mc.result(mc.initial, 'MC')}")
    print(f"result((3,3,True), 'CC') -> '((3,1,False))': {mc.result(mc.initial, 'CC')}")
    print(f"result((3,3,True), 'C') -> '((3,2,False))': {mc.result(mc.initial, 'C')}")

    # Test goal_state
    test_state_fail = (3,3,True)
    test_state_win = (0,0, False)
    print(f"\ngoal_test(3,3,True) -> 'False': {mc.goal_test(test_state_fail)}")
    print(f"goal_test(0,0, False) -> 'True': {mc.goal_test(test_state_win)}")

    # Test action
    print(f"\naction((3, 3, True) -> ['MC', 'CC', 'C']: {mc.actions((3, 3, True))}")
    print(f"action((3, 2, True) -> ['CC', 'C', 'M']: {mc.actions((3, 2, True))}")
    print(f"action((3, 0, False) -> ['CC', 'C']: {mc.actions((3, 0, False))}")

    # Test DFGS and BFGS on the mc object.
    path = depth_first_graph_search(mc).solution()
    print(f"\nDepth-First-Graph-Search: {path}")
    path = breadth_first_graph_search(mc).solution()
    print(f"Breadth-First-Graph-Search: {path}")


