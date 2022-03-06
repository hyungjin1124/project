import requests
from twilio.rest import Client
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
with open('config.json', 'r') as f:
    config = json.load(f)

stock_api_key = config['DEFAULT']['STOCK_API_KEY']
stock_endpoint = 'https://www.alphavantage.co/query?'
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': stock_api_key
}

response = requests.get(url=stock_endpoint, params = stock_params)
response.raise_for_status()
result = response.json()

data_list = [value for (key, value) in result['Time Series (Daily)'].items()]
one_day_before_price = float(data_list[0]['4. close'])
two_day_before_price = float(data_list[1]['4. close'])

difference = abs(one_day_before_price - two_day_before_price)

if difference >= one_day_before_price * 0.01:
    # Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_api_key = config['DEFAULT']['NEWS_API_KEY']
    news_end_point = 'https://newsapi.org/v2/everything?'
    news_params = {
        'q':COMPANY_NAME,
        'apiKey':news_api_key
    }

    response = requests.get(url=news_end_point, params=news_params)
    response.raise_for_status()
    result = response.json()
    top3_articles = result['articles'][:3]

    formmated_articles = [{'title':article['title'], 'description':article['description']} for article in top3_articles]

    # Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 

    # get my twilio account_sid
    account_sid = config['DEFAULT']['TWILIO_ACCOUNT_SID']
    # get my twilio autho_token
    auth_token = config['DEFAULT']['TWILIO_AUTHO_TOKEN']

    # create client object
    client = Client(account_sid, auth_token)

    # create body of message
    if one_day_before_price > two_day_before_price:
        up_or_down = '▲'
    else:
        up_or_down = '▼'
    
    body = ''
    for article in formmated_articles:
        description = article['description'].replace('\n', '')
        body += f"""\n{COMPANY_NAME}: {up_or_down}{round(difference / two_day_before_price)}%\nHeadline: {article['title']}\nBreif: {description}
        """

    # send a mobile text message.
    message = client.messages \
                .create(
                    body=body,
                    from_='+19108382898',
                    to=config['DEFAULT']['TO_NUMBER']
                )
    print(message.status)