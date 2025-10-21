# Quote Scraper

A Python web scraper that collects quotes and authors from quotes.toscrape.com

## What it does
- Scrapes all 11 pages automatically
- Saves quotes and authors to CSV
- Handles errors 

## How to run
1. Install dependencies: `pip install requests beautifulsoup4`
2. Run: `python scraper.py`
3. Check `quotes.csv` for results

## What I learned
- HTTP requests with `requests` library
- HTML parsing with BeautifulSoup
- Error handling with try/except
- Writing data to CSV files