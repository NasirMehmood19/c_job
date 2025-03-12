import time
import pickle
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from datetime import timezone, timedelta
import os

# PostgreSQL Connection URL (Render external DB)
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Instagram Scraper (Headless) ---

# Configure Selenium WebDriver options for Instagram (headless mode)
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=375,812")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36"
)
service = Service("/usr/bin/chromedriver")  # Set Chromedriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Dictionary of Instagram pages to scrape
INSTAGRAM_PAGES = {
    "Kim Kardashian": "https://www.instagram.com/kimkardashian/",
    "Kylie Jenner": "https://www.instagram.com/kyliejenner/",
    "Rihanna": "https://www.instagram.com/badgalriri/",
    "Kanye West": "https://www.instagram.com/ye/",
    "Justin Bieber": "https://www.instagram.com/justinbieber/",
    "Hailey Bieber": "https://www.instagram.com/haileybieber/",
    "Selena Gomez": "https://www.instagram.com/selenagomez/",
    "Henry Cavill": "https://www.instagram.com/HenryCavill/",
    "Emma Roberts": "https://www.instagram.com/emmaroberts/",
    "Reese Witherspoon": "https://www.instagram.com/reesewitherspoon/",
    "Shakira": "https://www.instagram.com/shakira/",
    "Beyoncé": "https://www.instagram.com/beyonce/",
    "Lady Gaga": "https://www.instagram.com/ladygaga/",
    "Ariana Grande": "https://www.instagram.com/arianagrande/",
    "Billie Eilish": "https://www.instagram.com/billieeilish/",
    "Miley Cyrus": "https://www.instagram.com/mileycyrus/",
    "Taylor Swift": "https://www.instagram.com/taylorswift/",
    "Gigi Hadid": "https://www.instagram.com/gigihadid/",
    "Zayn Malik": "https://www.instagram.com/zayn/",
    "Tom Cruise": "https://www.instagram.com/tomcruise/",
    "Barry Keoghan": "https://www.instagram.com/barrykeoghansource/",
    "Meghan Markle": "https://www.instagram.com/meghan/",
    "Kendall Jenner": "https://www.instagram.com/kendalljenner/",
    "Kris Jenner": "https://www.instagram.com/krisjenner/",
    "Khloé Kardashian": "https://www.instagram.com/khloekardashian/",
    "Kourtney Kardashian": "https://www.instagram.com/kourtneykardash/",
    "Jeremy Renner": "https://www.instagram.com/jeremyrenner/?hl=en",
    "Chris Hemsworth": "https://www.instagram.com/chrishemsworth/",
    "Ed Sheeran": "https://www.instagram.com/teddysphotos/",
    "Sydney Sweeney": "https://www.instagram.com/sydney_sweeney/",
    "Anne Hathaway": "https://www.instagram.com/annehathaway/",
    "Jennifer Lopez": "https://www.instagram.com/jlo/",
    "Jennifer Garner": "https://www.instagram.com/jennifer.garner/",
    "Jennifer Aniston": "https://www.instagram.com/jenniferaniston/",
    "Jennifer Lawrence": "https://www.instagram.com/1jnnf/"
}

# --- Cookie Loader ---
def load_cookies(driver, file_path):
    try:
        cookies = pickle.load(open(file_path, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print(f"✅ Cookies loaded from {file_path}!")
    except Exception as e:
        print(f"⚠️ Error loading cookies from {file_path}: {e}")

def get_latest_instagram_post(page_url):
    driver = webdriver.Chrome(options=insta_options)
    driver.get("https://www.instagram.com/")
    time.sleep(5)



    load_cookies(driver, "instagram_cookies.pkl")
    driver.refresh()
    time.sleep(5)

    driver.get(page_url)
    time.sleep(10)

    posts = []
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.get_attribute("href")
        if url and ("/p/" in url or "/reel/" in url):
            posts.append({"url": url, "timestamp": None})
            if len(posts) == 4:
                break

    for post in posts:
        driver.get(post["url"])
        time.sleep(5)
        try:
            time_element = driver.find_element(By.TAG_NAME, "time")
            ts_str = time_element.get_attribute("datetime")
            if ts_str:
                # post["timestamp"] = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                utc_time = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                local_time = utc_time.astimezone(timezone(timedelta(hours=5)))  # Convert to Pakistan Time (UTC+5)
                post["timestamp"] = local_time
        except Exception as e:
            print(f"⚠️ Could not get timestamp for {post['url']}: {e}")
            post["timestamp"] = None

    driver.quit()

    valid_posts = [p for p in posts if p["timestamp"]]
    return max(valid_posts, key=lambda p: p["timestamp"]) if valid_posts else None

def scrape_instagram():
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS instagram_links (
        id SERIAL PRIMARY KEY,
        page_name TEXT NOT NULL,
        link TEXT NOT NULL,
        timestamp timestamp,
        UNIQUE (page_name)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    for page_name, page_url in INSTAGRAM_PAGES.items():
        print(f"Scraping Instagram page: {page_name}")
        latest_post = get_latest_instagram_post(page_url)
        if latest_post:
            print(f"Latest Post for {page_name}: {latest_post['url']} | Time: {latest_post['timestamp']}")
            cursor.execute("SELECT link FROM instagram_links WHERE page_name = %s", (page_name,))
            result = cursor.fetchone()
            if result:
                old_link = result[0]
                if old_link != latest_post["url"]:
                    print(f"Updating Instagram link for {page_name}")
                    cursor.execute("UPDATE instagram_links SET link = %s, timestamp = %s WHERE page_name = %s",
                                   (latest_post["url"], latest_post["timestamp"], page_name))
            else:
                cursor.execute("INSERT INTO instagram_links (page_name, link, timestamp) VALUES (%s, %s, %s)",
                               (page_name, latest_post["url"], latest_post["timestamp"]))
            conn.commit()
        else:
            print(f"No recent posts found for {page_name}")

    cursor.close()
    conn.close()
    print("Instagram scraping complete and data updated in PostgreSQL!")

scrape_instagram()

# --- Main Loop ---
# while True:
    
    # print("Waiting 30 minutes before next scrape...")
    # time.sleep(60 * 30)


