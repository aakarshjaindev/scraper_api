# Simple Web Scraper API

A lightweight and efficient API built with Python and FastAPI to perform basic web scraping tasks. This service accepts a URL and returns structured data, such as the page title.

## About The Project

In the world of data, the ability to quickly extract information from websites is a fundamental skill. This project serves as a robust and easily deployable microservice that provides a clean RESTful interface for basic web scraping.

It is designed to be a reliable backend component for applications that need to fetch web page metadata, preview links, or gather simple data without the overhead of a full-scale scraping framework.

## Features

* **Title Extraction**: Scrapes the primary `<title>` tag from any given URL.
* **Error Handling**: Gracefully handles common network issues, invalid URLs, and HTTP errors.
* **High Performance**: Built on FastAPI and Uvicorn for fast request handling.
* **Lightweight & Deployable**: Minimal dependencies ensure a small footprint and easy deployment on free cloud hosting platforms.
* **Interactive Documentation**: Comes with automatically generated API docs via Swagger UI.

## Tech Stack

* **Backend:** Python
* **API Framework:** FastAPI
* **Web Server:** Uvicorn
* **HTTP Requests:** `requests`
* **HTML Parsing:** `BeautifulSoup4`
* **Deployment:** Render
* **Version Control:** Git

## API Endpoints

### Scrape a Page Title

This endpoint accepts a URL and returns the title of the webpage.

* **URL:** `/scrape-title/`
* **Method:** `POST`

#### Request Body:

You must send a JSON object with a single key, `url`.

```json
{
  "url": "https://github.com/aakarshjaindev"
}
```

#### Success Response (200 OK):

The API returns the original URL and the extracted title.

```json
{
  "url": "https://github.com/aakarshjaindev",
  "title": "aakarshjaindev (Aakarsh Jain) · GitHub"
}
```

#### Error Response (400 Bad Request):

If the URL is invalid or cannot be reached, the API returns a detailed error message.

```json
{
  "detail": "Could not fetch URL: ..."
}
```

## Live Demo

This application is deployed on Render and is available for live testing.

[https://scraper-api-0dqg.onrender.com](https://scraper-api-0dqg.onrender.com)

## How to Run Locally

To get a local copy up and running, follow these simple steps.

1. **Clone the repository:**

   ```sh
   git clone https://github.com/aakarshjaindev/scraper_api.git
   cd scraper_api
   ```

2. **Create and activate the virtual environment using `uv`:**

   ```sh
   uv venv --seed
   # On Windows
   .\.venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```sh
   uv pip install -r requirements.txt
   ```

4. **Run the application server:**

   ```sh
   uvicorn main:app --reload
   ```

5. **Access the API documentation:**
   Navigate to `http://127.0.0.1:8000/docs` in your web browser to see the interactive FastAPI documentation and test the endpoint directly.

## License

Distributed under the MIT License. See `LICENSE` for more information.
