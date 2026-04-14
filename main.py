import pandas as pd
from scraper import scrape_reviews
from preprocess import clean_text
from llm import summarize_review
from utils import save_to_csv

def main():
    url = input("Enter product URL: ")

    print("Scraping reviews...")
    reviews = scrape_reviews(url)

    processed_data = []

    for review in reviews:
        try:
            clean = clean_text(review["text"])
            summary = summarize_review(clean)

            processed_data.append({
                "author": review["author"],
                "rating": review["rating"],
                "date": review["date"],
                "original_review": review["text"],
                "clean_review": clean,
                "summary": summary
            })

        except Exception as e:
            print(f"Error processing review: {e}")

    df = pd.DataFrame(processed_data)
    save_to_csv(df)

    print("Done! Data saved in output/reviews.csv")

if __name__ == "__main__":
    main()