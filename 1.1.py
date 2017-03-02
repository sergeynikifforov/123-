def dijkstra(G,start):
	d={v:float('inf') for v in G}
	d[start]=0
	used=set() 
	while len(used)!=len(G):
		min_d = float('inf')
		for v in d:
			if d[v]<min_d and v not in used:
				current = v
				mid_d = d[v]
		used.add(current)
		for neighbour in G[current]:
			l=d[current]+G[current][neighbour]
			if l<d[neigbour]:
				d[neigbour] = l
		used.add(current)
	return d				
n = [int(x) for x in input().split()]
graph = [[] for i in range(n[0])]
for edge in range(n[1]):
	a,b=  [int(x) for x in input().split()]
	graph[a].append(b)
	graph[b].append(a)
for i in range(n[0]):	
	print(dijkstra(graph,i))
