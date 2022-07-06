# Actions

class Action:
    left = 'left'
    right = 'right'
    straight = 'straight'
    
    count = 3
    
    def __init__(self, rotation):
        match rotation:
            case self.map_to_signal(Action.left):
                self.value = Action.left
            case self.map_to_signal(Action.right):
                self.value = Action.right
            case self.map_to_signal(Action.straight):
                self.value = Action.straight

    def get_available_actions(state):
        return [Action.left, Action.right, Action.straight] # here every action is available in every state, but it not always is the case

    def map_to_id(action):
        a_id = -1
        match action:
            case Action.left:
                a_id = 0
            case Action.right:
                a_id = 1
            case Action.straight:
                a_id = 2
        return a_id
    
    def map_to_signal(action):
        match action:
            case Action.left:
                a_id = -1
            case Action.right:
                a_id = 0
            case Action.straight:
                a_id = 1
        return a_id

# State

class State:
        def __init__(self, distances):
            self.distances = distances # start at x,y = 0,0
        
        def get_init_state():
            return State([0 for _ in range(9)]) # start at center on x and 0 on y)
            
        def copy_of(state):
            return State(state.distances)
        
        def to_tuple(self):
            return tuple(self.distances)
            
        # def add(state, dx, dy):
        #     return State(state.pos.x + dx, state.pos.y + dy)
        
# Methods

def is_terminal_state(state):
    pass # TODO implement in unity

    # if (state.pos.x < 0 or state.pos.x > width-1):
    #     return (True, 'fail')
    # elif (state.pos.y > length):
    #     return (True, 'win')
    # else: 
    #     return (False, '')

def do_action(action, current_state):
    pass # TODO implement in unity

    # dx = 0
    # match action:
    #     case actions.left:
    #         dx = -1
    #     case actions.right:
    #         dx = 1
            
    # next_state = State.add(current_state, dx, dy=1)
    
    # r = reward(current_state, action, next_state)
    # return next_state, r

def reward(state, action, next_state):
    pass # TODO implement in unity

#     is_terminal, episode_result = is_terminal_state(next_state)
#     if (is_terminal == False):
#         return 0
    
#     if episode_result == 'win':
#         return 100
    
#     if episode_result == 'fail':
#         return -100