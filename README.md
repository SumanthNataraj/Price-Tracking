# Price Tracker

## Overview
This project is a **Python-based web scraper** designed to track the prices of products on Snapdeal. It compares the current price of specified products with their target prices and provides recommendations on whether to purchase the product or wait for a price drop.

## Features
- Fetches the current price of products from Snapdeal using **BeautifulSoup** and **requests**.
- Compares the current price with the target price for each product.
- Writes the results to a text file (`result_file`) for further reference.
- Notifies whether the product price is below or above the target price.

## How It Works
1. A list of products is defined with their URLs, names, and target prices.
2. The script scrapes the current price of each product using the Snapdeal product page URL.
3. The comparison between the current price and the target price determines if it’s a good time to buy the product.
4. Results are displayed in the console and saved in the `result_file`.

## Prerequisites
- Python 3.7 or higher
- Libraries: `requests`, `beautifulsoup4`

Install the required libraries:
```bash
pip install requests beautifulsoup4
