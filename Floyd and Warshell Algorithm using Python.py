def all_pair_sort(dist,n):
    for k in range(n):
     for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j], (dist[i][k]+dist[k][j]))
def transit_clos(reach,n):
 for k in range(n):
    for i in range(n):
        for j in range(n):
         reach[i][j]=(reach[i][j])or(reach[i][k]and reach[k][j])
#------------driver code-----------
#input for floyd's algorithm
graph=[[0,100,3,100],[2,0,100,100],[100,7,0,1],[6,100,100,0]]
n=4
all_pair_sort(graph,n)
print("All-Pairs- Shortest-Paths")
for i in range(n):
 print (graph[i])
#input for warshall's algorithm 
graph=[[1,1,0,1],[0,1,1,0],[0,0,1,1],[0,0,0,1]]
n=4
transit_clos(graph,n)
print("\ntransitive closure")
for i in range(n):
 print (graph[i])