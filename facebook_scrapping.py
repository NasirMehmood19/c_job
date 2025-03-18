
# import time
# import pickle
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse
# from datetime import datetime
# import os

# # PostgreSQL Connection URL (Render external DB)
# DATABASE_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# # --- Instagram Scraper (Headless) ---

# insta_options = Options()
# insta_options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")  # Use Chromium
# insta_options.add_argument("--headless=new")
# insta_options.add_argument("--disable-gpu")
# insta_options.add_argument("--window-size=375,812")
# insta_options.add_argument("--disable-blink-features=AutomationControlled")
# insta_options.add_argument(
#     "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) "
#     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36"
# )

# # Setup ChromeDriver service
# service = Service(os.getenv("CHROMEDRIVER_BIN", "/usr/bin/chromedriver"))  # Use correct Chromedriver path
# driver = webdriver.Chrome(service=service, options=insta_options)

# #  --- Facebook Scraper ---
# facebook_pages = [
#     {"name": "Meghan", "url": "https://www.facebook.com/MeghanDuchessOfSussex/"},
#     {"name": "The Royal Family", "url": "https://www.facebook.com/TheBritishMonarchy/"},
#     {"name": "Prince and Princess of Wales", "url": "https://www.facebook.com/WilliamAndCatherinePDA/"},
#     {"name": "Kim Kardashian", "url": "https://www.facebook.com/KimKardashian/"},
#     {"name": "Justin Bieber", "url": "https://www.facebook.com/JustinBieber/"},
#     {"name": "Hailey Bieber", "url": "https://www.facebook.com/HaileyBaldwin/"},
#     {"name": "Kanye West", "url": "https://www.facebook.com/kanyewest/"},
#     {"name": "Jennifer Aniston", "url": "https://www.facebook.com/JenniferAniston/"},
#     {"name": "Jennifer Garner", "url": "https://www.facebook.com/JenniferGarner/"},
#     {"name": "JLo", "url": "https://www.facebook.com/jenniferlopez/"},
#     {"name": "Cardi B", "url": "https://www.facebook.com/cardib/"},
#     {"name": "Soompi", "url": "https://www.facebook.com/soompi/"},
#     {"name": "Katy Perry", "url": "https://www.facebook.com/katyperry/"},
#     {"name": "Selena Gomez", "url": "https://www.facebook.com/Selena/"},
#     {"name": "Paris Hilton", "url": "https://www.facebook.com/ParisHilton/"},
#     {"name": "Taylor Swift", "url": "https://www.facebook.com/TaylorSwift/"},
#     {"name": "Zendaya", "url": "https://www.facebook.com/Zendaya/"},
#     {"name": "Kylie Jenner", "url": "https://www.facebook.com/KylieJenner/"},
#     {"name": "Miley Cyrus", "url": "https://www.facebook.com/MileyCyrus/"},
#     {"name": "Jenna Ortega", "url": "https://www.facebook.com/Jenna0rtega/"},
#     {"name": "Netflix", "url": "https://www.facebook.com/netflixus/"},
#     {"name": "Tom Cruise", "url": "https://www.facebook.com/officialtomcruise/"},
#     {"name": "Tom Hanks", "url": "https://www.facebook.com/TomHanks/"},
#     {"name": "Robert De Niro", "url": "https://www.facebook.com/groups/51483531168/"},
#     {"name": "Al Pacino", "url": "https://www.facebook.com/groups/505486102813510/"},
#     {"name": "Vin Diesel", "url": "https://www.facebook.com/VinDiesel/"},
#     {"name": "Robert Downey Jr.", "url": "https://www.facebook.com/robertdowneyjr/"},
#     {"name": "Selena Gomez", "url": "https://www.instagram.com/selenagomez/"}
# ]

# def normalize_url(url):
#     parsed_url = urlparse(url)
#     netloc = parsed_url.netloc.replace("web.", "www.").replace("www.", "")
#     return f"{parsed_url.scheme}://www.{netloc}{parsed_url.path}"

# def get_facebook_posts(page_name, url):
#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()
#     posts = soup.find_all("a", href=True)
#     new_posts = []
#     for post in posts:
#         href = post['href']
#         if any(pattern in href for pattern in ["/posts/", "/reels/"]):
#             full_link = href #"https://www.facebook.com" + 
#             new_posts.append({"page_name": page_name, "link": normalize_url(full_link)})
#     return new_posts[:1] if new_posts else []

# def store_facebook_posts(posts):
#     conn = psycopg2.connect(DATABASE_URL)
#     cursor = conn.cursor()
#     for post in posts:
#         cursor.execute("INSERT INTO facebook_links (page_name, link) VALUES (%s, %s) " 
#                        "ON CONFLICT (page_name) DO UPDATE SET link = EXCLUDED.link;",
#                        (post["page_name"], post["link"]))
#     conn.commit()
#     cursor.close()
#     conn.close()

# def fetch_all_posts():
#     all_posts = []
#     for page in facebook_pages:
#         posts = get_facebook_posts(page["name"], page["url"])
#         if posts:
#             store_facebook_posts(posts)
#     print(f"✅ Stored/Updated the latest post in the database.")

