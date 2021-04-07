class Edge(object):

    def __init__(self, edge_tuple=(), value=None):
        self.edge = edge_tuple
        self.value = value
    
    def get_edge(self):
        return self.edge
    
    def get_edge_value(self):
        return self.value
    
    def set_edge_value(self,value):
        self.value = value