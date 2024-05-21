import sys


def parse_input():
    # Input() takes line by line

    N, C, M, P = input().split()


    # For every letter we get a list of the cost to every other letter, loop through all of them
    # Convert the costs to int and add to list
    costs = [int(val) for val in input().split()]

    # Add the cost between current character and every other character
    for i, cost in enumerate(costs):
        gain_map[c][characters[i]] = cost
    # Next we get the query amount
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    # Return 2D array and comparisons we want to do
    return gain_map, queries


def main():
    pass


if __name__ == "__main__":
    main()