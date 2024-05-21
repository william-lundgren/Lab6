import sys


class Route:
    def __init__(self, n1, n2, c):
        self.node_1 = n1
        self.node_2 = n2
        self.flow = c

    def __str__(self):
        return f"({self.node_1}, {self.node_2}, Flow:{self.flow})"

    def __repr__(self):
        return self.__str__()


def parse_input():
    # Input() takes line by line

    N, M, C, P = list(map(int, input().split()))

    # For every letter we get a list of the cost to every other letter, loop through all of them

    # Take all the inputs from ever line with u, v, and c and make into ints split them make into route and add
    # route obj to routes
    routes = [Route(*input().split()) for _ in range(M)]

    # Edges to be removed
    to_remove = [int(input()) for _ in range(P)]


def main():
    parse_input()


if __name__ == "__main__":
    main()