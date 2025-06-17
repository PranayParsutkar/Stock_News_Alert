import os
import requests
import yfinance as yf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

def get_current_stock_price():
    ticker = yf.Ticker(STOCK_NAME)
    data = ticker.history(period="1d")
    if data.empty:
        return "N/A"
    latest_price = data["Close"].iloc[-1]
    return round(latest_price, 2)
def get_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json()["articles"]
    top_3 = articles[:3]
    news_list = []
    for article in top_3:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        news_list.append(f"*{title}*\n{description}\n {url}")
    return news_list
def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_USER_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(telegram_url, data=payload)
    if response.status_code != 200:
        print("Failed to send Telegram message.")
    else:
        print("Alert sent to Telegram!")
def main():
    print("Running Stock News Alert Bot...")
    try:
        current_price = get_current_stock_price()
        price_msg = f"*{STOCK_NAME}* Current Price: ${current_price}\n*Top 3 News Headlines:*"
        send_telegram_message(price_msg)
        news_articles = get_news()
        for article in news_articles:
            send_telegram_message(article)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()