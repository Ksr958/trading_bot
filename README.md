# Binance Futures CLI Trading Bot

A command-line trading bot built in Python that interacts with the Binance Futures Testnet API.  
This project demonstrates clean architecture, modular design, proper input validation, structured logging, and real-world API integration.

---

## 📌 Project Overview

This bot allows users to execute Futures trades directly from the terminal. It supports:

- **Market Orders** – Buy or sell instantly at market price.
- **Limit Orders** – Place orders at a specific price.
- **Automatic Leverage Configuration** – Set leverage before placing an order.
- **Input Validation** – Ensures correct parameters before sending requests.
- **Structured Logging** – Logs all API interactions, requests, and errors.
- **Error Handling** – Graceful handling of API errors and runtime exceptions.

The project is designed to be **modular, scalable, and maintainable**, making it easy to extend with additional trading strategies or features.

---

## 🏗 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py           # Python package initializer
│   ├── client.py             # Binance API connection
│   ├── orders.py             # Trading logic and order placement
│   ├── validators.py         # Validates user input
│   └── logging_config.py     # Sets up logging
│
├── logs/
│   └── bot.log               # Logs all order activity and errors
│
├── cli.py                    # Command-line interface entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
🧩 Architecture Overview

The project is divided into layers:

CLI Layer – Handles parsing user input and displaying results.

Service Layer – Contains trading logic, including leverage setup and order placement.

Client Layer – Manages the Binance API connection.

Validation Layer – Ensures all user inputs are valid.

Logging Layer – Records order requests, responses, and errors for traceability.

This separation ensures maintainability, readability, and easier testing.

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/trading_bot.git
cd trading_bot

2. Create and Activate Virtual Environment
python -m venv venv
# Activate venv:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Credentials

Create a .env file in the root directory with your Binance Testnet keys:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

▶ Usage Examples
Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 50000

🔄 Execution Flow

CLI parses the arguments provided by the user.

Inputs are validated to prevent incorrect orders.

Leverage is automatically configured for the selected symbol.

Order is sent to the Binance Futures API.

Response is displayed to the user and logged.

📝 Logging

Logs include:

Leverage configuration

Order request details

API responses

Errors and exceptions 

Error Management

The bot handles:

Binance API exceptions (invalid API key, insufficient balance, etc.)

Invalid command-line inputs (wrong symbols, sides, or order types)

Missing price for LIMIT orders

Unexpected runtime failures

Errors are logged and clearly displayed to the user for debugging.

⚠️ Price Validation on Binance Futures

SELL LIMIT orders must be above the current market price.

BUY LIMIT orders must be below the current market price.

Setting a price outside these limits will result in an API error (e.g., code -4024).

MARKET orders execute immediately at the best available price and do not require manual price input