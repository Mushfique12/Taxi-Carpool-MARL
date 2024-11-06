import numpy as np

class City:
    def __init__(self,
                 ):
        self.nodes = self.init_nodes()

    def init_nodes(self, ):
        nodes = [Node(i) for i in range(M*N)]  # list of nodes: node id start from 0
        rows, cols = np.where()
        return nodes

class Node:
    '''
    Represent one cell in city grid
    '''
    def __init__(self, idx):
        self.idx = idx