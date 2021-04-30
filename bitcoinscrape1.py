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



consumer_key = 'yourkey'
consumer_secret = 'yourkey'

key = 'yourkey'

secret = 'yourkey'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

def post():
    api = tweepy.API(auth)
    api.update_status("Bitcoin:" + PB +'\n' "Ethereum:" + PE +'\n' + "Dogecoin:" +PD)

while True:
    post()
    time.sleep(1800)
