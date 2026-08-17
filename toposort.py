import sys
import heapq

def main():
    input_data= list(map(int, sys.stdin.buffer.read().split()))
    if not input_data:
        return
    n = input_data[0]
    m = input_data[1]

    # Pre-allocate fast structure arrays
    indegree = [0] * (n + 1)
    graph =[[] for _ in range(n + 1)]
    it = iter(input_data)
    next(it) # skip n
    next(it) # skip m

    for u, v in zip(it, it):
        graph[u].append(v)
        indegree[v] += 1

    heap = [i for i in range(1, n + 1) if indegree[i] == 0]
    heapq.heapify(heap)

    order = []

    while heap:
        u = heapq.heappop(heap)
        order.append(u)

        for neighbor in graph[u]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    if len(order) == n:
        sys.stdout.write(" ".join(map(str, order)) + "\n")
        return
    else:
        sys.stdout.write("Sandro fails. \n")



if __name__ == '__main__':
    main()