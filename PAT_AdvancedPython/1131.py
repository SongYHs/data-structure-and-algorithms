# 当要多次计算同一图的最短路径，不能直接更新图的距离，除非在新图上加上更新后的路径作为虚拟路径

maxL=10**9+7
def dijkstra(dist, stops, s, e, lines):
    U, i= list(range(len(stops))), []
    U.remove(s)
    prev=[s]*len(stops)
    cost = dist[s][:].copy()
    while U:
        mins = maxL
        for u in U:
            if mins > cost[u]:
                i, mins=u, dist[s][u]
        
        U.remove(i)

        for u in U:
            if cost[i]+ dist[i][u] < cost[u]:
                prev[u]=i
                cost[u] = cost[i]+ dist[i][u]
    print({stops[i]: stops[prev[i]] for i in range(len(stops))})

    findAndPrint(prev, stops, s, e, lines)
def findAndPrint(prev, stops, s0, e, lines):
    c, ans = e, []
    while not c==s0:
        ans.insert(0, stops[c])
        c = prev[c]
    ans.insert(0,stops[s0])
    l  = set(lines[ans[0]]) & set(lines[ans[1]])
    pl = l.pop()
    start = ans[0]
    print(len(ans)-1) #  ans, [lines[a] for a in ans]
    # ans+=[("0","-1")]
    for i, s in enumerate(ans[1:]):
        l = set(lines[ans[i]]) & set(lines[s])
        if not pl in l:
            print(f"Take Line#{pl} from {start} to {ans[i]}")
            start, pl= ans[i-1], l.pop()
    print(f"Take Line#{pl} from {start} to {ans[-1]}")


if __name__=="__main__":
    n = 4# int(input())
    stops, c = {}, 0
    roads=[]
    lines = {}
    l1 = [
        "7 1001 3212 1003 1204 1005 1306 7797",
        "9 9988 2333 1204 2006 2005 2004 2003 2302 2001",
        "13 3011 3812 3013 3001 1306 3003 2333 3066 3212 3008 2302 3010 3011",
        "4 6666 8432 4011 1306"
    ]
    for i in range(n):
        line = l1[i].split()
        for i in range(1, len(line)-1):
            if not stops.get(line[i]):
                stops[line[i]] = c
                c+=1
            if not stops.get(line[i+1]):
                stops[line[i+1]] = c
                c+=1
            lines[line[i]] = lines.get(line[i], []) + [line[0]]
            if i == len(line)-2:
                lines[line[-1]] = lines.get(line[-1], []) + [line[0]]
            roads.append((stops[line[i]], stops[line[i+1]]))
    dist=[[maxL]* len(stops) for _ in range(len(stops))]
    for a, b in roads:
        dist[a][b]=1
        dist[b][a]=1
    for i in range(len(stops)):
        dist[i][i]=0
    m = 3#int(input())
    nstops = {v:(k) for k,v in stops.items()}
    l2 =["3011 3013","6666 2001","2004 3001"]
    print([(nstops[i], nstops[j]) for i, j in roads])
    for i in range(m):
        s, e = l2[i].split()
#         print( s, e, len(nstops), len(stops), stops[s][0], stops[e][0])
        dijkstra(dist, nstops, stops[s], stops[e], lines)