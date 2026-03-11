import networkx as nx

def build_transaction_graph(df):

    G = nx.DiGraph()

    for _, row in df.iterrows():

        sender = row["sender"]
        receiver = row["receiver"]
        amount = row["amount"]

        G.add_edge(sender, receiver, weight=amount)

    return G