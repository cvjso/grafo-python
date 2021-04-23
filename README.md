# grafo-python
Sistema de criação e visualização de grafos feito em python

# Rodar projeto
- Entre na pasta code dentro do repositório
- Execute no terminal python3 main.py
- Execute o comando `help` para mais informações

# Classes
O codigo é divido entre classe principal e classes secundarias.

- Classe principal: Graph
    - Todo o projeto é instanciado por essa classe onde são feitas as adições das demais classes.
    - Dentro da classe são feitas: as criação dos vertices
                                   - criação das arestas
                                   - a ordem do grafo
                                   - o tamanho do grafo
                                   - retorno dos vertices
                                   - retorno do grafo

- Classes Secundarias: Vertice e Edge
    - Após instaciado o grafo pela classe Graph nós precisamos dar um nome para os vertices e arestas, então é criado permeiro a classe Vertice onde é feito todo e qualquer tipo de atribuição de valores para o vertice e após é criado a classe Edge onde que é feito uma atribuição de valores entre dois vertices.

# Metodos
Classe Graph:
- get_graph_vertices():
    - Parametros:
        nenhum
    
    Retorna uma lista de todos os vertices pertencentes ao grafo

- is_vertices_adjacents(vertice_one, vertice_two)
    - Parametros:
        vertice_one: Primeiro vertice da comparação
        vertice_two: Segundo vertice da comparação

    retorna verdadeiro caso os vertices sejam adjacentes e falso caso nao

- get_vertice_edges(vertice_name,direction='output'):
    - Parametros:
        vertice_name: nome do vertice que queira procurar as conecções dele

        direction: caso queira saber se o vertice ele possua arestas de chegada ou de saida (num grafo direcionado)
        Default: output(saida)

    Retorna uma lista de tuplas contendo as arestas que conectam aquele vertice com outros

- get_n_vertices_by_name(vertice_name, direction='output')
    - Parametros:
        vertice_name: nome do vertice que queira procurar a quantidade de conecções dele

        direction: caso queira saber se o vertice ele possua arestas de chegada ou de saida (num grafo direcionado)
        Default: output(saida)

    Retorna o tamanho das arestas que conectam aquele vertice com outros

- create_vertice(vertice_name, conection_list=[], edges_values:list = [])
    - Parametros:
        vertice_name: nome que vai ser atribuido ao vetice

        conection_list: lista de vertices que vao ser conectados com esse vertice

        edges_values: se o vertice possuira um nome em especifico

    Cria o vertice

- get_graph_order()
    - Parametros:
        nenhum

    Retorna o ordem do grafo

- get_vertice_value_by_name(vertice_name)
    - Parametros:
        vertice_name: Nome do vertice que queremos procurar

    Retorna o valor do vertice

- get_graph_size()
    - Parametros:
        nenhum

    Retorna o tamnha do grafo

- get_graph()
    - Parametros:
        nenhum
    
    Retorna todo grafo

- delete_vertice_by_name(vertice_name)
    - Parametros:
        vertice_name: nome do vertice que vai ser excluido do grafo

    exclui o vertice e suas conecções no grafo

- set_edge_value_by_edge(edge_tuple, new_value)
    - Parametros:
        edge_tuple: Tupla que contem os dois vertices que sua arestao possuira um novo valor

        new_value: Nome da nova aresta

    Setta o novo valor para a aresta

- get_edge_value_by_edge(edge_tuple)
    - Parametros:
        edge_tuple: Tupla que contem os dois vertices

    Retorna o nome da aresta

Classe Vertice:
- get_name():
    - Parametros:
        nenhum
    
    retorna o vertice

- get_vertice_conections()
    - Parametros:
        nenhum
    
    retorna as arestas relacionado ao vertice

- get_vertice_value()
    - Parametros:
        nenhum

    Retorna o valor atribuido para aquele vertice

- update_value(, new_value)
    - Parametros:
        new_value: Novo valor para o vertice
    
    setta um novo valor para aquele vertice

- set_edge_value_by_edge(edge_tuple, new_value)
    - Parametros:
        edge_tuple: Tupla que contem os dois vertices que sua arestao possuira um novo valor

        new_value: Nome da nova aresta

    Setta o novo valor para a aresta

- get_edge_value_by_edge(edge_tuple)
    - Parametros:
        edge_tuple: Tupla que contem os dois vertices

    Retorna o nome da aresta

Classe Edge:
- get_edge()
    - Parametros:
        Nenhum

    retorna a aresta

- get_edge_value()
    - Parametros:
        nenhum

    retorna o valor da aresta

- set_edge_value(value)
    - Parametros:
        value: valor que vai ser atribuido a aresta
    
    setta um valor para a aresta
