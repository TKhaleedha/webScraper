import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h2")

        with open(output_file, "w", encoding="utf-8") as f:
            for idx, headline in enumerate(headlines, start=1):
                f.write(f"{idx}. {headline.get_text(strip=True)}\n")

        print(f" Headlines scraped and saved to {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
