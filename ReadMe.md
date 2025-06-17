# Stock News Alert Project (Live Price + Telegram Alerts)
This Python project tracks a stock (like Tesla or Apple) and sends the latest stock price and the top 3 news headlines directly to your Telegram using your own bot.

## Features
- Real-time stock price using yfinance
- Top 3 breaking news from NewsAPI
- Alerts delivered via Telegram Bot
- Uses .env file to keep API keys safe

## Tools used
- Python
- yfinance
- NewsAPI
- Telegram Bot API
- python-dotenv
- requests
- VS Code

## Sample Telegram Alert
TSLA Current Price: $207.33 
Top 3 News Headlines:
Tesla announces record-breaking Q2 sales
The EV company delivered over 400,000 units in Q2, beating estimates.
https://www.reuters.com/business/tesla-earnings

Elon Musk teases new AI company
Musk reveals plans for a new venture, xAI, to rival OpenAI.
https://www.cnbc.com/elon-musk-launches-xai

Cybertruck delayed again
Tesla's Cybertruck production is delayed due to supply issues.
https://www.theverge.com/tesla-cybertruck-delays

## Note
To run the project, it includes ".env.example" file rename it to ".env" and replace the given values with your own API keys and credentials.