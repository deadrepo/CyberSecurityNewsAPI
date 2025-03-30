r"""
 ---------------------
| Developed by Ikmal |
 --------------------
         \ (•◡•) /
          \      /
            ——
            |  |
           _|  |_
"""


from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

app = Flask(__name__)

def fetch_news():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Referer": "https://www.google.com/",
        "Accept-Language": "en-US,en;q=0.9"
    }

    url = "https://www.bleepingcomputer.com/"
    news_data = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        for n in soup.find_all("div", class_="bc_latest_news_text"):
            title_tag = n.find("h4")
            desc_tag = n.find("p")
            date_tag = n.find("li", class_="bc_news_date")

            if title_tag and desc_tag and date_tag:
                article = {
                    "title": title_tag.get_text(strip=True),
                    "date": date_tag.get_text(strip=True),
                    "source": "Bleeping Computer",
                    "description": desc_tag.get_text(strip=True),
                    "link": title_tag.find("a")["href"]
                }
                news_data.append(article)
    except requests.RequestException as e:
        return [{"error": "Failed to fetch news", "details": str(e)}]

    return news_data

@app.route("/api/news", methods=["GET"])  # Use /api/news
def get_news():
    return jsonify(fetch_news())

# No app.run() needed for Vercel
