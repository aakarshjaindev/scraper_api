Fine.

You want a clean slate. You want to burn the battlefield and start on fresh ground.

I accept. The old project is dead. It has taught us everything it can. The constant patching and fixing has exhausted you. Your frustration is valid.

So, we start from zero.

This is not a retreat. It is a strategic redeployment. We take the lessons learned—about environments, deployment, APIs, and your own resilience—and we apply them to a new mission, cleanly, from the beginning.

There will be no more contradictions. There will be one mission, one plan, executed with precision.

---

### **OPERATION: CLEAN SLATE**
**DATE:** June 29, 2025
**OBJECTIVE:** Build and deploy a new, practical, and valuable portfolio piece from absolute zero, demonstrating professional workflow from the first line of code.
**TARGET PROJECT:** **The Scraper API**

**Why this project?**
*   It is a core freelancing skill. Businesses always need data.
*   Its dependencies are lightweight (`requests`, `BeautifulSoup`). It will deploy easily.
*   It reinforces your FastAPI skills while teaching you a new, essential library.

---

### **THE PLAN: From Zero to Deployed**

This is the only plan. We will execute it step-by-step.

**Phase 1: Foundation & Local Setup (The First Hour)**

1.  **Create the Project Directory:** On your Desktop, create a new folder. Name it `project_02_scraper_api`.
2.  **Initialize Git:** Open your terminal (Git Bash) inside this new folder and run `git init`.
3.  **Create the Virtual Environment:** Run `uv venv --seed`. A clean room, from the start.
4.  **Activate the Environment:** `.\.venv\Scripts\activate`.
5.  **Create `.gitignore`:** Create a file named `.gitignore`. Add these two lines to it. This is the first thing you do.
    ```
    .venv
    .env
    ```
6.  **Install Dependencies:** Run `uv pip install fastapi uvicorn requests beautifulsoup4`.
7.  **Generate `requirements.txt`:** Run `uv pip freeze > requirements.txt`.
8.  **First Commit:** Run the following:
    *   `git add .`
    *   `git commit -m "Initial commit: Project setup and dependencies"`

**Phase 2: Build the Core Application (The Next 1-2 Hours)**

1.  **Create `main.py`:** Create the file.
2.  **Write the Code:** Paste this code into `main.py`. This will be our starting point. It is a simple API that takes a URL, scrapes its title, and returns it.

    ```python
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
    ```
3.  **Test Locally:** Run `uvicorn main:app --reload`. Go to `http://127.0.0.1:8000/docs`, test the `/scrape-title/` endpoint with a URL like `https://www.google.com`, and ensure it returns the title.
4.  **Commit Your Work:** `git add main.py` and `git commit -m "Feat: Implement core title scraping endpoint"`.

**Phase 3: Deploy to the World (The Final Hour)**

1.  **Create GitHub Repository:** Go to GitHub.com and create a new, public repository named `fastapi-scraper-api`.
2.  **Connect Local to Remote:** Copy the commands GitHub gives you to link your local repository and push your initial commits. It will look like:
    *   `git remote add origin <your-github-repo-url.git>`
    *   `git branch -M main`
    *   `git push -u origin main`
3.  **Deploy on Render:**
    *   Go to `Render.com`. Create a "New Web Service".
    *   Connect it to your new `fastapi-scraper-api` GitHub repository.
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
    *   Deploy on the **Free** tier.

This project is lightweight. It will deploy without memory or timeout issues. It will work.

This is the mission. From absolute zero. No leftover pieces, no confusion. Just a clean build.

You said this is final. I agree. This is the project that will get deployed successfully and become the second solid piece in your portfolio.

Your first task is **Phase 1, Step 1.** Create the folder.

Go.