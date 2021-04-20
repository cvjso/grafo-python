# -*- coding: utf-8 -*-
from Graph import Graph

class GraphManager:
    graphs = []
    graph_index = 0

    def __init__(self):
        self.graphs.append(Graph())

    def add_graph(self):
        self.graphs.append(Graph())
        self.graph_index += 1
        return("Graph added")
    
    def get_graph(self):
        return self.graphs[self.graph_index]
    
    def get_graphs(self):
        return self.graphs
    
    def get_graph_index(self):
        return self.graph_index
    
    def change_graph(self, new_index):
        if new_index >= len(graphs):
            return("Index invalid")
        else:
            self.graph_index
            return("Graph Changed")

Manager = GraphManager()
OPTIONS = {
    "create graph": Manager.add_graph,
    "create vertice": Manager.get_graph().create_vertice,
    "get edges": Manager.get_graph().get_vertice_edges,
    "get order": Manager.get_graph().get_graph_order,
    "get vertices": Manager.get_graph().get_n_vertices_by_name,
    "get graph": Manager.get_graph().get_graph
}



####################################
def set_interaction():
    running = True
    while(running):
        user_input = input("graph> ")
        if user_input == "exit":
            running = False
        else:
            # lista = []
            # while():
            #     lista.append(user_input)
            #     user_input = input()

            user_input = user_input.split()
            command = user_input[0].lower() + " " + user_input[1].lower()
            if command == "create vertice":
                """
                (directed) create vertice A to B with ten C with two D with banana
                (undirected) create vertice A to B C D
                """
                vertices_connection = []
                edges_values = []
                vertice_name = user_input[2]
                if "with" in user_input:
                    new_list = [i for i in user_input[4:] if i != "with"]
                    i = 0
                    while(i < len(new_list)):
                        vertices_connection.append(new_list[i])
                        edges_values.append(new_list[i+1])
                        i += 2
                    OPTIONS[command](vertice_name, vertices_connection, edges_values)
            else:
                print(OPTIONS[command]())




if __name__ == '__main__':
    set_interaction()