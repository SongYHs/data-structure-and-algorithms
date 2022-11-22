# ​
# Input Specification:
# Each input file contains one test case. Each case starts with a line containing 4 positive integers N, M, S, and D, where N (≤500) is the number of cities (and hence the cities are numbered from 0 to N−1); M is the number of highways; S and D are the starting and the destination cities, respectively. Then M lines follow, each provides the information of a highway, in the format:

# City1 City2 Distance Cost

# where the numbers are all integers no more than 500, and are separated by a space.

# Output Specification:
# For each test case, print in one line the cities along the shortest path from the starting point to the destination, followed by the total distance and the total cost of the path. The numbers must be separated by a space and there must be no extra space at the end of output.

# Sample Input:
# 4 5 0 3
# 0 1 1 20
# 1 3 2 30
# 0 3 4 10
# 0 2 2 20
# 2 3 1 20

# Sample Output:
# 0 2 3 3 40


def travel_plan(roads, n, s, d):
    maxL = 10**9+7
    dist = [[(maxL, maxL)]*n for _ in range(n)]
    for i, j, l, c in roads:
        dist[i][j] = (l, c)
        dist[j][i] = (l, c)
    prev = [-1]*n
    lens, cost = [maxL]*n, [maxL]*n
    for i in range(n):
        dist[i][i] = (0, 0)
        if not dist[s][i][0] == maxL:
            prev[i] = s
            lens[i], cost[i] = dist[s][i]
    prev[s] = -1
    U = list(range(n))
    while U:
        minU, minC, i = maxL, maxL, -1
        for u in U:
            if lens[u] < minU or (lens[u] == minU and cost[u] < minC):
                minU, minC = lens[u], cost[u]
                i = u
        U.remove(i)
        for v in U:
            if lens[i] + dist[i][v][0] < lens[v] \
                or (
                    lens[i] + dist[i][v][0] == lens[v] and
                    cost[i] + dist[i][v][1]< cost[v]
                ):
                prev[v] = i
                lens[v] = lens[i] + dist[i][v][0]
                cost[v] = cost[i] + dist[i][v][1]
    cur, ans = d, []
    while not cur == -1:
        ans.insert(0, cur)
        cur = prev[cur]
    return ans + [lens[d], cost[d]]  
 

if __name__=="__main__":
    n,m,s,d = list(map(int,input().split()))
    roads = [list(map(int, input().split())) for _ in range(m)]
    res = travel_plan(roads, n, s, d)
    print(" ".join(list(map(str, res))))
