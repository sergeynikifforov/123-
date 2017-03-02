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
data = [int(x) for x in input().split()]
coord_org = [int(x) for x in input().split()]
coord_end = [int(x) for x in input().split()]
image = [list(input()) for i in range(data[0])]
graph = [[] for i in range(data[0]*data[1])]
print(graph)
x = [[] for i in range(data[0])]
k1=len(image)
k2=len(image[0])
for i in range(len(image)):
	for j in range(len(image[i])):
		if(image[i][j] != 'X'):
			if(image[i][j+1] == ' ' and (j+1)<k2):
				graph[i*k1+j*k2].append(i*k1+(j+1)*k2)
				graph[i*k1+(j+1)*k2].append(i*k1+j*k2)
			elif(image[i+1][j] == ' ' and (i+1)<k1):
				graph[i*k1+j*k2].append((i+1)*k1+j*k2)
				graph[(i+1)*k1+j*k2].append(i*k1+j*k2)
			elif(image[i+1][j+1] == ' ' and (i+1)<k1 and (j+1)<k2):
				graph[i*k1+j*k2].append((i+1)*k1+(j+1)*k2)
				graph[(i+1)*k1+(j+1)*k2].append(i*k1+j*k2)
print(graph)				
#print(bfs(image,coord_org,coord_end))

