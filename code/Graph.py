from Vertice import Vertice
from copy import deepcopy

class Graph:

    def __init__(self, graph_type='directed', vertices_list=[]):
        self.graph_type = graph_type
        self.vertices = vertices_list
    

    def get_graph_vertices(self):
        vertice_list = []
        for vertice in self.vertices:
            vertice_list.append(vertice.get_name())
        return vertice_list


    def get_vertice_edges(self, vertice_name, direction='output'):
        if direction == 'output':
            for vertice in self.vertices:
                if vertice_name == vertice.get_name():
                    return vertice.get_vertice_conections()
        elif direction == 'input':
            input_conection_list = []
            for vertice in self.vertices:
                if vertice_name != vertice.get_name():
                    for edges in vertice.get_vertice_conections():
                        if vertice_name in edges:
                            input_conection_list.append(edges)
            return input_conection_list

        return None


    def get_n_vertices_by_name(self, vertice_name, direction='output'):
        if direction == 'output':
            for vertice in self.vertices:
                if vertice_name == vertice.get_name():
                    return len(vertice.get_vertice_conections())
        elif direction == 'input':
            input_conection_list = []
            for vertice in self.vertices:
                if vertice_name != vertice.get_name():
                    for edges in vertice.get_vertice_conections():
                        if vertice_name in edges:
                            input_conection_list.append(edges)
            return len(input_conection_list)

        return None
    

    def create_vertice(self, vertice_name, conection_list=[], value=None):
        new_vertice = Vertice(vertice_name=vertice_name, value=value)
        new_vertice.update_conections(new_conection_list=conection_list)
        self.vertices.append(deepcopy(new_vertice))


    def get_graph_order(self):
        return len(self.vertices)
    

    def get_vertice_value_by_name(self, vertice_name):
        for vertice in self.vertices:
            if vertice_name == vertice.get_name():
                return vertice.get_vertice_value()

    
    def get_graph_size(self):
        size = 0
        for vertice in self.vertices:
                size += len(vertice.get_vertice_conections())
        return size

    
    def get_graph(self):
        graph = {}
        for vertice in self.vertices:
                graph[vertice.get_name()] = (vertice.get_vertice_conections(), vertice.get_vertice_value())
        return graph

    
    def delete_vertice_by_name(self, vertice_name):
        index_to_delete = None
        for index in range(len(self.vertices)):
            if vertice_name == self.vertices[index].get_name():
                index_to_delete = index
        if index_to_delete != None:
            del self.vertices[index_to_delete]
            for vertice in self.vertices:
                current_vertice_name = vertice.get_name()
                edge_tuple = (current_vertice_name, vertice_name)
                vertice_edges = vertice.get_vertice_conections()
                if edge_tuple in vertice_edges:
                    index_to_delete = vertice_edges.index(edge_tuple)
                    del vertice.conections[index_to_delete]
    

    def set_edge_value_by_edge(self, edge_tuple, new_value):
        for vertice in self.vertices:
            if edge_tuple in vertice.get_vertice_conections():
                vertice.set_edge_value_by_edge(edge_tuple, new_value)


    def get_edge_value_by_edge(self, edge_tuple):
        for vertice in self.vertices:
            if edge_tuple in vertice.get_vertice_conections():
                return vertice.get_edge_value_by_edge(edge_tuple)