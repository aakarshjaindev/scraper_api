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
