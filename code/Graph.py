from Vertice import Vertice
from copy import deepcopy

class Graph:

    def __init__(self, graph_type='directed', vertices_list=[], graph_id=0):
        self.id = graph_id
        self.graph_type = graph_type
        self.vertices = vertices_list
    
    def distance_dj(self,start, end = None):
        lista_ordem = [start]
        start_vertice = self._get_vertice_by_name(start)
        start_vertice.update_value(0)

        while(lista_ordem != []):
            actual_vertice = self._get_vertice_by_name(lista_ordem[0])
            inital_connections = actual_vertice.conections
            for edge in inital_connections:
                val_vert = actual_vertice.value
                target_val = self.get_vertice_value_by_name(edge.get_edge()[1])
                edge_val = edge.value
                target_vert_name = edge.get_edge()[1]
                lista_ordem.append(target_vert_name)

                if (target_val == None or (val_vert + edge_val) < target_val):
                    target = self._get_vertice_by_name(target_vert_name)
                    target.update_value(val_vert + edge_val)
                    target.set_origin(actual_vertice.name)
            
            lista_ordem.pop(0)
        

        if type(end) == str:
            loop_vertice = self._get_vertice_by_name(end)
            msg = f"{start} para {loop_vertice.name} com custo de {loop_vertice.value}"
            percourse = [loop_vertice.name]
            while(loop_vertice.origin != None):
                percourse.append(loop_vertice.origin)
                loop_vertice = self._get_vertice_by_name(loop_vertice.origin)
            print(msg)
            percourse.reverse()
            print(percourse)

            

        
    
    def _get_vertice_by_name(self, target) -> Vertice:
        for vertice in self.vertices:
            if vertice.name == target:
                return vertice

    def _get_edges(vertice):
        pass

    def get_graph_vertices(self):
        vertice_list = []
        for vertice in self.vertices:
            vertice_list.append(vertice.get_name())
        return vertice_list

    def is_vertices_adjacents(self, vertice_one:str, vertice_two:str):
        edges = self.get_vertice_edges(vertice_one)
        for edge in edges:
            if tuple((vertice_one, vertice_two)) == edge or tuple((vertice_two, vertice_one)) == edge:
                return True
        return False

    def get_vertice_edges(self, vertice_name, direction='all') -> list:
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

            for index in range(len(conection_list)):
                conection_list[index] = tuple(i for i in sorted(conection_list[index]))
            return list(set(conection_list))

    # Grau do vertice
    def get_n_vertices_by_name(self, vertice_name, direction='output') -> int:
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
        all_vertices = [vertice.name for vertice in self.vertices]
        if vertice_name in all_vertices:
            raise Exception("Vertice already exists")
        new_vertice = Vertice(vertice_name=vertice_name, conections=[])
        new_vertice.update_conections(new_conection_list=conection_list, edges_values = edges_values)
        self.vertices.append(deepcopy(new_vertice))
        # Conecto o vertice depois de criado nos outros vertices
        if self.graph_type == "undirected":
            for vertice in self.vertices:
                if vertice.name in conection_list:
                    index_value = conection_list.index(vertice.name)
                    vertice.update_conections(new_conection_list=[vertice_name], edges_values= [edges_values[index_value]])


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
        if self.graph_type == "undirected":
            size = size//2
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
    

    def set_edge_value_by_edge(self, vertice_one, vertice_two, new_value):
        if self.graph_type == "directed":
            edge_tuple = tuple((vertice_one, vertice_two))
            for vertice in self.vertices:
                if edge_tuple in vertice.get_vertice_conections():
                    vertice.set_edge_value_by_edge(edge_tuple, new_value)
        else:
            edge_tuple = tuple((vertice_one, vertice_two))
            seg_edge = tuple((vertice_two, vertice_one))
            for vertice in self.vertices:
                if edge_tuple in vertice.get_vertice_conections():
                    vertice.set_edge_value_by_edge(edge_tuple, new_value)
                if seg_edge in vertice.get_vertice_conections():
                    vertice.set_edge_value_by_edge(seg_edge, new_value)
        return "updated edge"


    def get_edge_value_by_edge(self, edge_tuple):
        for vertice in self.vertices:
            if edge_tuple in vertice.get_vertice_conections():
                return vertice.get_edge_value_by_edge(edge_tuple)