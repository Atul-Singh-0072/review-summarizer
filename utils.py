import os

def save_to_csv(df):
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/reviews.csv", index=False)