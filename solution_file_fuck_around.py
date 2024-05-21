import sys


class FlowNetwork:
    def __init__(self, routes, N_nodes, capacities, s, t) -> None:
        #See wikipedia on push-relabel
        self.routes = routes
        self.N_nodes = N_nodes
        self.capacities = capacities
        self.s = s
        self.t = t
        self.N_edges = len(routes)

        self.f = [0 for _ in range(N_edges)]
        
        self.xf = [0 for _ in range(N_nodes)]
        self.cf = capacities.copy()

        self.labels = [0 for _ in range(N_nodes)]
        self.labels[s] = N_nodes

        self.Ef = self.routes.copy() #assuming all capacities != 0 for now?




class Route:
    def __init__(self, n1, n2, c):
        self.node_1 = n1
        self.node_2 = n2
        self.capacity = c

    def reverse_node(self):
        return Route(self.node_2, self.node_1, self.flow)

    def __str__(self):
        return f"({self.node_1}, {self.node_2}, Flow:{self.flow})"

    def __repr__(self):
        return self.__str__()


def parse_input():
    # Input() takes line by line
    N, M, C, P = list(map(int, input().split()))

    # Take all the inputs from ever line with u, v, and c and make into ints split them make into route and add
    # route obj to routes
    routes = [Route(*input().split()) for _ in range(M)]

    # Edges to be removed
    to_remove = [int(input()) for _ in range(P)]
    return routes, to_remove, C, N


def goldberg(edges, N, s, t):
    # duplicate graph and reverse, essentially making it undirected
    edges = [edge.reverse_node() for edge in edges] + edges
    n_e = len(edges)
    f_e = [0 for _ in range(n_e)]
    x_f_e = [edge.capacity for edge in edges]

    # GOLDBERG TIME


def main():
    routes, to_remove, C, N = parse_input()
    print(routes)
    # TODO replace with binary search
    Cmax = 9999999999999
    i = 0
    # test change again

    goldberg(routes)


if __name__ == "__main__":
    main()
