# Price Monitor

A Python-based price monitoring application that automatically tracks product prices and stores price history using SQLite.

The project uses Playwright for browser automation and JavaScript-rendered pages, SQLite for data persistence, and APScheduler for running the monitoring process periodically.

## Features

- Monitor product prices automatically
- Scrape JavaScript-rendered pages using Playwright
- Store product information in SQLite
- Store historical prices
- Compare current and previous prices
- Calculate price differences and percentage changes
- Run monitoring tasks automatically using APScheduler
- Use asynchronous programming with Playwright
- Maintain structured price history

## Technologies

- Python
- Playwright
- APScheduler
- SQLite
- asyncio
- Git
- GitHub

## Project Structure

```text
price-monitor/
│
├── monitor/
│   ├── __init__.py
│   └── scraper.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.10+
- pip
- Google Chrome or Chromium

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hydarian/price-monitor.git
cd price-monitor
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright

If you are using Playwright's bundled browsers:

```bash
playwright install
```

## Browser Configuration

The project uses Playwright to launch a Chromium-based browser.

If you are using an existing Chrome or Chromium installation, configure the executable path in the application.

Example:

```python
browser = await p.chromium.launch(
    executable_path=r"C:\chrome-win\chrome.exe",
    headless=True
)
```

Change the `executable_path` according to your local Chrome or Chromium installation.

### Headless Mode

For background execution:

```python
headless=True
```

For development and debugging:

```python
headless=False
```

## Database

The project uses SQLite to store product and price information.

The application creates the required database tables automatically.

The database stores information such as:

- Product information
- Product URL
- Current price
- Previous price
- Price change
- Price change percentage
- Price update time

The SQLite database is generated locally and should not be committed to GitHub.

## Running the Project

After installing the dependencies and configuring the browser path, run:

```bash
python main.py
```

The application will start the price monitoring process.

## Scheduling

The project uses APScheduler to run the monitoring process periodically.

For example, to run the monitor every 10 minutes:

```python
scheduler.add_job(
    monitor.run,
    trigger="interval",
    minutes=10
)
```

This allows the application to automatically check product prices without manually running the scraper each time.

## How It Works

The general workflow of the application is:

```text
Product URLs
     │
     ▼
Playwright
     │
     ▼
Load Product Page
     │
     ▼
Extract Product Information
     │
     ▼
Save Current Price
     │
     ▼
Compare With Previous Price
     │
     ▼
Calculate Price Change
     │
     ▼
Store Price History
     │
     ▼
Wait For Next Scheduled Run
```

## Price Change Calculation

For example:

```text
Previous Price: 10,000,000
Current Price:   9,500,000
```

Price difference:

```text
9,500,000 - 10,000,000 = -500,000
```

Percentage change:

```text
(-500,000 / 10,000,000) × 100 = -5%
```

The result indicates that the product price decreased by 5%.

## Error Handling

Web scraping applications can encounter different types of failures.

Possible problems include:

- Network problems
- Website changes
- Request timeouts
- Invalid product URLs
- Missing price elements
- Browser launch failures

## Development

To work on the project locally:

```bash
git clone https://github.com/Hydarian/price-monitor.git
cd price-monitor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

## Git Workflow

After making changes:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

## Limitations

- Scraping logic depends on the target website structure
- Browser automation requires more resources than simple HTTP requests
- SQLite is more suitable for lightweight applications
- No web dashboard
- No notification system
- Error recovery can be improved

## Future Improvements

- Add Telegram notifications when prices change
- Add support for multiple e-commerce websites
- Add a REST API
- Add a web dashboard
- Add Docker support
- Improve retry mechanisms
- Add structured logging
- Add automated tests
- Add Celery for background task processing
- Add price history visualization

## License

This project is created for educational and personal use.
