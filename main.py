'''
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape-title/")
def scrape_title(request: ScrapeRequest):
    """
    Accepts a URL and returns the title of the web page.
    """
    try:
        # Send a request to the URL, with a timeout
        response = requests.get(request.url, timeout=10)
        # Raise an error if the request was not successful
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle network errors, invalid URLs, etc.
        raise HTTPException(status_code=400, detail=f"Could not fetch URL: {e}")

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title tag and get its text
    title = soup.find('title')
    if not title:
        return {"url": request.url, "title": "No title found"}

    return {"url": request.url, "title": title.get_text()}

@app.get("/")
def read_root():
    return {"status": "Scraper API is running"}

    '''
import logging
from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from bs4 import BeautifulSoup
import httpx

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scraper")

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape-title/")
async def scrape_title(request: ScrapeRequest):
    # Validate URL
    parsed = urlparse(request.url)
    if not parsed.scheme.startswith("http") or not parsed.netloc:
        raise HTTPException(status_code=400, detail="Invalid URL format.")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/130.0.0.0 Safari/537.36"
        )
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(request.url, headers=headers)
            response.raise_for_status()
    except httpx.RequestError as e:
        logger.error(f"Request error: {e}")
        raise HTTPException(status_code=400, detail=f"Could not fetch URL: {e}")
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

    soup = BeautifulSoup(response.content, "html.parser")
    title_tag = soup.find("title")

    if not title_tag:
        return {"url": request.url, "title": "No title found"}

    return {"url": request.url, "title": title_tag.get_text(strip=True)}

@app.get("/")
async def read_root():
    return {"status": "Scraper API is running"}

