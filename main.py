import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from monitor.scraper import PriceMonitor



async def main():
    monitor = PriceMonitor(
        r"C:\chrome-win\chrome.exe"
    )

    await monitor.run()

    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        monitor.run,
        trigger="interval",
        minutes=1440,
        max_instances=1,
        coalesce=True
    )

    scheduler.start()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

