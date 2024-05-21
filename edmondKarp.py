class FlowNetwork:
    def __init__(self, routes, N_nodes, capacities, s, t) -> None:
        #See wikipedia on push-relabel
        self.routes = routes # [[u,v],[u,v], .... ]
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


def parse_input():
    # Input() takes line by line
    N, M, C, P = list(map(int, input().split()))

    # Take all the inputs from ever line with u, v, and c and make into ints split them make into route and add
    # route obj to routes
    routes = [Route(*input().split()) for _ in range(M)]

    # Edges to be removed
    to_remove = [int(input()) for _ in range(P)]
    return routes, to_remove, C, N


def edmondKarp(edges, N, s, t):
    # duplicate graph and reverse, essentially making it undirected 
    edges = [edge.reverse_node() for edge in edges] + edges
    n_e = len(edges)
    f_e = [0 for _ in range(n_e)]
    x_f_e = [edge.capacity for edge in edges]

    # GOLDBERG TIME


def main():
    routes, to_remove, C, N, M, P = parse_input()
    s, t = 0, N-1
    print(routes)
    split = 9
    Cmax = 9999999999999
    i = 0
    # test change again

    goldberg(routes)


if __name__ == "__main__":
    main()