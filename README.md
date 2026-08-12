# Price Monitor

A Python-based application for monitoring product prices and tracking
price changes over time.

## Features

- Scrape product prices using Playwright
- Store product and price data in SQLite
- Track price changes over time
- Automatically monitor prices every 10 minutes
- Asynchronous execution using asyncio
- Scheduled tasks using APScheduler

## Technologies

- Python
- Playwright
- SQLite
- asyncio
- APScheduler

## Installation

Clone the repository:

git clone <your-repository-url>

Install dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install

## Running

Run the application:

python main.py

The application performs an initial price check and then automatically
checks the products every 10 minutes.
