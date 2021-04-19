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
        print("Graph added")
    
    def get_graph(self):
        return self.graphs[self.graph_index]
    
    def get_graphs(self):
        return self.graphs
    
    def get_graph_index(self):
        return self.graph_index
    
    def change_graph(self, new_index):
        if new_index >= len(graphs):
            print("Index invalid")
        else:
            self.graph_index
            print("Graph Changed")

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
        if user_input == exit:
            running = False
        else:
            lista = []
            while():
                lista.append(str(user_input))
                user_input = input()

            user_input = user_input.split()
            command = user_input[0] + " " + user_input[1]
            OPTIONS[command]()


if __name__ == '__main__':
    set_interaction()