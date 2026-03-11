def detect_fraud(model,features):

    X = features[[
        "degree",
        "betweenness",
        "closeness",
        "pagerank"
    ]]

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)[:,1]

    features["fraud_prediction"] = predictions
    features["fraud_probability"] = probabilities

    return features