# if __name__ == "__main__":
#     # while True:
#     fetch_all_posts()
#         # print("Waiting 20 minutes before next scrape...")
#         # time.sleep(60 *20)






import time
import pickle
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

# PostgreSQL Connection URL (Render external DB)
DATABASE_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# --- Instagram Scraper (Headless) ---

# Configure Selenium WebDriver options for Instagram (headless mode)
insta_options = Options()
insta_options.add_argument("--headless=new")  # No browser window appears
insta_options.add_argument("--disable-gpu")
insta_options.add_argument("--window-size=375,812")
insta_options.add_argument("--disable-blink-features=AutomationControlled")
insta_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36"
)

#  --- Facebook Scraper ---
facebook_pages = [
    {"name": "Kim Kardashian", "url": "https://www.facebook.com/KimKardashian/"},
    {"name": "Kylie Jenner", "url": "https://www.facebook.com/KylieJenner/"},
    {"name": "Rihanna", "url": "https://www.facebook.com/Rihanna/"},
    {"name": "Kanye West", "url": "https://www.facebook.com/KanyeWest/"},
    {"name": "Justin Bieber", "url": "https://www.facebook.com/JustinBieber/"},
    {"name": "Hailey Bieber", "url": "https://www.facebook.com/HaileyBaldwin/"},
    {"name": "Selena Gomez", "url": "https://www.facebook.com/Selena/"},
    {"name": "Henry Cavill", "url": "https://www.facebook.com/henrycavill/"},
    {"name": "Emma Roberts", "url": "https://www.facebook.com/EmmaRoberts/"},
    {"name": "Reese Witherspoon", "url": "https://www.facebook.com/ReeseWitherspoon/"},
    {"name": "Shakira", "url": "https://www.facebook.com/Shakira/"},
    {"name": "Beyoncé", "url": "https://www.facebook.com/Beyonce/"},
    {"name": "Lady Gaga", "url": "https://www.facebook.com/LadyGaga/"},
    {"name": "Ariana Grande", "url": "https://www.facebook.com/ArianaGrande/"},
    {"name": "Billie Eilish", "url": "https://www.facebook.com/BillieEilish/"},
    {"name": "Miley Cyrus", "url": "https://www.facebook.com/MileyCyrus/"},
    {"name": "Taylor Swift", "url": "https://www.facebook.com/TaylorSwift/"},
    {"name": "Gigi Hadid", "url": "https://www.facebook.com/officialgigihadid/"},
    {"name": "Zayn Malik", "url": "https://www.facebook.com/Zayn/"},
    {"name": "Tom Cruise", "url": "https://www.facebook.com/officialtomcruise/"},
    {"name": "Meghan Markle", "url": "https://www.facebook.com/MeghanDuchessOfSussex/"},
    {"name": "Kendall Jenner", "url": "https://www.facebook.com/KendallJenner/"},
    {"name": "Kris Jenner", "url": "https://www.facebook.com/KrisJenner/"},
    {"name": "Khloé Kardashian", "url": "https://www.facebook.com/KhloeKardashian/"},
    {"name": "Kourtney Kardashian", "url": "https://www.facebook.com/KourtneyKardashian/"},
    {"name": "Jeremy Renner", "url": "https://www.facebook.com/JeremyRennerOfficial/"},
    {"name": "Chris Hemsworth", "url": "https://www.facebook.com/ChrisHemsworth/"},
    {"name": "Ed Sheeran", "url": "https://www.facebook.com/EdSheeranMusic/"},
    {"name": "Anne Hathaway", "url": "https://www.facebook.com/Hathaway/"},
    {"name": "Jennifer Lopez", "url": "https://www.facebook.com/JenniferLopez/"},
    {"name": "Jennifer Garner", "url": "https://www.facebook.com/JenniferGarner/"},
    {"name": "Jennifer Aniston", "url": "https://www.facebook.com/JenniferAniston/"},
    {"name": "Jennifer Lawrence", "url": "https://www.facebook.com/JenniferLawrence/"}
]


def normalize_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc.replace("web.", "www.").replace("www.", "")
    return f"{parsed_url.scheme}://www.{netloc}{parsed_url.path}"

def get_facebook_posts(page_name, url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    posts = soup.find_all("a", href=True)
    new_posts = []
    for post in posts:
        href = post['href']
        if any(pattern in href for pattern in ["/posts/", "/reels/"]):
            full_link = href #"https://www.facebook.com" + 
            new_posts.append({"page_name": page_name, "link": normalize_url(full_link)})
    return new_posts[:1] if new_posts else []

def store_facebook_posts(posts):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    for post in posts:
        cursor.execute("INSERT INTO facebook_links (page_name, link) VALUES (%s, %s) " 
                       "ON CONFLICT (link) DO NOTHING",
                       (post["page_name"], post["link"]))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_all_posts():
    all_posts = []
    for page in facebook_pages:
        posts = get_facebook_posts(page["name"], page["url"])
        if posts:
            store_facebook_posts(posts)
    print(f"✅ Stored/Updated the latest post in the database.")

if __name__ == "__main__":
    while True:
       
        fetch_all_posts()
        print("Waiting 20 minutes before next scrape...")
        time.sleep(60 *20)
