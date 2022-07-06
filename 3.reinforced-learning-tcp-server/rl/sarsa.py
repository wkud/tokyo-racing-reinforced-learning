import numpy as np
from rl.env_unity import Action,  State, is_terminal_state, do_action
from rl.e_greedy import e_greedy_policy as policy
from rl.q_table import getQ, setQ

class Sarsa:
    def __init__(self, alpha_learning_rate, epsilon_propability_of_best, gamma_discount_rate):
        self.alpha_learning_rate = alpha_learning_rate
        self.epsilon_propability_of_best = epsilon_propability_of_best
        self.gamma_discount_rate = gamma_discount_rate
        
    def initialize(self):
        self.s = State.get_init_state() # initial state
        self.a = policy(self.epsilon_propability_of_best, Action.get_available_actions, self.s, getQ) # initial action based on state
        
    def predict_and_learn(self, reward, new_s):
        new_a = policy(self.epsilon_propability_of_best, Action.get_available_actions, new_s, getQ)
        new_q = getQ(self.s, self.a) + self.alpha_learning_rate*(reward + self.gamma_discount_rate*getQ(new_s, new_a) - getQ(self.s, self.a))
        setQ(self.s, self.a, new_q)
        
        # is_terminal, _ = is_terminal_state(new_s)
        self.s = new_s
        self.a = new_a
        
        return new_a
        # break loop if is_terminal
        
    def sarsa_static(alpha_learning_rate, epsilon_propability_of_best, gamma_discount_rate, num_of_episodes):
        for _ in range(num_of_episodes):
            s = State.get_init_state() # initial state
            a = policy(epsilon_propability_of_best, Action.get_available_actions, s, getQ) # initial action based on state
            
            is_terminal = False
            while not is_terminal:
                new_s, reward = do_action(a, s)
                new_a = policy(epsilon_propability_of_best, Action.get_available_actions, new_s, getQ)
                new_q = getQ(s, a) + alpha_learning_rate*(reward + gamma_discount_rate*getQ(new_s, new_a) - getQ(s, a))
                setQ(s, a, new_q)
                
                is_terminal, _ = is_terminal_state(new_s)

                s = new_s
                a = new_a
    
# def printQ():
#     for (s,a) in Q_table.keys():
#         if Q_table[(s,a)] != 0:
#             print(f'{s.pos.x}, {s.pos.y} -> {a} = {Q_table[(s,a)]}')

# def measure():
#     max_y = np.max([s.pos.y for s,a in Q_table.keys()])
#     print(max_y)

# def printQ_v2():
#     for a in actions.get_available_actions(State.get_init_state()):
#         print(a)
#         for y in range(length):
#             for x in range(width):
#                 q = getQ(State(x, y), a)
#                 print(f'{q}, ', end='')
#             print()
        
# sarsa_static(0.1, 0.1, 0.9, 100000)

# printQ_v2()
# measure()
# printQ()