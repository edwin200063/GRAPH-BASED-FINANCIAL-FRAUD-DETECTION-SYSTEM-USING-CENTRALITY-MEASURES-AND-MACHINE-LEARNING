import pandas as pd
import random

def generate_dataset():

    users = list(range(1,101))  # 100 users
    data = []

    for i in range(200):

        sender = random.choice(users)
        receiver = random.choice(users)

        while receiver == sender:
            receiver = random.choice(users)

        amount = random.randint(100,20000)

        fraud = 0
        if amount > 15000 or random.random() < 0.1:
            fraud = 1

        data.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "fraud": fraud
        })

    df = pd.DataFrame(data)

    return df