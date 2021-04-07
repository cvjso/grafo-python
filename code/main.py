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
    
    def change_graph(self, new_index:int):
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

def main():
    graph = Graph()

    graph.create_vertice(vertice_name='A', conection_list=[], value="Recife")
    graph.create_vertice(vertice_name='B', conection_list=['A'], value="Fortaleza")
    graph.create_vertice(vertice_name='C', conection_list=['A','B'], value="Maceio")
    graph.create_vertice(vertice_name='D', conection_list=['A','B', 'C'], value="Minas Gerais")
    graph.create_vertice(vertice_name='E', conection_list=[], value="Sao Paulo")

    # Get vertices names validation
    #print(graph.get_graph_vertices())

    # Get edges from vertice validation
    #print(graph.get_vertice_edges('A'))
    #print(graph.get_vertice_edges('A', direction='input'))
    #print(graph.get_vertice_edges('B'))
    #print(graph.get_vertice_edges('C'))
    #print(graph.get_vertice_edges('D'))
    #print(graph.get_vertice_edges('E'))


    # Get graph order validation
    #print(graph.get_graph_order())

    # Get vertice value validation
    #print(graph.get_vertice_value_by_name('C'))


    # Get number of adjacent vertices validation
    #print(graph.get_n_vertices_by_name('B', direction='output'))
    #print(graph.get_n_vertices_by_name('B', direction='input'))


    # Get graph validation
    #print(graph.get_graph())


    # Delete Validation
    print(graph.get_graph())
    print(graph.get_graph_size())
    print(graph.get_graph_order())
    #graph.delete_vertice_by_name('A')
    #graph.delete_vertice_by_name('E')
    #print(graph.get_graph())
    #print(graph.get_graph_size())
    #print(graph.get_graph_order())

def set_interaction():
    running = True
    while(running):
        user_input = input("graph> ")
        if user_input == "exit":
            running = False
        else:
            user_input = user_input.split()
            command = user_input[0] + " " + user_input[1]
            OPTIONS[command]()


if __name__ == '__main__':
    set_interaction()