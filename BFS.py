import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def BFS_animation(graph, source, pos):
    visited = {node: False for node in graph.nodes}
    queue = [source]
    visited[source] = True

    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('BFS Animation')
    
    def update(num):
        ax.clear()
        color_map = ['red' if visited[node] else 'blue' for node in graph]
        
        nx.draw(graph, pos, node_color=color_map, with_labels=True, ax=ax)
        edge_labels = dict([((u, v), d['weight']) for u, v, d in graph.edges(data=True)])
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
        
        if queue and num < len(graph.nodes):
            currNode = queue.pop(0)
            for neighbor in graph.neighbors(currNode):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    ani = anim.FuncAnimation(fig, update, frames=len(graph.nodes), repeat=False, interval=1000)
    plt.show()

# Initialize the graph
graph = nx.DiGraph()
graph.add_edge(0, 1, weight=3)
graph.add_edge(1, 2, weight=1)
graph.add_edge(2, 4, weight=1)
graph.add_edge(1, 10, weight=4)
graph.add_edge(7, 3, weight=1)
graph.add_edge(7, 5, weight=5)
graph.add_edge(4, 8, weight=2)
graph.add_edge(4, 7, weight=8)

# Draw the initial graph
pos = nx.spring_layout(graph)

# Run the BFS animation
BFS_animation(graph, 0, pos)

