import random

def scrape_reviews(url):
    print("Using dynamic sample review data")

    positive_reviews = [
        "Amazing product, really loved it!",
        "Excellent quality and great performance.",
        "Worth every penny, highly recommend.",
        "Very satisfied with the purchase.",
        "Superb product, exceeded expectations."
    ]

    negative_reviews = [
        "Very bad quality, not recommended.",
        "Waste of money, stopped working.",
        "Poor performance and low durability.",
        "Not satisfied, expected better.",
        "Terrible experience overall."
    ]

    neutral_reviews = [
        "Average product, okay for price.",
        "Not bad, not great.",
        "Decent quality but can improve.",
        "Works fine but nothing special.",
        "Okay product for daily use."
    ]

    # Change output based on URL keyword
    if "amazon" in url.lower():
        selected = positive_reviews
    elif "flipkart" in url.lower():
        selected = negative_reviews
    else:
        selected = neutral_reviews

    reviews = []

    for i in range(5):
        reviews.append({
            "text": random.choice(selected),
            "author": f"User{i+1}",
            "rating": f"{random.randint(1,5)} stars",
            "date": f"2024-01-{i+1}"
        })

    return reviews