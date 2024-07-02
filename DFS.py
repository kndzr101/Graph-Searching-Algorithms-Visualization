from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited, dfs_sequence):
        visited.add(v)
        dfs_sequence.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, dfs_sequence)
    
    def DFS(self, v):
        visited = set()
        dfs_sequence = []
        self.DFSUtil(v, visited, dfs_sequence)
        return dfs_sequence

def animate_dfs(graph, dfs_sequence, pos):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('DFS Animation')

    def update(num):
        ax.clear()
        color_map = ['red' if node in dfs_sequence[:num+1] else 'blue' for node in graph.nodes()]
        
        nx.draw(graph, pos, node_color=color_map, with_labels=True, ax=ax)
        edge_labels = dict([((u, v), d['weight']) for u, v, d in graph.edges(data=True)])
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)

    ani = anim.FuncAnimation(fig, update, frames=len(dfs_sequence), repeat=False, interval=1000)
    plt.show()

if __name__ == "__main__":
    graph = Graph()

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 4)
    graph.addEdge(1, 10)
    graph.addEdge(7, 3)
    graph.addEdge(7, 5)
    graph.addEdge(4, 8)
    graph.addEdge(4, 7)
    dfs_sequence = graph.DFS(0)

    # Initialize the networkx graph
    nx_graph = nx.DiGraph()
    for node in graph.graph:
        for neighbor in graph.graph[node]:
            nx_graph.add_edge(node, neighbor, weight=1)

    # Draw the initial graph
    pos = nx.spring_layout(nx_graph)

    # Run the DFS animation
    animate_dfs(nx_graph, dfs_sequence, pos)

