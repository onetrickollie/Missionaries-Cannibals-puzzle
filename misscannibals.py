from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        '''
            This init function gives the default for 3-tuple when called.
            Rather than using (3,3,L) or R, we are using a boolean onLeft.
            if onLeft is true its on the left, if not then right.
        '''
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

# TODO
# [X] Constructor/init: (Given by prof.)
# [X] method: goal_test(state) (Jahn)
# [ ] method: result(state, action) -> returns new state
#     reached from the given state and action
# [ ] method: actions(state) return a list of valid actions given state
# [!] Prof says implement them in order and test all the output in driver function

# CODE GOES BELOW HERE

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

def result(state):
    ...
    return NotImplementedError

"""
Example: EightPuzzle Problem's .result() method:
    def result(self, state, action):
        Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state 

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)
"""

def actions(self,state):
    #define tuple
    m,c, onLeft = state
    #define action list
    actions = []

    if onLeft:
        if m >= 2:
            actions.append('MM')
        if m >= 1 and c >= 1:
            actions.append('MC')
        if c >= 2:
            actions.append('CC')
        if m >= 1:
            actions.append('M')
        if c >= 1:
            actions.append('C')
    else:
        if (self.M - m) >= 2:
            actions.append('MM')
        if (self.M - m) >= 1 and (self.C - c) >= 1:
            actions.append('MC')
        if (self.C - c) >= 2:
            actions.append('CC')
        if (self.M - m) >= 1:
            actions.append('M')
        if (self.C - c) >= 1:
            actions.append('C')
    return actions

"""
Example: EightPuzzle Problem's .action() method:
    def actions(self, state):
        Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions
"""

'''
"MAIN" FUNCTION
    Put functions to test output here
    Uncomment DF Graph and BF Graph and compare output
'''
if __name__ == '__main__':
    # Initialize 3-tuple initial state of (3,3, True) into an mc object.
    mc = MissCannibals(M=3,C=3)


    # Test action function
    #
    # print(mc.actions((3, 2, True)))
    # Expected Output: ['CC', 'C', 'M']

    # Test DFGS and BFGS on the mc object.
	path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
    # Example Output: ['MC', 'M', 'CC', 'C', 'MM', 'MC', 'MM', 'C', 'CC', 'M', 'MC']

