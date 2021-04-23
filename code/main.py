# -*- coding: utf-8 -*-
from Graph import Graph
import cmd
from copy import deepcopy

class GraphManager:
    graphs = []
    graph_index = 0

    def __init__(self):
        self.graphs.append(Graph("directed", graph_id=self.graph_index))
        self.graph_index += 1
        self.graphs.append(Graph("undirected", graph_id=self.graph_index))

    def add_graph(self, graph_type):
        self.graph_index += 1
        self.graphs.append(deepcopy(Graph(graph_type=graph_type, graph_id=self.graph_index)))
        return("Graph added")
    
    def get_act_graph(self):
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
    
    def create_vertice(self, *args, **kwargs):
        return self.get_act_graph().create_vertice(*args,**kwargs)
    
    def get_vertice_edges(self, *args, **kwargs):
        return self.get_act_graph().get_vertice_edges(*args,**kwargs)
    
    def get_graph_order(self, *args, **kwargs):
        return self.get_act_graph().get_graph_order(*args,**kwargs)
    
    def get_graph(self, *args, **kwargs):
        return self.get_act_graph().get_graph(*args,**kwargs)
    
    def get_graph_vertices(self, *args, **kwargs):
        return self.get_act_graph().get_graph_vertices(*args,**kwargs)
    
    def get_n_vertices_by_name(self, *args, **kwargs):
        return self.get_act_graph().get_n_vertices_by_name(*args,**kwargs)
    
    def is_vertices_adjacents(self, *args, **kwargs):
        return self.get_act_graph().is_vertices_adjacents(*args,**kwargs)
    
    def set_edge_value_by_edge(self, *args, **kwargs):
        return self.get_act_graph().set_edge_value_by_edge(*args,**kwargs)
    
    def get_graph_size(self, *args, **kwargs):
        return self.get_act_graph().get_graph_size(*args,**kwargs)
    

Manager = GraphManager()
OPTIONS = {
    "create graph": Manager.add_graph,
    "create vertice": Manager.create_vertice,
    "get edges": Manager.get_vertice_edges,
    "order": Manager.get_graph_order,
    "get graph": Manager.get_graph,
    "get graphs": Manager.get_graphs,
    "change graph": Manager.change_graph,
    "vertices": Manager.get_graph_vertices,
    "degree": Manager.get_n_vertices_by_name,
    "adjacents vertices": Manager.is_vertices_adjacents,
    "set edge": Manager.set_edge_value_by_edge,
    "size":Manager.get_graph_size
}



####################################
class GraphInteraction(cmd.Cmd):
    prompt = f"graph {Manager.graph_index} {Manager.get_act_graph().graph_type} > "
    history = []
    help_message = """
------------Comandos disponíveis------------

help -> mostra os comandos disponíveis
exit -> sai do programa
create graph (directed | undirected) -> cria um grafo direcionado ou não direcionado
change graph X -> X é o numero de identificação do grafo
get graph -> mostra o grafo atual
get graphs -> mostra todos os grafos existentes

--- vertices ---
(valorado) create vertice X to Y with Z -> X é o nome do vertice, Y o nome do vertice que será relacionado e Z o valor da aresta
(não valorado) create vertice X to Y -> X é o nome do vertice e Y o nome do vertice que será relacionado
adjacents vertices X Y -> retorna se os vertices X e Y são adjacentes

--- edges ---
get edges X -> mostra as arestas da aresta X
degree X (input | output) -> X é o nome do vertice
order -> ordem do grafo
size -> tamanho do grafo
set edge X Y Z -> X e Y são os vertices da aresta e Z é o novo valor que a aresta terá
    """

    def att_prompt(self):
        self.prompt = f"graph {Manager.graph_index} {Manager.get_act_graph().graph_type} > "

    def do_exit(self, line):
        return True

    def do_help(self,line):
        print(self.help_message)
    
    def do_set(self, user_input):
        user_input = user_input.split()
        command = "set edge"
        print(OPTIONS[command](user_input[1], user_input[2], user_input[3]))

    def do_size(self, user_input):
        user_input = user_input.split()
        command = "size"
        print(OPTIONS[command]())
    
    def do_adjacents(self, user_input):
        user_input = user_input.split()
        command = "adjacents vertices"
        print(OPTIONS[command](user_input[1],user_input[2]))
    
    def do_vertices(self, user_input):
        user_input = user_input.split()
        command = "vertices"
        print(OPTIONS[command])
    
    def do_degree(self, user_input):
        user_input = user_input.split()
        command = "degree"
        print(OPTIONS[command](user_input[0], direction = user_input[1]))
    
    def do_order(self, user_input):
        user_input = user_input.split()
        command = "order"
        print(OPTIONS[command]())
    
    def do_change(self, user_input):
        user_input = user_input.split()
        command = "change" + " " + user_input[0].lower()
        print(OPTIONS[command](user_input[1]))
        self.att_prompt()

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
            self.att_prompt()

    def default(self, user_input):
        user_input = user_input.split()
        command = user_input[0].lower() + " " + user_input[1].lower()
        print(OPTIONS[command]())


if __name__ == '__main__':
    GraphInteraction().cmdloop()