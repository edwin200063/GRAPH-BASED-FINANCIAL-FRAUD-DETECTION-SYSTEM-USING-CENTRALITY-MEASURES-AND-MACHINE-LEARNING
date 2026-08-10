

# 🔐 Graph-Based Financial Fraud Detection System

## 📌 Overview

The **Advanced Graph-Based Financial Fraud Detection System** is an intelligent fraud detection application that combines **Graph Theory, Centrality Measures, Machine Learning, and Data Analysis** to identify potentially fraudulent financial transactions and suspicious accounts.

Traditional fraud detection systems often analyze transactions independently. However, financial fraud can involve multiple accounts, repeated transactions, intermediaries, and complex relationships.

This project represents financial transactions as a **graph network** and combines graph-based features with machine learning to detect suspicious behavior.

---

## 🎯 Problem Statement

Financial fraud is a major challenge for banks, financial institutions, digital payment platforms, and e-commerce systems.

Fraudsters may use:

- Multiple accounts
- Rapid transactions
- Money transfer chains
- Suspicious intermediaries
- High-frequency transactions
- Coordinated groups of accounts

Analyzing each transaction independently may fail to identify these relationships.

Therefore, this project proposes a **graph-based fraud detection approach** where accounts are represented as nodes and transactions are represented as edges.

Graph centrality measures are then calculated and combined with transaction features to train a machine learning model.

---

## 💡 Proposed Solution

The system follows this process:

