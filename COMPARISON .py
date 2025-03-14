#printed a sample
if response.status_code == 200:
    data = response.json()
    print(data[:5])  # Print only the first 5 records
  import json
#save to JSON format
if response.status_code == 200:
    data = response.json()
    with open("scraped_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved to scraped_data.json")
#check JSON keys
for item in data[:5]:  # Show sample records
    print("Keys in record:", item.keys())
#for flipkart 
import requests
from bs4 import BeautifulSoup

product_url = "PRODUCT_PAGE_URL_HERE"  # Replace with actual product URL
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Try different price selectors
price = soup.find("span", class_="price-class")  # Replace with actual class
if not price:
    price = soup.find("div", class_="price-class")

print(f"Price: {price.text.strip() if price else 'Not Found'}")
