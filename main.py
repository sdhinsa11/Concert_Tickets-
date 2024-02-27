import requests
from dotenv import load_dotenv
import os

load_dotenv() # load env vars from.env file

apikey = os.getenv("apikey") # gets the api key


url = "https://app.ticketmaster.com/discovery/v2/events.json?"

params = {
    "apikey": apikey,
    "countryCode": "CA",
    "city": "Vancouver"
    # "city": "Edmonton"
    
}

try: 
    response = requests.get(url, params=params)
    response.raise_for_status()
    json_data = response.json() # parse json
    
    events = json_data["_embedded"]["events"]

    for event in events:
        print("Name:", event["name"])
    

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)