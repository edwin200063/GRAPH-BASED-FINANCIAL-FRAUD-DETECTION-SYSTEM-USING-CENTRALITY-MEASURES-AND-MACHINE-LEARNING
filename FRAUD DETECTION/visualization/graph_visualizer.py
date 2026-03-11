import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, fraud_nodes):

    plt.figure(figsize=(14,10))

    # Better layout
    pos = nx.spring_layout(G, k=1.2)

    normal_nodes = [n for n in G.nodes() if n not in fraud_nodes]

    # Draw normal users
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=normal_nodes,
        node_color="skyblue",
        node_size=400,
        label="Normal Users"
    )

    # Draw fraud users
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=fraud_nodes,
        node_color="red",
        node_size=900,
        label="Fraud Users"
    )

    # Draw edges lightly
    nx.draw_networkx_edges(G, pos, alpha=0.2)

    # Show labels
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title("Graph Based Financial Fraud Detection", fontsize=16)
    plt.legend()
    plt.axis("off")

    plt.show()