import networkx as nx
from typing import List, Dict, Tuple


def havel_hakimi(sequence: List[int]) -> nx.Graph:
    """Create a graph from a valid graphic sequence using Havel-Hakimi algorithm."""
    if not nx.is_graphical(sequence):
        return None

    G = nx.Graph()
    nodes = list(range(len(sequence)))

    while sequence and max(sequence) > 0:
        sequence, nodes = zip(*sorted(zip(sequence, nodes), reverse=True))
        sequence = list(sequence)
        nodes = list(nodes)

        d = sequence.pop(0)
        v = nodes.pop(0)

        if d > len(sequence):
            return None

        for i in range(d):
            sequence[i] -= 1
            if sequence[i] < 0:
                return None
            G.add_edge(v, nodes[i])

    return G


def is_eulerian(G: nx.Graph) -> bool:
    """Check if the graph is Eulerian (all nodes have even degree)."""
    return nx.is_eulerian(G)


def fleury_algorithm(G: nx.Graph) -> List[Tuple[int, int]]:
    """Implement Fleury's algorithm to find Eulerian circuit."""
    if not is_eulerian(G):
        return []

    G_copy = G.copy()
    eulerian_path = list(nx.eulerian_circuit(G_copy))
    return eulerian_path


def assign_random_weights(G: nx.Graph) -> None:
    """Assign random weights to the edges of the graph."""
    import random
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)


def dijkstra(G: nx.Graph, start: int) -> Dict[int, int]:
    """Implement Dijkstra's algorithm for shortest path."""
    return nx.single_source_dijkstra_path_length(G, start, weight='weight')


def minimum_spanning_tree(G: nx.Graph) -> nx.Graph:
    """Find minimum spanning tree using Kruskal's algorithm."""
    return nx.minimum_spanning_tree(G)


def fundamental_cutsets(G: nx.Graph, T: nx.Graph) -> List[set]:
    """Find fundamental cutsets with respect to the spanning tree."""
    cutsets = []
    for edge in G.edges():
        if edge not in T.edges():
            T.add_edge(*edge)
            cutset = nx.minimum_edge_cut(T, *edge)
            cutsets.append(cutset)
            T.remove_edge(*edge)
    return cutsets


def fundamental_circuits(G: nx.Graph, T: nx.Graph) -> List[set]:
    """Find fundamental circuits with respect to the spanning tree."""
    circuits = []
    for edge in G.edges():
        if edge not in T.edges():
            T.add_edge(*edge)
            circuit = nx.find_cycle(T, edge)
            circuits.append(set(circuit))
            T.remove_edge(*edge)
    return circuits


def edge_connectivity(G: nx.Graph) -> int:
    """Find edge connectivity of the graph."""
    return nx.edge_connectivity(G)


def vertex_connectivity(G: nx.Graph) -> int:
    """Find vertex connectivity of the graph."""
    return nx.node_connectivity(G)


def k_connectedness(G: nx.Graph) -> int:
    """Find the K-connectivity of the graph."""
    return min(edge_connectivity(G), vertex_connectivity(G))


def print_adjacency_list(G: nx.Graph) -> None:
    """Print the adjacency list representation of the graph with weights."""
    print("Adjacency List with Weights:")
    for node in G.nodes():
        neighbors = [(neighbor, G[node][neighbor]['weight']) for neighbor in G.neighbors(node)]
        print(f"{node}: {neighbors}")


def main():
    n = int(input("Please enter the length of the graphic sequence ----->  "))
    sequence = [0, -1]
    while not nx.is_graphical(sequence):
        sequence.clear()
        sequence = [int(input(f"Enter Degree of node {i}: ")) for i in range(n)]
        if not nx.is_graphical(sequence):
            print("The sequence you entered is not graphical according to the Havel Hakimi Algorithm.")

    print("The sequence you entered is :", sequence)
    G = havel_hakimi(sequence)

    if G is None:
        print(" NOT possible to generate graph ! ")
        return

    # Assign weights before printing the adjacency list
    assign_random_weights(G)

    # Print adjacency list with weights
    print_adjacency_list(G)

    if is_eulerian(G):
        print("The graph you entered is Eulerian.")
        euler_circuit = fleury_algorithm(G.copy())
        print("The Euler circuit is ---> ", euler_circuit)
    else:
        print("The graph you entered is not Eulerian.")

    start_node = random.choice(list(G.nodes()))
    shortest_paths = dijkstra(G, start_node)
    print(f"The shortest paths from node {start_node} using Dijkstra's Algorithm :", shortest_paths)

    # Find and print minimum spanning tree
    T = minimum_spanning_tree(G)
    print("\nMinimum Spanning Tree (MST) : ")
    print_adjacency_list(T)

    cutsets = fundamental_cutsets(G, T)
    circuits = fundamental_circuits(G, T)

    print("Fundamental cutsets for given graphical sequence ----> ", cutsets)
    print("Fundamental circuits ------> ", circuits)

    edge_conn = edge_connectivity(G)
    vertex_conn = vertex_connectivity(G)
    k_conn = k_connectedness(G)

    print("Edge connectivity ----> ", edge_conn)
    print("Vertex connectivity ----->", vertex_conn)
    print(f"The graph is {k_conn}-connected.")



if __name__ == "__main__":
    main()
