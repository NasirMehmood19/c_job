


import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import os

# PostgreSQL Connection URL (Render external DB)
DATABASE_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# Selenium WebDriver Setup (Headless Mode)
insta_options = Options()
insta_options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")  # Use Chromium
insta_options.add_argument("--headless=new")
insta_options.add_argument("--disable-gpu")
insta_options.add_argument("--window-size=375,812")
insta_options.add_argument("--disable-blink-features=AutomationControlled")
insta_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36"
)

# Setup ChromeDriver service
service = Service(os.getenv("CHROMEDRIVER_BIN", "/usr/bin/chromedriver"))  # Use correct Chromedriver path
driver = webdriver.Chrome(service=service, options=insta_options)



def create_table():
    """Create fb_links table if it doesn't exist."""
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fb_links (
            id SERIAL PRIMARY KEY,
            link TEXT UNIQUE,
            page_name TEXT,
            timestamp TEXT
        );
    """)
    conn.commit()
    conn.close()

def get_facebook_links():
    """Fetch all stored Facebook links from facebook_links table."""
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT link FROM facebook_links")
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links

def start_driver():
    """Start and return a fresh Selenium WebDriver instance."""
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=insta_options)

def extract_page_details(driver, link):
    """Extract timestamp and page name from a Facebook post URL."""
    try:
        driver.get(link)

        # Wait for timestamp
        timestamp_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/posts/') or contains(@href, '/videos/') or contains(@href, '/reels/')]"))
        )
        timestamp = timestamp_element.text.strip()

        # Try multiple XPaths to extract the correct page name
        possible_xpaths = [
            "//div[@role='banner']//h1",  # Page name in banner
            "//h2/span",  # General h2 title
            "//h1"  # Standard title
        ]
        
        page_name = None
        for xpath in possible_xpaths:
            try:
                page_name_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                page_name = page_name_element.text.strip()
                if page_name and page_name.lower() not in ["video", "videos"]:
                    break  # Stop if we find a valid page name
            except:
                continue  # Try the next XPath if one fails

        if not page_name:
            raise Exception("Page name not found!")

        print(f"✅ Page: {page_name}, Timestamp for {link}: {timestamp}")

    except Exception as e:
        print(f"❌ Error extracting details for {link}: {e}")
        return None, None

    return page_name, timestamp

def save_to_db(link, page_name, timestamp):
    """Insert link, page_name, and timestamp into fb_links table."""
    if timestamp and page_name:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO fb_links (link, page_name, timestamp) VALUES (%s, %s, %s) ON CONFLICT (link) DO UPDATE SET page_name = EXCLUDED.page_name, timestamp = EXCLUDED.timestamp",
                (link, page_name, timestamp)
            )
            conn.commit()
            print(f"✅ Saved to DB: {link}, Page: {page_name}")
        except Exception as e:
            print(f"❌ Database Error: {e}")
        finally:
            conn.close()

def clear_fb_links():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fb_links")
    conn.commit()
    conn.close()       

def main():
    create_table()  # Ensure fb_links table exists
    clear_fb_links()
    links = get_facebook_links()  # Get links from facebook_links table
    print(f"🔗 Found {len(links)} links to process.")

    driver = start_driver()  # Start Selenium WebDriver

    for link in links:
        try:
            page_name, timestamp = extract_page_details(driver, link)  # Extract page name & timestamp
            
            if page_name and timestamp:
                save_to_db(link, page_name, timestamp)  # Store in DB
                
        except InvalidSessionIdException:
            print("⚠️ Browser session lost! Restarting WebDriver...")
            driver.quit()
            driver = start_driver()  # Restart Selenium WebDriver
        
        except WebDriverException as e:
            print(f"⚠️ WebDriver Error: {e}. Restarting browser...")
            driver.quit()
            time.sleep(5)  # Wait before restarting to prevent frequent crashes
            driver = start_driver()

    driver.quit()  # Ensure driver is closed after processing all links

if __name__ == "__main__":
    main()
