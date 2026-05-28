# 📈 Alpaca Trading Bot

A Python-based automated trading bot built using the Alpaca Markets API for fetching real-time and historical stock market data, generating trading signals, and executing paper trades automatically.

> 🚀 Designed for algorithmic trading, market analysis, and strategy experimentation using moving average crossover logic and risk management techniques.

---

# ✨ Features

- ✅ Fetches real-time and historical stock market data
- ✅ Supports multiple stock symbols
- ✅ Implements Moving Average Crossover Strategy
- ✅ Automated BUY/SELL signal generation
- ✅ Paper trading using Alpaca Trading API
- ✅ Stop-loss and take-profit risk management
- ✅ Portfolio position tracking
- ✅ Minute-level OHLC data processing
- ✅ Error handling and continuous execution loop
- ✅ Easily extendable for advanced trading strategies

---

# 🧰 Tech Stack

| Component           | Technology |
|--------------------|------------|
| Language           | Python 3 |
| Trading API        | Alpaca Markets API |
| Data Processing    | Pandas |
| Timezone Handling  | pytz |
| Trading Framework  | alpaca-py |

---

# 📊 Trading Strategy

The bot uses a simple Moving Average Crossover strategy:

- BUY when short-term moving average crosses above long-term moving average
- SELL when short-term moving average crosses below long-term moving average

Risk management includes:
- Stop-loss protection
- Take-profit execution
- Position monitoring

---

# 📁 Project Structure

```bash
trading-bot/
│
├── trading_bot.py
├── requirements.txt
├── README.md

### 1. 📦 Clone the Repository
```bash
git clone https://github.com/Anubhab-anjan/Trading_Bot.git
cd Trading_Bot
