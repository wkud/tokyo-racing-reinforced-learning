from tkinter import Y


class actions:
    left = 'left'
    right = 'right'
    straight = 'straight'
    
width = 3
length = 100


def init_state():
    class State:
        def __init__(self):
            self.pos = Position(int(width/2), 0) # start at center on x and 0 on y
    class Position:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    s0 = State()
    
    return s0 # initial state

state = init_state()


def is_terminal_state(state):
    if (state.x < 0 or state.x > width-1):
        return (True, 'fail')
    elif (state.pos.y > length):
        return (True, 'win')
    else: 
        return (False, '')

def step(action):
    match action:
        case actions.left:
            state.pos.x -= 1
        case actions.right:
            state.pos.x += 1
    
    state.pos.y += 1
    return state

def reward(state, action):
    if state.pos.x == 0 and action == actions.left:
        return -100
    
    if state.pos.x == width-1 and action == actions.right:
        return -100
    
    if state.pos.y == 99:
        return 100
    
    