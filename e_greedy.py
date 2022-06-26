import numpy as np

def e_greedy_policy(epsilon_propability_of_choosing_greedy, get_available_actions, current_state, get_Q):
    p = np.random.random()
    if p < epsilon_propability_of_choosing_greedy:
        av_actions = get_available_actions(current_state)
        best_a_index = np.argmax([get_Q(current_state, a) for a in av_actions])
        return av_actions[best_a_index] # exploatation (greedy)
    else:
        av_actions = get_available_actions(current_state)
        random_a = np.random.choice(av_actions)
        return random_a # exploration
        
      
          