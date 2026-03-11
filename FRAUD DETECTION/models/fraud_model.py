from sklearn.ensemble import RandomForestClassifier

def train_fraud_model(features):

    # Feature columns
    X = features[["degree", "betweenness", "closeness"]]

    # Simulated fraud labels
    y = []
    for i in range(len(features)):
        if i % 10 == 0:
            y.append(1)   # Fraud
        else:
            y.append(0)   # Normal

    # Train model
    model = RandomForestClassifier(n_estimators=100)

    model.fit(X, y)

    return model