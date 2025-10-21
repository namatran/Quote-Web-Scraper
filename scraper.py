import requests # installed requests library, then called url & got url from requests
from bs4 import BeautifulSoup # beautiful soup helps index & read through html
quotes = {}  # Create it once

import csv

with open('quotes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Author', 'Quote'])
    
    for page_num in range(1, 11):
        try:
            url = f"http://quotes.toscrape.com/page/{page_num}/"
            response = requests.get(url, timeout=10)  # Wait for website to respond for 10 seconds instead of forever

            if response.status_code != 200: # Catch filure to load page
                print(f"Failed to load page {page_num} - Status: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser') # Parse the text & find all text + authors then add
            table = soup.find_all('span', class_='text')
            tableauthors = soup.find_all('small', class_="author")

            if len(table) == 0: # If page is empty error
                print(f"No more quotes found. Stopping at page {page_num}")
                break
            
            for i in range(len(table)): # Write row allows it to write a new row 
                writer.writerow([tableauthors[i].text, table[i].text])
            
            print(f"Scraped page {page_num}")
        
        except requests.exceptions.RequestException as e: # Error handling
            print(f"Error on page {page_num}: {e}") 
            continue
        except Exception as e:
            print(f"Unexpected error on page {page_num}: {e}")
            continue