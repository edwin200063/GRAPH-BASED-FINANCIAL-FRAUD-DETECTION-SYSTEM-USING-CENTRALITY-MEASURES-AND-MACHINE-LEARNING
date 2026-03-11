import networkx as nx
import pandas as pd

def compute_centrality_features(G):

    degree = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)

    data = []

    for node in G.nodes():

        data.append({
            "node": node,
            "degree": degree[node],
            "betweenness": betweenness[node],
            "closeness": closeness[node]
        })

    df = pd.DataFrame(data)

    return df