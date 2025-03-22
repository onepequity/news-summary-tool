# LLaMA News Summary Tool

## Overview
This tool summarizes trending news topics from X by scraping user-generated tweets, avoiding mainstream media bias. Powered by LLaMA (or BART for testing), it delivers concise summaries of what people are talking about in real-time.

## Why It Exists
Traditional news aggregators often reflect editorial biases. This tool taps into raw, unfiltered conversations on X, capturing diverse perspectives directly from users. It’s perfect for businesses, researchers, or individuals seeking an unbiased view of trending topics.

## Features
- Scrapes tweets from any hashtag on X.
- Filters for news-relevant content using keywords like "breaking," "event," and "news."
- Summarizes discussions into concise, readable summaries using LLaMA AI.
- Designed for business applications (e.g., market trend analysis).

## Setup
1. **Clone the Repository**: 

   git clone https://github.com/onepequity/news-summary-tool.git

2. **Install Dependencies**:

   pip install requests beautifulsoup4 transformers torch

3. **Access LLaMA**:
- Request access to `meta-llama/Llama-2-7b-hf` on Hugging Face.
- Use `facebook/bart-large-cnn` as a fallback model for testing.

## Usage
1. Run the script:

   python news_summary_tool.py

2. Enter a trending hashtag (e.g., `News` or `StockMarket`).
3. View the summarized output of relevant tweets.

## Business Value
- **Market Insights**: Understand public sentiment on trending topics.
- **Efficiency**: Summarizes thousands of tweets in minutes.
- **Unbiased**: Reflects user voices, not media agendas.

## Example
**Input Hashtag**: #News  
**Output**: Summary of #News: Users discuss breaking updates on global events, including a recent political announcement.

## Notes
- X’s HTML structure changes often. Update the class name in `get_tweets()` using Chrome’s Inspect tool if scraping fails.
- Add more keywords to `relevant_tweets` filter for broader results.

## Future Enhancements
- Expand to scrape Facebook, Instagram, and TikTok.
- Add a web interface for easier access.

