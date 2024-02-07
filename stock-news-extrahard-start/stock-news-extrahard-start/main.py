import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "VDIPI9IR8ULYMJH0"
news_apikey = "cc547ad0071b4db7a8cb77bbc47fe929"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key,
}
response1 = requests.get("https://www.alphavantage.co/query", params=parameters)
response1.raise_for_status()
stock_data = response1.json()
# print(stock_data["Time Series (Daily)"]["2024-01-30"])
today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

yesterday_stock = float(stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
day_before_yesterday_stock = float(stock_data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])

percentage_change = (yesterday_stock - day_before_yesterday_stock) / day_before_yesterday_stock * 100
rounded_percent = round(percentage_change, 2)
## STEP 2: Use https://newsapi.org

tesla_param = {
    "q": "Tesla stocks",
    "from": day_before_yesterday,
    "to": yesterday,
    "sortBy": "popularity",
    "apikey": news_apikey,
}

response2 = requests.get("https://newsapi.org/v2/everything", params=tesla_param)
# news_data = response2.json()
# data0_title = news_data["articles"][0]["title"]
# data0_description = news_data["articles"][0]["description"]
# data0_link = news_data["articles"][0]["url"]
#
# if percentage_change > 0:
#     message = f"TSLA: 🔺{rounded_percent}%\n{data0_title}.\n{data0_description}\n{data0_link}"
# elif percentage_change < 0:
#     message = f"TSLA: 🔻{rounded_percent}%\n{data0_title}.\n{data0_description}\n{data0_link}"
# print(message)
articles = response2.json()["articles"]

three_art = articles[:3]
if percentage_change > 0:
    message = [f"{STOCK}: 🔺{rounded_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_art]
elif percentage_change < 0:
    message = [f"{STOCK}: 🔻{rounded_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_art]


bot_token = '6389852152:AAHB9xxBi-sxB_2WCK7K-pbAhUUmjYSE9vs'
bot_chatID = '6374414086'
for article in message:
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + article
    response = requests.get(send_text)
