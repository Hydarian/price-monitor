import asyncio
from asyncio import timeout
from playwright.async_api import async_playwright, Playwright
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .database import MonitorPriceDatabase



class PriceMonitor:
    def __init__(self, path):
        self.path = path
        self.db = MonitorPriceDatabase()


    async def run(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                executable_path=self.path
            )

            # getting product link from file
            with open("products.txt") as f:
                urls = [line.strip() for line in f if line.strip()]

            for url in urls:
                page = await browser.new_page()
                MAX_RETRIES = 5

                for attempt in range(MAX_RETRIES):
                    try:
                        await page.goto(
                            url, wait_until='domcontentloaded', timeout=60000
                        )

                        title = await page.get_by_test_id("pdp-title").inner_text()
                        str_price = await page.locator('[data-theme-animation="price-container"]').first.inner_text()
                        price = int(str_price.replace(',',''))

                        self.db.saving_data_products(url, title)
                        self.db.saving_price_data(url, price)
                        change = self.db.price_change(url)

                        if change is not None:
                            print(f'Price changed: {change}%')

                        break
                    except Exception as e:
                        print(f"Timeout. Retry {attempt + 1}/{MAX_RETRIES}")
                        print(e)

                        await asyncio.sleep(3)
                else:
                    print('Failed after all retries.')

