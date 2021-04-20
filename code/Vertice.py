from Edge import Edge
from copy import deepcopy

class Vertice(object):

    def __init__(self, vertice_name, conections=[],value=None):
        self.name = vertice_name
        self.conections = conections
        self.value = value
    

    def get_name(self):
        return self.name


    def get_vertice_conections(self):
        conection_list = []
        for conection in self.conections:
            conection_list.append(conection.edge)
        return conection_list


    def get_vertice_value(self):
        return self.value


    def update_conections(self, new_conection_list:list, edges_values:list):
        current_node_name = self.name
        for i in range(len(new_conection_list)):
            new_edge_tuple = (current_node_name, new_conection_list[i])
            new_edge = Edge(edge_tuple=new_edge_tuple, value=edges_values[i])
            self.conections.append(deepcopy(new_edge))


    def update_value(self, new_value):
        self.value = new_value


    def set_edge_value_by_edge(self, edge_tuple, new_value):
        for edge in self.conections:
            if edge_tuple == edge.get_edge():
                edge.set_edge_value(new_value)


    def get_edge_value_by_edge(self, edge_tuple):
        for edge in self.conections:
            if edge_tuple == edge.get_edge():
                return edge.get_edge_value()