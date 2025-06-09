# 📊 Alpaca Trading Bot - Historical Data Fetcher

A Python script that fetches historical minute-level stock data for selected symbols using the [Alpaca Markets API](https://alpaca.markets/).

> 🔍 Built for quick data retrieval and potential future use in trading algorithms and backtesting systems.

---

## 🚀 Features

- ✅ Retrieves **minute-level** OHLCV data for multiple stocks
- ✅ Uses **Alpaca's SIP feed** for premium data access
- ✅ Handles time zone conversion (Eastern to UTC)
- ✅ Includes basic error handling and data preview
- ✅ Easily extendable for use in strategy backtesting or live trading

---

## 🧰 Tech Stack

| Component       | Technology         |
|----------------|--------------------|
| Language        | Python 3.10+       |
| Data Provider   | Alpaca Markets     |
| Libraries       | `alpaca-py`, `pytz`, `datetime` |

---

## 🛠️ Setup Instructions

### 1. 📦 Clone the Repository
```bash
git clone https://github.com/Anubhab-anjan/Trading_Bot.git
cd Trading_Bot