```text
                Financial Transactions
                         │
                         ▼
                  Data Preprocessing
                         │
                         ▼
                Transaction Graph
                         │
                         ▼
               Centrality Calculation
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Degree       Betweenness      Closeness
      Centrality     Centrality      Centrality
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                     PageRank
                         │
                         ▼
                Feature Engineering
                         │
                         ▼
                  SMOTE / Balancing
                         │
                         ▼
                  Random Forest
                         │
                         ▼
                 Fraud Prediction
                         │
                         ▼
                  Risk Assessment
                         │
                         ▼
                 Web Dashboard


---

🚀 Features

1. Transaction Analysis

The system analyzes financial transactions using features such as:

Transaction amount

Source account

Destination account

Transaction frequency

Account relationships

Graph-based characteristics



---

2. Graph-Based Analysis

Financial transactions are represented as a graph.

Account A ───────► Account B
    │                  │
    │                  ▼
    └──────────────► Account C
                       │
                       ▼
                    Account D

Graph Representation

Nodes: Bank accounts / users

Edges: Financial transactions

Edge attributes: Transaction amount, timestamp, transaction type, etc.


This allows the system to identify relationships between accounts.


---

📊 Centrality Measures

The project uses multiple centrality measures to identify suspicious or important nodes in the financial network.

1. Degree Centrality

Degree centrality measures how many connections a node has.

An account with an unusually high number of connections may require further investigation.

B
        │
        │
A ───── C ───── D
        │
        │
        E

Here, account C has multiple connections.


---

2. Betweenness Centrality

Betweenness centrality measures how often a node appears on the shortest paths between other nodes.

It can help identify accounts acting as intermediaries.

A ─── B ─── C ─── D
        ↑
   Intermediary

An account with high betweenness may play an important role in moving money between different groups.


---

3. Closeness Centrality

Closeness centrality measures how close a node is to other nodes in the network.

An account with high closeness can reach other accounts through relatively short paths.


---

4. PageRank

PageRank measures the importance of a node based on the importance of the nodes connected to it.

This can help identify influential accounts within a transaction network.


---

🤖 Machine Learning

After graph analysis, centrality measures are combined with transaction-level features.

The machine learning pipeline is:

Raw Transaction Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Graph Construction
        ↓
Centrality Measures
        ↓
Feature Combination
        ↓
Class Balancing
        ↓
Model Training
        ↓
Fraud Prediction

Machine Learning Algorithm

The primary classification model used in this project is:

Random Forest

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make predictions.

It is suitable for this project because it can handle:

Multiple features

Non-linear relationships

Numerical data

Feature interactions

Classification problems



---

⚖️ Handling Imbalanced Data

Financial fraud datasets are usually highly imbalanced.

For example:

Legitimate Transactions: 95%
Fraudulent Transactions: 5%

If the model simply predicts every transaction as legitimate, it may achieve high accuracy while failing to detect fraud.

Therefore, the project can use SMOTE (Synthetic Minority Over-sampling Technique) to improve representation of the minority fraud class during model training.


---

📈 Model Evaluation

The system evaluates the machine learning model using:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Confusion Matrix


Precision

Measures how many transactions predicted as fraud were actually fraudulent.

Recall

Measures how many actual fraudulent transactions were successfully detected.

F1-Score

Provides a balance between precision and recall.

ROC-AUC

Measures the model's ability to distinguish between legitimate and fraudulent transactions across classification thresholds.


---

🖥️ Web Application

The project uses Flask to provide a web-based interface.

The dashboard can display:

Transaction information

Fraud predictions

Risk scores

Suspicious accounts

Centrality scores

Graph relationships

Model results


Example workflow:

User
 │
 ▼
Web Dashboard
 │
 ▼
Transaction Input
 │
 ▼
Flask Backend
 │
 ├── Graph Engine
 │
 └── ML Model
       │
       ▼
 Fraud Prediction
       │
       ▼
 Dashboard Result


---

🗂️ Project Structure

Advanced-Graph-Based-Financial-Fraud-Detection/
│
├── app.py
├── database.py
├── graph_engine.py
├── ml_model.py
├── data_generator.py
├── requirements.txt
├── README.md
│
├── data/
│   └── transactions.csv
│
├── models/
│   └── fraud_model.joblib
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── results.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── database/
    └── fraud_detection.db


---

🛠️ Technologies Used

Programming Language

Python


Backend

Flask


Machine Learning

Scikit-learn

Random Forest

SMOTE


Graph Processing

NetworkX


Data Processing

Pandas

NumPy


Visualization

Matplotlib

Seaborn


Database

SQLite


Model Serialization

Joblib


Frontend

HTML

CSS

JavaScript



---

⚙️ Installation

Step 1: Clone the Repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Navigate to the project:

cd Advanced-Graph-Based-Financial-Fraud-Detection


---

Step 2: Create Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate


---

Step 3: Install Dependencies

pip install -r requirements.txt


---

📦 Requirements

Example requirements.txt:

Flask
pandas
numpy
networkx
scikit-learn
imbalanced-learn
matplotlib
seaborn
joblib

Install manually if required:

pip install flask pandas numpy networkx scikit-learn imbalanced-learn matplotlib seaborn joblib


---

▶️ Running the Application

Start the Flask application:

python app.py

After starting the server, open:

http://127.0.0.1:5000

The application dashboard will then be available in your browser.


---

🔍 Example Detection Process

Suppose a transaction occurs:

Source Account      : ACC102
Destination Account : ACC450
Transaction Amount  : ₹85,000

The system extracts transaction features and analyzes the accounts in the graph.

It calculates:

Degree Centrality
Betweenness Centrality
Closeness Centrality
PageRank

These features are passed to the machine learning model.

The model produces a prediction such as:

Prediction : Potential Fraud
Risk Level : HIGH

This result can then be displayed on the dashboard.


---

🔐 Security

Financial systems contain sensitive information.

The following security practices should be followed:

Never store passwords directly in source code.

Never upload API keys to GitHub.

Never upload .env files.

Validate user input.

Use authentication for administrative features.

Protect database credentials.

Use HTTPS when deploying publicly.


Example .gitignore:

.env
venv/
.venv/
__pycache__/
*.pyc
*.pyo
*.db


---

📊 System Architecture

┌─────────────────────┐
                  │   User / Admin      │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Flask Web App     │
                  └──────────┬──────────┘
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
      ┌─────────────────┐       ┌─────────────────┐
      │  Graph Engine   │       │   ML Engine     │
      └────────┬────────┘       └────────┬────────┘
               │                         │
               ▼                         ▼
      ┌─────────────────┐       ┌─────────────────┐
      │ Centrality      │       │ Random Forest   │
      │ Measures        │       │ Classifier      │
      └────────┬────────┘       └────────┬────────┘
               │                         │
               └────────────┬────────────┘
                            ▼
                  ┌─────────────────────┐
                  │ Fraud Risk Analysis │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Dashboard / Results │
                  └─────────────────────┘


---

🔮 Future Enhancements

The project can be extended with:

Real-Time Fraud Detection

Monitor transactions continuously and generate alerts immediately.

Graph Neural Networks

Implement GNN-based fraud detection for more advanced graph learning.

Real-Time Alerts

Send notifications when high-risk transactions are detected.

Explainable AI

Show why a transaction was classified as suspicious.

Advanced Graph Visualization

Provide interactive transaction networks.

Cloud Deployment

Deploy the application using cloud platforms.

Advanced Anomaly Detection

Combine supervised classification with unsupervised anomaly detection.

Multi-Level Fraud Detection

Detect:

Individual fraudulent transactions

Suspicious accounts

Fraud rings

Coordinated transaction networks



---

🎓 Project Information

Project Title:
Advanced Graph-Based Financial Fraud Detection System Using Centrality Measures and Machine Learning

Domain:
Artificial Intelligence and Machine Learning

Sub-Domain:
Financial Fraud Detection

Technologies:
Python, Flask, NetworkX, Scikit-learn, Pandas, NumPy, SQLite

Project Type:
Academic / Final Year Project


---

🎯 Project Objectives Summary

Objective	Description

Fraud Detection	Identify potentially fraudulent transactions
Graph Analysis	Analyze relationships between financial accounts
Centrality Analysis	Identify important or suspicious nodes
Machine Learning	Classify transactions based on learned patterns
Risk Analysis	Generate fraud risk levels
Visualization	Display transaction and fraud insights
Web Interface	Provide an accessible dashboard



---

🌟 Advantages

Combines graph theory and machine learning.

Detects relationship-based fraud patterns.

Identifies suspicious intermediary accounts.

Handles imbalanced fraud datasets.

Provides multiple graph centrality features.

Supports visual analysis.

Can be extended to real-time fraud detection.

Suitable for academic and research applications.



---

⚠️ Limitations

Model performance depends on the quality of the dataset.

Synthetic data may not represent real-world fraud patterns.

Centrality measures can become computationally expensive for very large graphs.

Fraud predictions should be treated as decision-support signals rather than definitive proof of fraud.



---

📚 Conclusion

The Advanced Graph-Based Financial Fraud Detection System demonstrates how Graph Theory and Machine Learning can be combined to detect suspicious financial activity.

By representing financial transactions as a network, the system can analyze relationships between accounts using Degree Centrality, Betweenness Centrality, Closeness Centrality, and PageRank.

These graph-based features are combined with transaction characteristics and provided to a machine learning model for fraud classification.

The proposed approach provides a strong foundation for developing more advanced financial fraud detection systems and can be further extended using real-time monitoring, Graph Neural Networks, Explainable AI, and cloud-based deployment.


---

👨‍💻 Author

Your Name Edwin joe.M

B.Tech Information Technology


---

📜 License

This project is developed for educational and research purposes.


---

⭐ If you find this project useful

Give this repository a ⭐ on GitHub.
