class Graph:
    # lista de vértices
    # matrix de adjacência ou lista de adjacência
    def __init__(self, vertex_list, adjacency_matrix = None):
        self.vertex_list = vertex_list
        if adjacency_matrix is not None:
            self.adjacency_matrix = adjacency_matrix
