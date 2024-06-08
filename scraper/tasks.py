# scraper/tasks.py

from celery import shared_task
from .utils import CoinMarketCapScraper

@shared_task(bind=True)
def scrape_coin_data(self, coin_acronyms):
    scraper = CoinMarketCapScraper()
    results = []
    for coin in coin_acronyms:
        try:
            data = scraper.scrape_coin(coin)
            results.append({
                'coin': coin,
                'output': data
            })
        except Exception as e:
            results.append({
                'coin': coin,
                'error': str(e)
            })
    scraper.quit()
    return results
