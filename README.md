# **Projeto Grafos**

## **Índice:**  

[Intro](#Intro)  
[Como rodar a API?](#Como-rodar-a-API?)  
[Estrutura do código](#Estrutura-do-código)  
[Classes](#Classes)  
[Classe Graph](#Classe-Graph)  
[Classes Vertice e Edge](#Classes-Vertice-e-Edge)  
[Métodos](#Métodos)  
[Métodos da classe Graph](#Métodos-da-classe-Graph)  
[Métodos da classe Vertice](#Métodos-da-classe-Vertice)  
[Métodos da classe Edge](#Métodos-da-classe-Edge)  

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

# **Intro**

Projeto desenvolvido em Python com o objetivo de entregar uma API capaz de criar, modificar e analisar grafos. Durante a primeira etapa do projeto foi realizada a estrutura base da aplicação, com a possibilidade de criação, manipulação e visualização dos valores em um grafos. Para a segunda fase desenvolvemos um algoritmo de Dijkstra para encontrar o menor caminho entre os vértices de um grafo.

## **Como rodar a API?**
- Entre na pasta code dentro do repositório
- Execute no terminal python3 main.py
- Execute o comando `help` para mais informações

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

# Estrutura do código  

O código foi estruturado de uma forma que tivesse uma alta escalabilidade para futuras implementações. Com isso em mente foi escolhido adotar uma estratégia de programação orientada a objetos para que fosse possível dividir a estrutura do código de maneira mais acoplável para novas classes. Atualmente a API conta com as seguintes classes:  

## **Classes**

O código pode ser divido entre as seguintes classes:

### **Classe Graph** 

Todo o projeto é instanciado ela, onde são feitas as adições das demais classes. Fica resposável pelas seguintes atividades:  
* Criar os Vértices;
* Criar as Arestas;
* Retornar a ordem do grafo;
* Retornar o tamanho do grafo;
* Retornar os valores dos vértices;
* Retornar o grafo.

### **Classes Vertice e Edge**

Após instaciada a classe Graph é possível dar um nome para os vértices e arestas, para isso, é criado primeiro um objeto Vertice, o qual é responsável pela atribuição de valores para o vertice, incluindo a criação dos objetos Edge, que guardam os valores referentes a uma aresta do grafo.

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## **Métodos**

### **Métodos da classe Graph**  

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

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

### **Métodos da classe Vertice**
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

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

### **Métodos da classe Edge**  

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
