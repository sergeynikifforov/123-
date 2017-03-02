def bfs(G,start,l,fired=None):
	if fired is None:
		fired = set()
	fired.add(start)
	Q=[start]
	while Q and l!=0:
		current = Q.pop(0)
		for neighbour in G[current]:
			if neighbour not in fired:
				fired.add(neighbour)
				Q.append(neighbour)
				print(current,neighbour)
				l-=1
	return l
n = [int(x) for x in input().split()]
a = []
graph = [[] for i in range(n[0])]
x = [[] for i in range(n[0])]
for edge in range(n[1]):
	a,b=  [int(x) for x in input().split()]
	graph[a].append(b)
	graph[b].append(a)
bfs(graph,1,n[0]-1)

