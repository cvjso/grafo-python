# -*- coding: utf-8 -*-
from Graph import Graph
import cmd

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
class GraphInteraction(cmd.Cmd):
    prompt = "graph> "
    history = []

    def start(self):
        Manager.add_graph()

    def do_get(self, user_input):
        user_input = user_input.split()
        command = "get " + user_input[0]
        if user_input[0] == "graph":
            print(OPTIONS[command]())
        elif user_input[0] == "edges":
            print(OPTIONS[command](user_input[1]))
    
    def do_history(self, line):
        print(history)
    
    def do_create(self, user_input):
        user_input = user_input.split()
        command = "create " + user_input[0]
        if user_input[0] == "vertice":
            user_input.pop(0)
            vertices_connection = []
            edges_values = []
            vertice_name = user_input[0]
            if "with" in user_input:
                parameters = [i for i in user_input[2:] if i != "with"]
                i = 0
                while(i < len(parameters)):
                    vertices_connection.append(parameters[i])
                    edges_values.append(parameters[i+1])
                    i += 2
            OPTIONS[command](vertice_name, vertices_connection, edges_values)
    
    def default(self, user_input):
        user_input = user_input.split()
        command = user_input[0].lower() + " " + user_input[1].lower()
        print(OPTIONS[command]())


if __name__ == '__main__':
    GraphInteraction().cmdloop()