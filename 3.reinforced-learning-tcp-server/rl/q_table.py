Q_table = dict()

def getQ(s, a):
    if((s.to_tuple(), a) in Q_table):
        return Q_table[(s.pos.x, s.pos.y, a)]
    else:
        return 0
    # a_index = actions.map_to_id(a)
    # return Q_table[s.pos.x+1, s.pos.y, a_index]

def setQ(s, a, new_q):
    Q_table[(s.to_tuple(), a)] = new_q
    # a_index = actions.map_to_id(a)
    # Q_table[s.pos.x+1, s.pos.y, a_index] = new_q
    