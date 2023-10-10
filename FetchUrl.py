import requests
from bs4 import BeautifulSoup


def fetch_and_save(url, path):
    # Choose a random proxy for this request
    proxy = {
        "http": "http://scraperapi:085b1119b9156014dd01ea049fad7b95@proxy-server.scraperapi.com:8001"
    }

    # Make the request using the selected proxy
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element containing the data you want to extract
    element = soup.find("h1", class_="HNMDR")

    # Extract the data from the element
    data = element.text

    # Save the data to a file
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

# Define the URL of the webpage you want to scrape
url = "https://timesofindia.indiatimes.com/india/centre-cites-pendency-for-blip-in-ease-of-doing-business-forgets-its-the-largest-litigant-seeking-frequent-needless-adjournments-bombay-hc/articleshow/104291598.cms"

# Define the path to save the scraped data
output_path = "data/scraped_data.txt"

# Fetch and save data using rotating proxies
fetch_and_save(url, output_path)
