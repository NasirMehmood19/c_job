# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time

# # Set up Selenium WebDriver
# options = Options()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Define categories (category numbers from Google Trends)
# categories = {
#     "auto and vehicles": 1,
#     "Beauty": 2,
#     "Business": 3,
#     "Entertainment": 4
# }

# # Loop through categories
# for category_name, category_id in categories.items():
#     url = f"https://trends.google.com/trending?geo=PK&hours=4&category={category_id}"
#     driver.get(url)
#     time.sleep(5)  # Allow JavaScript to load

#     # Extract trending topics
#     trending_topics = driver.find_elements(By.CLASS_NAME, "GLyLe")

#     # Print category header
#     print(f"\n🔥 Trending in Pakistan ({category_name}) - Last 4 Hours 🔥\n")
#     for i, topic in enumerate(trending_topics, 1):
#         print(f"{i}. {topic.text}")

# # Close the driver
# driver.quit()


# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# from tabulate import tabulate

# # Set up Selenium WebDriver
# options = Options()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Open Google Trends "Trending Now" for Pakistan (Business & Finance category)
# url = [

#         {"https://trends.google.com/trending?geo=PK&hours=4&category=4"},
#         {"https://trends.google.com/trending?geo=PK&hours=4&category=3"}
# ]
# driver.get(url)
# time.sleep(5)  # Allow JavaScript to load

# # Extract elements
# trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")  # Titles
# search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")  # Volume (e.g., 500+)
# percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")  # Percentage (e.g., 800%)
# started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")  # Start time (e.g., 2 hours ago)

# # Extract data
# data = []
# for i in range(len(trending_topics)):
#     data.append([
#         trending_topics[i].text, 
#         search_volume[i].text if i < len(search_volume) else "N/A",
#         percent_change[i].text if i < len(percent_change) else "N/A",
#         started_time[i].text if i < len(started_time) else "N/A",
#         "✅ Active"
#     ])

# # Convert list to DataFrame
# df = pd.DataFrame(data, columns=["Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

# # Print table format
# print("\n🔥 Trending Searches in Pakistan (Business & Finance) - Last 4 Hours 🔥\n")
# print(tabulate(df, headers="keys", tablefmt="pretty"))

# # Close the driver
# driver.quit()





















# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# from tabulate import tabulate

# # Set up Selenium WebDriver
# options = Options()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Define multiple URLs
# urls = [
#     {"category": "Entertainment", "url": "https://trends.google.com/trending?geo=AU&category=3&hours=24"},
#     {"category": "Business", "url": "https://trends.google.com/trending?geo=AU&category=4&hours=24"}
# ]

# # Store extracted data
# data = []

# # Loop through each URL
# for entry in urls:
#     category = entry["category"]
#     url = entry["url"]

#     driver.get(url)
#     time.sleep(5)  # Allow JavaScript to load

#     # Extract elements
#     trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")  # Titles
#     search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")  # Volume (e.g., 500+)
#     percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")  # Percentage (e.g., 800%)
#     started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")  # Start time (e.g., 2 hours ago)

#     # Append extracted data
#     for i in range(len(trending_topics)):
#         data.append([
#             category,
#             trending_topics[i].text,
#             search_volume[i].text if i < len(search_volume) else "N/A",
#             percent_change[i].text if i < len(percent_change) else "N/A",
#             started_time[i].text if i < len(started_time) else "N/A",
#             "✅ Active"
#         ])

# # Close the driver
# driver.quit()

# # Convert list to DataFrame
# df = pd.DataFrame(data, columns=["Category", "Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

# # Print table format
# print("\n🔥 Trending Searches in Pakistan - Last 4 Hours 🔥\n")
# print(tabulate(df, headers="keys", tablefmt="pretty"))




















# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# from tabulate import tabulate

# # Set up Selenium WebDriver
# options = Options()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Define specific URLs for different countries and categories
# urls = [
#     {"country": "Pakistan", "category": "Business", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=3"},
#     {"country": "Pakistan", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=4"},
#     {"country": "Australia", "category": "Business", "url": "https://trends.google.com/trending?geo=AU&category=3&hours=24"}
#     # {"country": "United States", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=US&hours=4&category=4"},
#     # {"country": "India", "category": "Business", "url": "https://trends.google.com/trending?geo=IN&hours=4&category=3"},
#     # {"country": "India", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=IN&hours=4&category=4"},
# ]

# # Store extracted data
# data = []

# # Loop through each country's URL
# for item in urls:
#     country = item["country"]
#     category = item["category"]
#     url = item["url"]

#     driver.get(url)
#     time.sleep(5)  # Allow JavaScript to load

#     # Extract elements
#     trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")  # Titles
#     search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")  # Volume (e.g., 500+)
#     percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")  # Percentage (e.g., 800%)
#     started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")  # Start time (e.g., 2 hours ago)

