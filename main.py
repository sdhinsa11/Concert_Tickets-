import requests
from dotenv import load_dotenv
import os

load_dotenv() # load env vars from.env file

apikey = os.getenv("apikey") # gets the api key


url = "https://app.ticketmaster.com/discovery/v2/events.json"

params = {
    "size":1,
    "apikey": "{apikey}"
}