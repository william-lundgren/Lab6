from collections import deque
import time
import sys


def binary(split, prev_split, to_remove, N, M, P, edges, capacities, s, t, Cmax):

    attempt_to_remove = to_remove[:split]
    attempt_edges = [edge for i, edge in enumerate(edges) if i not in attempt_to_remove]
    new_cmax = edmondKarp(N, M, attempt_edges, capacities,  s, t)
    
    brute_force_limit = 2
    if abs(split - prev_split) < brute_force_limit:
        low = min(split, prev_split)
        high = low+brute_force_limit
        low = low-brute_force_limit
        low = 0 if low < 0 else low
        for split2 in range(low, high):
            attempt_to_remove = to_remove[:split2]
            attempt_edges = [edge for i, edge in enumerate(edges) if i not in attempt_to_remove]
            prev_cmax = new_cmax
            new_cmax = edmondKarp(N, M, attempt_edges, capacities,  s, t)
            if new_cmax < Cmax:
                return split2-1, prev_cmax

    
    if prev_split != -1:
        if split == prev_split: #We done
            return split, new_cmax

        diff = abs(prev_split-split)
    else: 
        diff = abs(P-1 - split)
    prev_split = split

    if new_cmax > Cmax:
        split += diff//2
    else:
        split -= diff//2
        
    return binary(split, prev_split, to_remove, N, M, P, edges, capacities, s, t, Cmax)
    ##print("haha fel")
    

        

def parse_input():
    # Input() takes line by line
    N, M, C, P = list(map(int, input().split()))

    # Take all the inputs from ever line with u, v, and c and make into ints split them make into route and add
    # route obj to routes
    capacities = [[0 for _ in range(N)] for _ in range(N) ]
    edges = [[] for _ in range(M)]

    for i in range(M):
        u, v, c = list(map(int, input().split()))
        capacities[u][v] = capacities[v][u] = c
        edges[i] = [u, v]
        ##print(edges[i])
    ##print(edges)
    # Edges to be removed
    to_remove = [int(input()) for _ in range(P)]
    return N, M, C, P, edges, capacities, to_remove


def edmondKarp(N, M, edges, capacities,  s, t):
    flow = [[0 for _ in range(N)] for _ in range(N) ] #edge flow
    # c_f = capacities.copy()

    #Skapa ett träd
    children = [[] for _ in range(N)] #Lista över alla noder som har en edge med en given nod
    for e in edges:
        ##print(e)
        u, v = e
        children[u].append(v)
        children[v].append(u)

    totalflow = 0

    while True: #gör BFS flera gånger tills vi inte hittar fler enkla bra fina vägar

        #Initiate arrays
        visited = [False for _ in range(N)]
        visited[s] = True
        pred = [None for _ in range(N)]
        q = deque([s])
        finished_bfs = False

        #BFS
        while q and not finished_bfs:
            v = q.popleft()

            # Neighborss
            for u in children[v]:
                
                
                if not visited[u] and capacities[v][u] - flow[v][u] > 0: #Only consider nodes that have capacities left
                    visited[u] = True
                    q.append(u)
                    pred[u] = v
                    if u == t:
                        finished_bfs = True
                        break
                
        if not finished_bfs: #Could not find a way where flow could be increased, we are done
            return totalflow #return flow out from start node

        #First traceback, to find delta 
        delta = None
        current = t
        while current != s:
            # ##print('lalala')
            preceding = pred[current]
            d = capacities[preceding][current] - flow[preceding][current]
            if delta is None or d < delta:
                delta = d
            current = preceding

        totalflow += delta
        
        #Second traceback, to update flow
        current = t
        while current != s:
            preceding = pred[current]
            flow[preceding][current] += delta
            current = preceding
             
def main():
    tstart = time.time()
    N, M, C, P, edges, capacities, to_remove = parse_input()
    s, t = 0, N-1
    print(*binary(P//2, -1, to_remove, N, M, P, edges, capacities, s, t, C))
    sys.stderr.write(f"Time: {time.time()-tstart}\n")

    # # Linear just to check edmond is working
    # prev_cmax = 999999999999
    # new_cmax = 999999999999
    # steps = 1
    # while new_cmax >= C:
    #     attempt_to_remove = to_remove[:steps]
    #     attempt_edges = [edge for i, edge in enumerate(edges) if i not in attempt_to_remove]
    #     #print("atetetet",attempt_edges)
    #     prev_cmax = new_cmax
    #     new_cmax = edmondKarp(N, M, attempt_edges, capacities,  s, t)
    #     steps +=1
    
    # print(steps-2, prev_cmax)
    
if __name__ == "__main__":
    main()