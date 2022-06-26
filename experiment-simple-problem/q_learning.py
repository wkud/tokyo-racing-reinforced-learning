from re import S
import numpy as np
from env import actions,  State, width, length, is_terminal_state, do_action, reward
from e_greedy import e_greedy_policy as policy
from q_table import Q_table, getQ, setQ

def qlearn(alpha_learning_rate, epsilon_propability_of_best, gamma_discount_rate, num_of_episodes):
    for _ in range(num_of_episodes):
        s = State.get_init_state() # initial state
        
        is_terminal = False
        while not is_terminal:
            a = policy(epsilon_propability_of_best, actions.get_available_actions, s, getQ) # initial action based on state
            new_s, reward = do_action(a, s)
            
            max_q_value_of_available_actions = np.max([getQ(new_s, a) for a in actions.get_available_actions(new_s)])
            new_q = getQ(s, a) + alpha_learning_rate*(reward + gamma_discount_rate*max_q_value_of_available_actions - getQ(s, a))
            setQ(s, a, new_q)
            
            # print(f'{s.pos.x}, {s.pos.y}')
            is_terminal, _ = is_terminal_state(new_s)
            # if (is_terminal):
            #     print('new episode')
                
            s = new_s

def printQ_v2():
    for a in actions.get_available_actions(State.get_init_state()):
        print(a)
        for y in range(length):
            for x in range(width):
                q = getQ(State(x, y), a)
                print(f'{q}, ', end='')
            print()
        
qlearn(0.1, 0.1, 0.9, 100000)
printQ_v2()