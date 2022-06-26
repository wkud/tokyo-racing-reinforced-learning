# Actions
class actions:
    left = 'left'
    right = 'right'
    straight = 'straight'
    
    count = 3

    def get_available_actions(state):
        return [actions.left, actions.right, actions.straight] # here every action is available in every state, but it not always is the case

    def map_to_id(action):
        a_id = -1
        match action:
            case actions.left:
                a_id = 0
            case actions.right:
                a_id = 1
            case actions.straight:
                a_id = 2
        return a_id
    
# Consts

width = 3
length = 100

# State
class Position:
        def __init__(self, x, y):
            self.x = x
            self.y = y
class State:
        def __init__(self, x, y):
            self.pos = Position(x, y) # start at center on x and 0 on y
        
        def get_init_state():
            return State(int(width/2), 0) # start at center on x and 0 on y)
            
        def copy_of(state):
            return State(state.pos.x, state.pos.y)
        
        def add(state, dx, dy):
            return State(state.pos.x + dx, state.pos.y + dy)
# Methods

def is_terminal_state(state):
    if (state.pos.x < 0 or state.pos.x > width-1):
        return (True, 'fail')
    elif (state.pos.y > length):
        return (True, 'win')
    else: 
        return (False, '')

def do_action(action, current_state):
    dx = 0
    match action:
        case actions.left:
            dx = -1
        case actions.right:
            dx = 1
            
    next_state = State.add(current_state, dx, dy=1)
    
    r = reward(current_state, action, next_state)
    return next_state, r

def reward(state, action, next_state):
    is_terminal, episode_result = is_terminal_state(next_state)
    if (is_terminal == False):
        return 0
    
    if episode_result == 'win':
        return 100
    
    if episode_result == 'fail':
        return -100
    
    # if state.pos.x == 0 and action == actions.left:
    #     return -100
    
    # if state.pos.x == width-1 and action == actions.right:
    #     return -100
    
    # if state.pos.y == 99:
    #     return 100
    
    