def bfs(G,start,end,fired=None):
	if fired is None:
		fired = set()
	fired.add(start)
	Q=[start]
	ans = [[] for i in range(n[0])]
	ans[start].append(0)
	while Q :
		current = Q.pop(0)
		for neighbour in G[current]:
			if neighbour not in fired:
				fired.add(neighbour)
				Q.append(neighbour)
				ans[neighbour].append(int(ans[current][0])+1)
	return ans[end][0]
n = [int(x) for x in input().split()]
a = []
graph = [[] for i in range(n[0])]
x = [[] for i in range(n[0])]
for edge in range(n[1]):
	a,b=  [int(x) for x in input().split()]
	graph[a].append(b)
	graph[b].append(a)
print(bfs(graph,n[2],n[3]))