#     # Append extracted data
#     for i in range(len(trending_topics)):
#         data.append([
#             country,
#             category,
#             trending_topics[i].text,
#             search_volume[i].text if i < len(search_volume) else "N/A",
#             percent_change[i].text if i < len(percent_change) else "N/A",
#             started_time[i].text if i < len(started_time) else "N/A",
#             "✅ Active"
#         ])

# # Close the driver
# driver.quit()

# # Convert list to DataFrame
# df = pd.DataFrame(data, columns=["Country", "Category", "Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

# # Print table format
# print("\n🔥 Trending Searches in Multiple Countries - Last 4 Hours 🔥\n")
# print(tabulate(df, headers="keys", tablefmt="pretty"))



















# import pandas as pd
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# from tabulate import tabulate

# # PostgreSQL Database Credentials
# DB_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# # Set up Selenium WebDriver
# options = Options()
# options.add_argument("--headless")  # Run in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Define specific URLs for different countries and categories
# urls = [
#     {"country": "Pakistan", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=1"},
#     {"country": "Pakistan", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=2"},
#     {"country": "Pakistan", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=3"},
#     {"country": "Pakistan", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=4"},

#     {"country": "Australia", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=AU&category=1&hours=4"},
#     {"country": "Australia", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=AU&category=2&hours=4"},
#     {"country": "Australia", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=AU&category=3&hours=4"},
#     {"country": "Australia", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=AU&category=4&hours=4"}
# ]

# # Store extracted data
# data = []

# # Loop through each country's URL
# for item in urls:
#     country = item["country"]
#     category = item["category"]
#     url = item["url"]

#     driver.get(url)
#     time.sleep(5)  # Allow JavaScript to load

#     # Extract elements
#     trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")  # Titles
#     search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")  # Volume (e.g., 500+)
#     percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")  # Percentage (e.g., 800%)
#     started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")  # Start time (e.g., 2 hours ago)

#     # Append extracted data
#     for i in range(len(trending_topics)):
#         data.append([
#             country,
#             category,
#             trending_topics[i].text,
#             search_volume[i].text if i < len(search_volume) else "N/A",
#             percent_change[i].text if i < len(percent_change) else "N/A",
#             started_time[i].text if i < len(started_time) else "N/A",
#             "✅ Active"
#         ])

# # Close the driver
# driver.quit()

# # Convert list to DataFrame
# df = pd.DataFrame(data, columns=["Country", "Category", "Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

# # Print table format
# print("\n🔥 Trending Searches in Multiple Countries - Last 4 Hours 🔥\n")
# print(tabulate(df, headers="keys", tablefmt="pretty"))

# # Store Data in PostgreSQL
# conn = None  # Ensure conn is always defined
# try:
#     conn = psycopg2.connect(DB_URL)
#     cur = conn.cursor()

