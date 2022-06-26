import numpy as np
from env import actions,  State, width, length, is_terminal_state, do_action, reward
from e_greedy import e_greedy_policy as policy

Q_table = dict()

def getQ(s, a):
    if((s.pos.x, s.pos.y, a) in Q_table):
        return Q_table[(s.pos.x, s.pos.y, a)]
    else:
        return 0
    # a_index = actions.map_to_id(a)
    # return Q_table[s.pos.x+1, s.pos.y, a_index]

def setQ(s, a, new_q):
    Q_table[(s.pos.x, s.pos.y, a)] = new_q
    # a_index = actions.map_to_id(a)
    # Q_table[s.pos.x+1, s.pos.y, a_index] = new_q
        
# def init_Q_table():    
    # Q_table = np.zeros((width+2, length, actions.count)) # available states (invalid ones also)

def sarsa(alpha_learning_rate, epsilon_propability_of_best, gamma_discount_rate, num_of_episodes):
    for _ in range(num_of_episodes):
        s = State.get_init_state() # initial state
        a = policy(epsilon_propability_of_best, actions.get_available_actions, s, getQ) # initial action based on state
        
        is_terminal = False
        while not is_terminal:
            new_s, reward = do_action(a, s)
            new_a = policy(epsilon_propability_of_best, actions.get_available_actions, new_s, getQ)
            new_q = getQ(s, a) + alpha_learning_rate*(reward + gamma_discount_rate*getQ(new_s, new_a) - getQ(s, a))
            setQ(s, a, new_q)
            
            # print(f'{s.pos.x}, {s.pos.y}')
            is_terminal, _ = is_terminal_state(new_s)
            # if (is_terminal):
                # print('new episode')
            s = new_s
            a = new_a


def printQ():
    for (s,a) in Q_table.keys():
        if Q_table[(s,a)] != 0:
            print(f'{s.pos.x}, {s.pos.y} -> {a} = {Q_table[(s,a)]}')

def measure():
    max_y = np.max([s.pos.y for s,a in Q_table.keys()])
    print(max_y)

def printQ_v2():
    for a in actions.get_available_actions(State.get_init_state()):
        print(a)
        for y in range(length):
            for x in range(width):
                q = getQ(State(x, y), a)
                print(f'{q}, ', end='')
            print()
        
sarsa(0.1, 0.1, 0.9, 100000)
printQ_v2()
# measure()
# printQ()