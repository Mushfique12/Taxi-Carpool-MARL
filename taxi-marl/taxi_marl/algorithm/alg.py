class Value:
    '''
    Value network
    Also the Q Estimator (estimator of Q value)
    '''
    def __init__(self,
                 action_dim, # Dimension of action: 7 if hexagonal grid (6 neighbora + 1 current cell)
                 state_dim,
                 env,
                 ):
        self.env = env