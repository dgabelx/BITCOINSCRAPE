import requests
import tweepy
import time
from bs4 import BeautifulSoup as Bitcoinscrape






url = "https://www.coindesk.com/price/bitcoin"

r = requests.get(url)

soup = Bitcoinscrape(r.content, "html.parser")

pricebitcoin = soup.find("div",{"class":"price-large"})
PB = pricebitcoin.text
print("Bitcoin is currently"+pricebitcoin.text,"worth.")



url = "https://www.coindesk.com/price/ethereum"

r = requests.get(url)

soup = Bitcoinscrape(r.content, "html.parser")

priceethereum = soup.find("div",{"class":"price-large"})
PE = priceethereum.text
print("Ethereum is currently" +priceethereum.text, "worth.")



url = "https://www.coindesk.com/price/dogecoin"

r = requests.get(url)

soup = Bitcoinscrape(r.content, "html.parser")

pricedogecoin = soup.find("div",{"class":"price-large"})
PD = pricedogecoin.text
print("Dogecoin is currently" +pricedogecoin.text, "worth.")



consumer_key = 'jNS34oBCmjlJoVjHHVKCwlqB4'
consumer_secret = 'tV60obo8LWcCoQt1jbYnJONn6r1Pm6BwQ4rI5K0CYFYxV0lovy'

key = '1387124570688262154-YH7rP5TXKd5w24UA1GWVLsrjGHalQs'

secret = 'iiwcbDDBIluCZX2AgMRFI9tXOU35W3r8SoEdzH8pKJ2vn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

def post():
    api = tweepy.API(auth)
    api.update_status("Bitcoin:" + PB +'\n' "Ethereum:" + PE +'\n' + "Dogecoin:" +PD)

while True:
    post()
    time.sleep(1800)