#     # Create table if not exists
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS trending_data (
#         id SERIAL PRIMARY KEY,
#         country TEXT,
#         category TEXT,
#         trending_search TEXT,
#         search_volume TEXT,
#         change_percentage TEXT,
#         started TEXT,
#         status TEXT,
#         scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
#     """
#     cur.execute(create_table_query)

#     # Insert data
#     insert_query = """
#     INSERT INTO trending_data (country, category, trending_search, search_volume, change_percentage, started, status)
#     VALUES (%s, %s, %s, %s, %s, %s, %s);
#     """
#     cur.executemany(insert_query, data)

#     conn.commit()
#     print("\n✅ Data successfully stored in PostgreSQL!")

# except Exception as e:
#     print("❌ Database Error:", e)

# finally:
#     if conn is not None:
#         cur.close()
#         conn.close()



































import pandas as pd
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from tabulate import tabulate
from datetime import datetime, timedelta
import re

# PostgreSQL Database Credentials
DB_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define specific URLs for different countries and categories
urls = [
    {"country": "Pakistan", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=1"},
    {"country": "Pakistan", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=2"},
    {"country": "Pakistan", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=3"},
    {"country": "Pakistan", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=PK&hours=4&category=4"},

    {"country": "Australia", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=AU&hours=4&category=1"},
    {"country": "Australia", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=AU&hours=4&category=2"},
    {"country": "Australia", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=AU&hours=4&category=3"},
    {"country": "Australia", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=AU&hours=4&category=4"},

    {"country": "New Zealand", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=NZ&hours=4&category=1"},
    {"country": "New Zealand", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=NZ&hours=4&category=2"},
    {"country": "New Zealand", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=NZ&hours=4&category=3"},
    {"country": "New Zealand", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=NZ&hours=4&category=4"},

    {"country": "Canada", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=CA&hours=4&category=1"},
    {"country": "Canada", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=CA&hours=4&category=2"},
    {"country": "Canada", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=CA&hours=4&category=3"},
    {"country": "Canada", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=CA&hours=4&category=4"},

    {"country": "United States", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=US&hours=4&category=1"},
    {"country": "United States", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=US&hours=4&category=2"},
    {"country": "United States", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=US&hours=4&category=3"},
    {"country": "United States", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=US&hours=4&category=4"},

    {"country": "United Kingdom", "category": "Auto and Vehicle", "url": "https://trends.google.com/trending?geo=GB&hours=4&category=1"},
    {"country": "United Kingdom", "category": "Beauty and Fashion", "url": "https://trends.google.com/trending?geo=GB&hours=4&category=2"},
    {"country": "United Kingdom", "category": "Business and finance", "url": "https://trends.google.com/trending?geo=GB&hours=4&category=3"},
    {"country": "United Kingdom", "category": "Entertainment", "url": "https://trends.google.com/trending?geo=GB&hours=4&category=4"},
]

# Store extracted data
# data = []

# # Loop through each URL
# for item in urls:
#     country, category, url = item["country"], item["category"], item["url"]
#     driver.get(url)
#     time.sleep(5)  # Allow JavaScript to load

#     trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")
#     search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")
#     percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")
#     started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")

#     for i in range(len(trending_topics)):
#         data.append([
#             country,
#             category,
#             trending_topics[i].text,
#             search_volume[i].text if i < len(search_volume) else "N/A",
#             percent_change[i].text if i < len(percent_change) else "N/A",
#             started_time[i].text if i < len(started_time) else "N/A",
#             "✅ Active"
#         ])

# # Close the driver
# driver.quit()

# # Convert list to DataFrame
# df = pd.DataFrame(data, columns=["Country", "Category", "Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

# print("\n🔥 Trending Searches in Multiple Countries - Last 4 Hours 🔥\n")
# print(tabulate(df, headers="keys", tablefmt="pretty"))

# # Store Data in PostgreSQL
# conn = None
# try:
#     conn = psycopg2.connect(DB_URL)
#     cur = conn.cursor()

#     # Create table if not exists
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS trending_data (
#             id SERIAL PRIMARY KEY,
#             country TEXT,
#             category TEXT,
#             trending_search TEXT,
#             search_volume TEXT,
#             change_percentage TEXT,
#             started TEXT,
#             status TEXT,
#             scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         );
#     """)

#     # Delete old data before inserting new data
#     cur.execute("DELETE FROM trending_data;")
#     conn.commit()

#     # Insert new data
#     insert_query = """
#     INSERT INTO trending_data (country, category, trending_search, search_volume, change_percentage, started, status)
#     VALUES (%s, %s, %s, %s, %s, %s, %s);
#     """
#     cur.executemany(insert_query, data)

#     conn.commit()
#     print("\n✅ Data successfully updated in PostgreSQL!")

# except Exception as e:
#     print("❌ Database Error:", e)

# finally:
#     if conn:
#         cur.close()
#         conn.close()






def parse_relative_time(text):
    now = datetime.now()
    if "minute" in text:
        minutes = int(re.findall(r'\d+', text)[0])
        return now - timedelta(minutes=minutes)
    elif "hour" in text:
        hours = int(re.findall(r'\d+', text)[0])
        return now - timedelta(hours=hours)
    elif "day" in text:
        days = int(re.findall(r'\d+', text)[0])
        return now - timedelta(days=days)
    else:
        return now  # fallback

data = []

# Loop through each URL
for item in urls:
    country, category, url = item["country"], item["category"], item["url"]
    driver.get(url)
    time.sleep(5)  # Allow JavaScript to load

    trending_topics = driver.find_elements(By.CLASS_NAME, "mZ3RIc")
    search_volume = driver.find_elements(By.CLASS_NAME, "lqv0Cb")
    percent_change = driver.find_elements(By.CLASS_NAME, "TXt85b")
    started_time = driver.find_elements(By.CLASS_NAME, "vdw3Ld")

    for i in range(len(trending_topics)):
        started_text = started_time[i].text if i < len(started_time) else "0 minutes ago"
        started_timestamp = parse_relative_time(started_text)

        data.append([
            country,
            category,
            trending_topics[i].text,
            search_volume[i].text if i < len(search_volume) else "N/A",
            percent_change[i].text if i < len(percent_change) else "N/A",
            started_timestamp,
            "✅ Active"
        ])

# Close the driver
driver.quit()

# Convert list to DataFrame
df = pd.DataFrame(data, columns=["Country", "Category", "Trending Search", "Search Volume", "Change (%)", "Started", "Status"])

print("\n🔥 Trending Searches in Multiple Countries - Last 4 Hours 🔥\n")
print(tabulate(df, headers="keys", tablefmt="pretty"))

# Store Data in PostgreSQL
conn = None
try:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS trending_data (
            id SERIAL PRIMARY KEY,
            country TEXT,
            category TEXT,
            trending_search TEXT,
            search_volume TEXT,
            change_percentage TEXT,
            started TIMESTAMP,
            status TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Delete old data before inserting new data
    cur.execute("DELETE FROM trending_data;")
    conn.commit()

    # Insert new data
    insert_query = """
    INSERT INTO trending_data (country, category, trending_search, search_volume, change_percentage, started, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    cur.executemany(insert_query, data)

    conn.commit()
    print("\n✅ Data successfully updated in PostgreSQL!")

except Exception as e:
    print("❌ Database Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()