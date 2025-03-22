import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import time

def get_tweets(hashtag):
    url = f"https://twitter.com/hashtag/{hashtag}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Updated class name for tweet text container
    tweets = soup.find_all('div', class_='css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
    tweet_texts = [tweet.get_text() for tweet in tweets]
    
    # Filter out promotional tweets
    cleaned_tweets = [tweet for tweet in tweet_texts if "http" not in tweet]
    
    # Broaden keyword search for news-relevant tweets
    relevant_tweets = [tweet for tweet in cleaned_tweets if any(keyword in tweet.lower() for keyword in ["breaking", "event", "update", "report", "news"])]
    
    return relevant_tweets[:3]

def summarize_tweets(tweets):
    # Use BART as a fallback if LLaMA access isn't ready
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Replace with LLaMA once access is granted
    text_to_summarize = " ".join(tweets)
    summary = summarizer(text_to_summarize, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    hashtag = input("Enter a trending hashtag (e.g., News): ")
    print(f"Scraping tweets for #{hashtag}...")
    tweets = get_tweets(hashtag)
    
    if tweets:
        print(f"Found {len(tweets)} relevant tweets. Summarizing...")
        summary = summarize_tweets(tweets)
        print(f"Summary of #{hashtag}: {summary}")
    else:
        print("No relevant tweets found for this hashtag.")
    
    time.sleep(5)

if __name__ == "__main__":
    main()