# -*- coding: utf-8 -*-
from Graph import Graph


def main():
    graph = Graph(graph_type='directed')

    graph.create_vertice(vertice_name='0', conection_list=['2','1'], edges_values=[7, 3])
    graph.create_vertice(vertice_name='1', conection_list=['3','4'], edges_values=[1, 1])
    graph.create_vertice(vertice_name='2', conection_list=['1','3','4'], edges_values=[1, 1, 7])
    graph.create_vertice(vertice_name='3', conection_list=['4'], edges_values=[3])
    graph.create_vertice(vertice_name='4', conection_list=[], edges_values=[])


    # graph.create_vertice(vertice_name='A', conection_list=[])
    # graph.create_vertice(vertice_name='B', conection_list=['A'], edges_values=[5])
    # graph.create_vertice(vertice_name='C', conection_list=['A','B'], edges_values=[10, 1])
    # graph.create_vertice(vertice_name='D', conection_list=['A','B', 'C'], edges_values=["Minas Gerais", "São bernado", "Campo Grande"])

    # Get vertices names validation
    #print(graph.get_graph_vertices())

    # Get distance
    graph.distance_dj('0','4')

    # Get edges from vertice validation
    # print(graph.get_vertice_edges('A'))
    #print(graph.get_vertice_edges('A', direction='input'))
    # print(graph.get_vertice_edges('B'))
    #print(graph.get_vertice_edges('C'))
    #print(graph.get_vertice_edges('D'))
    #print(graph.get_vertice_edges('E'))
    #print(graph.get_vertice_edges('F'))


    # Get graph order validation
    # print(graph.get_graph_order())

    # Get vertice value validation
    #print(graph.get_vertice_value_by_name('C'))


    # Get number of adjacent vertices validation
    # print(graph.get_n_vertices_by_name('B', direction='output'))
    # print(graph.get_n_vertices_by_name('B', direction='input'))
    # print(graph.get_n_vertices_by_name('B'))


    # Get graph validation
    # print(graph.get_graph())
    # print(graph.get_graph_vertices)


    # Delete Validation
    #print(graph.get_graph())
    #print(graph.get_graph_size())
    #print(graph.get_graph_order())
    #graph.delete_vertice_by_name('A')
    #graph.delete_vertice_by_name('E')
    #print(graph.get_graph())
    #print(graph.get_graph_size())
    #print(graph.get_graph_order())

    # Set edge value
    #graph.set_edge_value_by_edge(('C', 'A'), 1)
    #print('Resultado:')
    #print(graph.get_edge_value_by_edge(('C', 'A')))

main()