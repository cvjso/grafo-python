# -*- coding: utf-8 -*-
from Graph import Graph
import cmd

class GraphManager:
    graphs = []
    graph_index = 0

    def __init__(self):
        self.graphs.append(Graph("undirected", graph_id=self.graph_index))

    def add_graph(self, graph_type):
        self.graph_index += 1
        self.graphs.append(Graph(graph_type=graph_type, graph_id=self.graph_index))
        return("Graph added")
    
    def get_graph(self):
        return self.graphs[self.graph_index]
    
    def get_graphs(self):
        return str([graph.id for graph in self.graphs]) + f" você está agora no grafo {self.graph_index}"
    
    def get_graph_index(self):
        return self.graph_index
    
    def change_graph(self, new_index):
        if int(new_index) >= len(self.graphs):
            return("Index invalid")
        else:
            self.graph_index = int(new_index)
            return(f"Graph Changed, now using graph n°{self.graphs[self.graph_index].id}")

Manager = GraphManager()
OPTIONS = {
    "create graph": Manager.add_graph,
    "create vertice": Manager.get_graph().create_vertice,
    "get edges": Manager.get_graph().get_vertice_edges,
    "get order": Manager.get_graph().get_graph_order,
    "get vertices": Manager.get_graph().get_n_vertices_by_name,
    "get graph": Manager.get_graph().get_graph,
    "get graphs": Manager.get_graphs,
    "change graph": Manager.change_graph,
    "vertices": Manager.get_graph().get_graph_vertices,
}



####################################
class GraphInteraction(cmd.Cmd):
    prompt = f"graph {Manager.graph_index} > "
    history = []
    help_message = """
------------Comandos disponíveis------------
help -> mostra os comandos disponíveis
exit -> sai do programa
create graph (directed | undirected) -> cria um grafo direcionado ou não direcionado
get graph -> mostra o grafo atual
create vertice X to Y with Z -> X é o nome do vertice, Y o nome do vertice que será apontado e Z o valor da aresta
get edges X -> mostra as arestas da aresta X

    """

    def do_exit(self, line):
        return True

    def do_help(self,line):
        print(self.help_message)
    
    def do_change(self, line):
        line = line.split()
        command = "change" + " " + line[0].lower()
        print(OPTIONS[command](line[1]))
        self.prompt = f"graph {Manager.graph_index} > "

    def do_get(self, user_input):
        user_input = user_input.split()
        command = "get " + user_input[0]
        if user_input[0] == "graph":
            print(OPTIONS[command]())
        elif user_input[0] == "graphs":
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
            else:
                vertices_connection = user_input[2:]
                edges_values = ["" for i in range(len(vertices_connection))]
            OPTIONS[command](vertice_name, vertices_connection, edges_values)
        elif user_input[0] == "graph":
            print(OPTIONS[command](user_input[1]))
            self.prompt = f"graph {Manager.graph_index} > "

    def default(self, user_input):
        user_input = user_input.split()
        command = user_input[0].lower() + " " + user_input[1].lower()
        print(OPTIONS[command]())


if __name__ == '__main__':
    GraphInteraction().cmdloop()