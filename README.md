Binance Futures CLI Trading Bot

A command-line trading application built in Python that interacts with the Binance Futures API.

This project was developed to demonstrate clean software architecture, structured logging, proper validation, and real-world API integration in a trading environment.

📖 About the Project

This bot allows users to execute Futures trades directly from the terminal.

It supports:

Market orders

Limit orders

Automatic leverage configuration

Input validation before execution

Detailed logging for debugging and tracking

Graceful handling of API and runtime errors

The system is designed with modularity and scalability in mind, making it easy to extend with additional trading features in the future.

🏗 Project Structure
project/
│
├── bot/
│   ├── client.py          # Handles Binance API connection
│   ├── orders.py          # Contains trading logic
│   ├── validators.py      # Validates user inputs
│   ├── logging_config.py  # Configures logging system
│────── logs
|         ├── bot.log      #stores the log of orders and errors
├── cli.py                 # Main program entry point
├── requirements.txt
└── README.md

🧩 Architecture Overview

The application is divided into clear layers:

CLI Layer
Responsible for parsing user inputs and displaying results.

Service Layer
Handles core trading logic, including leverage setup and order placement.

Client Layer
Manages the connection to Binance Futures.

Validation Layer
Ensures that user inputs meet expected formats and constraints.

Logging Layer
Records order activity, responses, and errors for traceability.

This separation ensures maintainability, readability, and easier testing.

⚙️ Setup Instructions

Clone the repository
git clone  
cd project

Create and activate a virtual environment
python -m venv venv

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install required packages
pip install -r requirements.txt

🔐 Configuration

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

For testing purposes, use Binance Futures Testnet API keys.

▶ Running the Bot
Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order Example
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 50000

🔄 How It Works

The CLI collects trading parameters.

Inputs are validated to prevent incorrect orders.

Leverage is configured automatically for the selected symbol.

The order is sent to Binance Futures.

The response is logged and displayed to the user.

📝 Logging

The application logs:

Leverage configuration

Order request details

API responses

Errors and exceptions

Logs are:

Printed to the terminal

Saved in:

logs/bot.log

🛡 Error Management

The system handles:

API-related exceptions

Invalid command-line inputs

Missing price for limit orders

Unexpected runtime failures

Errors are clearly reported and logged for debugging.
