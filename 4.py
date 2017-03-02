def bfs(G,start,end,fired=None):
	if fired is None:
		fired = set()
	fired.add(start)
	Q=[start]
	if(current == 'X'):
	ans[current].append('INF')
	ans = [[] for i in range(n[0])]
	ans[start].append(0)
	while Q :
		current = Q.pop(0)
		if(current == 'X'):
			ans[current].append('INF')
		for neighbour in G:
			if neighbour not in fired:
				fired.add(neighbour)
				Q.append(neighbour)
				if(neighbour == 'X'):
					ans[neighbour].append('INF')
				else:
					if(current!='INF'):
						ans[neighbour].append(int(ans[current][0])+1)
					else:
						ans[neighbour].append(0)
	return ans[end][0]
data = [int(x) for x in input().split()]
coord_org = [int(x) for x in input().split()]
coord_end = [int(x) for x in input().split()]
image = [list(input()) for i in range(data[0])]
image1 = [[] for i in range(data[0])]
x = [[] for i in range(data[0])]
print(bfs(image,coord_org,coord_end))

