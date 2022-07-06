from rl.sarsa import Sarsa
from rl.env_unity import State, Action
from tcp import Tcp

tcp = Tcp(12880, 5.0)
algorithm = Sarsa(0.1, 0.1, 0.9)

def format_float(f):
    return float("{:.4f}".format(float(f)))

def decode_msg(msg):
    # Reward;IsTerminalState;Action(rotation);State(distances[9])
    string_msg = msg.decode('utf-8')
    print(string_msg, end=' -> ')
    table = string_msg.split(';')
    
    reward = format_float(table[0])
    is_terminal_state = bool(table[1])
    
    # rotation = int(table[2])
    # action = Action(rotation)
    
    distances = [format_float(d) for d in table[3:3+9]]  
    new_state = State(distances)
    
    return reward, is_terminal_state, new_state
    

while True:
    tcp.accept_client()
    
    algorithm.initialize()
    while True:
        msg, is_connection_lost = tcp.try_receive_msg() # try do action
        if(is_connection_lost or len(msg) <= 0): # try do action
            break
        reward, is_terminal_state, new_state = decode_msg(msg) # do action
        
        new_action = algorithm.predict_and_learn(reward, new_state) # continue algorithm after doing action
        
        if(is_terminal_state):
            algorithm.initialize() # restart
            pass # handle terminal state - send signal to restart game
        else:
            new_action_signal = Action.map_to_signal(new_action)
            print(new_action_signal)
            tcp.send(new_action_signal)
            
            
    