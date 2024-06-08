# scraper/utils.py

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Use ChromeDriverManager to install or fetch the Chrome WebDriver binary
driver = webdriver.Chrome(ChromeDriverManager().install())

class CoinMarketCapScraper:
    BASE_URL = 'https://coinmarketcap.com/currencies/'

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def scrape_coin(self, coin_acronym):
        url = f"{self.BASE_URL}{coin_acronym.lower()}/"
        self.driver.get(url)
        
        # Implement the scraping logic to extract details
        data = {
            'price': self._extract_price(),
            'price_change': self._extract_price_change(),
            'market_cap': self._extract_market_cap(),
            'market_cap_rank': self._extract_market_cap_rank(),
            'volume': self._extract_volume(),
            'volume_rank': self._extract_volume_rank(),
            'volume_change': self._extract_volume_change(),
            'circulating_supply': self._extract_circulating_supply(),
            'total_supply': self._extract_total_supply(),
            'diluted_market_cap': self._extract_diluted_market_cap(),
            'contracts': self._extract_contracts(),
            'official_links': self._extract_official_links(),
            'socials': self._extract_socials(),
        }
        
        return data

    def _extract_price(self):
        return self.driver.find_element(By.CLASS_NAME, "priceValue").text
    
    # Define similar methods to extract other required data...

    def quit(self):
        self.driver.quit()
