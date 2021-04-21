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


    def get_vertice_edges(self, vertice_name, direction='all'):
        if vertice_name not in self.get_graph_vertices():
            return None

        if self.graph_type == 'directed':
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
            else:
                input_conection_list = []
                for vertice in self.vertices:
                    if vertice_name != vertice.get_name():
                        for edges in vertice.get_vertice_conections():
                            if vertice_name in edges:
                                input_conection_list.append(edges)
                for vertice in self.vertices:
                    if vertice_name == vertice.get_name():
                        input_conection_list += vertice.get_vertice_conections()
                return input_conection_list
        
        elif self.graph_type == 'undirected':
            conection_list = []
            for vertice in self.vertices:
                for edges in vertice.get_vertice_conections():
                    if vertice_name in edges:
                        conection_list.append(edges)

            for edge in range(len(conection_list)):
                conection_list[edge] = tuple(i for i in sorted(conection_list[edge]))
            return list(set(conection_list))


    def get_n_vertices_by_name(self, vertice_name, direction='output'):
        if vertice_name not in self.get_graph_vertices():
            return None

        if self.graph_type == 'directed':
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
        
        elif self.graph_type == 'undirected':
                conection_list = []
                for vertice in self.vertices:
                    for edges in vertice.get_vertice_conections():
                        if vertice_name in edges:
                            conection_list.append(edges)
                
                for edge in range(len(conection_list)):
                    conection_list[edge] = tuple(i for i in sorted(conection_list[edge]))
                return len(list(set(conection_list)))
    

    def create_vertice(self, vertice_name, conection_list=[], edges_values:list = []):
        new_vertice = Vertice(vertice_name=vertice_name, conections=[])
        new_vertice.update_conections(new_conection_list=conection_list, edges_values = edges_values)
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
        graph = ""
        for vertice in self.vertices:
            name = vertice.get_name()
            graph += name + ":"
            for edge_tuple in vertice.get_vertice_conections():
                edge_value = vertice.get_edge_value_by_edge(edge_tuple)
                graph += f"\n\t{edge_value} -> {edge_tuple[1]}"
            graph+="\n"
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