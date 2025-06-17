# scraping/chapter_scraper.py

import asyncio
from playwright.async_api import async_playwright
import os

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
SCREENSHOT_PATH = os.path.join("outputs", "chapter1_screenshot.png")
CONTENT_PATH = os.path.join("outputs", "chapter1_text.txt")

async def scrape_chapter():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(URL)

        # Screenshot full page
        await page.screenshot(path=SCREENSHOT_PATH, full_page=True)
        print(f"[✔] Screenshot saved at: {SCREENSHOT_PATH}")

        # Get visible text
        content = await page.inner_text("div#mw-content-text")
        with open(CONTENT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[✔] Content saved at: {CONTENT_PATH}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_chapter())
