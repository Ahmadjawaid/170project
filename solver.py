import networkx as nx
import random
import matplotlib.pyplot as plt

def solve(client):
    client.end()
    client.start()

    all_students = list(range(1, client.students + 1))
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    client.scout(random.choice(non_home), all_students)

    botCounts = [(v,sum(client.scout(v, all_students).values())) for v in non_home]
    botCounts.sort(key=lambda x: x[1])

    for i in range(3,30):
    	client.G.remove_node(botCounts[i][0])

    mst = nx.algorithms.tree.mst.minimum_spanning_tree(client.G, weight = 'weight')
    shortestPaths = nx.single_source_dijkstra_path(mst, client.home, weight = 'weight')

    shortestPaths = sorted(shortestPaths.items(), key=lambda i:len(i[1]))

    for i in range(1,len(shortestPaths)):
        currPath = shortestPaths[-1 * i]
        if len(currPath[1]) > 1:
    	       client.remote(currPath[1][-1], currPath[1][-2])

    client.end()
