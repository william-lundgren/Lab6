import sys


class Route:
    def __init__(self, n1, n2, c):
        self.node_1 = n1
        self.node_2 = n2
        self.flow = c

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


def push(u, v, f, h):
    if xf[u] > 0 and 𝓁[u] == 𝓁[v] + 1: return
    delta = min(xf[u], c[u][v] - f[u][v])
    f[u][v] += delta
    f[v][u] -= delta
    xf[u] -= delta
    xf[v] += delta


def goldberg(edges):
    # GOLDBERG TIME

    # duplicate graph
    edges = [edge.reverse_node() for edge in edges] + edges


def main():
    routes, to_remove, C, N = parse_input()
    print(routes)
    # TODO replace with binary search
    Cmax = 9999999999999
    i = 0

    goldberg(routes)


if __name__ == "__main__":
    main()
