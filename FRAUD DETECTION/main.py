from data.dataset_generator import generate_dataset
from graph.graph_builder import build_transaction_graph
from graph.centrality_features import compute_centrality_features
from models.fraud_model import train_fraud_model
from visualization.graph_visualizer import visualize_graph


def main():

    print("Generating dataset...")
    df = generate_dataset()

    print("Building transaction graph...")
    G = build_transaction_graph(df)

    print("Computing centrality measures...")
    features = compute_centrality_features(G)

    print("Training ML model...")
    model = train_fraud_model(features)

    X = features[["degree","betweenness","closeness"]]

    predictions = model.predict(X)

    fraud_nodes = features["node"][predictions == 1].tolist()

    print("Fraud Users Detected:", fraud_nodes)

    visualize_graph(G,fraud_nodes)


if __name__ == "__main__":
    main()