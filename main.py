import requests
from bs4 import BeautifulSoup

url = "https://www.byerstoyota.com/used-vehicles/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Now we can find data within the page
vehicles = soup.find_all('div', class_='vehicle-card')
for vehicle in vehicles:
    # Print vehicle details
    print(vehicle.text)
