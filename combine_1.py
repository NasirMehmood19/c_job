# import feedparser
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from datetime import datetime, timezone, timedelta
# from dateutil import parser
# import html

# DATABASE_URL = "postgresql://instaxrss_user:QGBb5ALqiBraZtjt1c1zoifa4Kf4G1Tu@dpg-cv7sqcqj1k6c739htp00-a.oregon-postgres.render.com/instaxrss"

# def get_db_connection():
#     return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

# specific_feed_urls = [
#     "https://hollywoodlife.com/feed/",
#     "https://www.etonline.com/style/lifestyle/rss",
#     "http://rss.cnn.com/rss/edition_entertainment.rss",
#     "https://feeds.feedburner.com/GeoEntertainment-GeoTvNetwork",
#     "https://www.dailymail.co.uk/tvshowbiz/index.rss",
#     "https://eol-feeds.eonline.com/rssfeed/us/top_stories",
#     "https://www.usmagazine.com/category/entertainment/feed/",
#     "https://www.mirror.co.uk/lifestyle/?service=rss",
#     "https://feeds.feedburner.com/variety/headlines",
#     "https://feeds.feedburner.com/com/Yeor"
# ]

# def fetch_rss_feed_data(feed_urls):
#     articles = []
#     for url in feed_urls:
#         try:
#             feed = feedparser.parse(url)
#             channel_name = feed.feed.get('title', 'Unknown Channel')

#             for entry in feed.entries:
#                 try:
#                     title = html.unescape(entry.get('title', 'No Title'))
#                     link = entry.get('link', 'No Link')
#                     pub_date_str = entry.get('published', entry.get('updated', None))
#                     pub_date = parser.parse(pub_date_str) if pub_date_str else None

#                     if pub_date:
#                         time_diff = datetime.now(timezone.utc) - pub_date
#                         if time_diff > timedelta(hours=24):
#                             continue

#                     formatted_pub_date = pub_date.strftime('%Y-%m-%d %H:%M') if pub_date else 'Unknown Date'

#                     articles.append({
#                         'title': title,
#                         'link': link,
#                         'pubDate': formatted_pub_date,
#                         'channel': channel_name
#                     })
#                 except Exception as e:
#                     print(f"Error processing article from {channel_name}. Error: {e}")
#         except Exception as e:
#             print(f"Error parsing feed from URL: {url}. Error: {e}")

#     return articles

# def store_articles():
#     articles = fetch_rss_feed_data(specific_feed_urls)
#     conn = get_db_connection()
#     cur = conn.cursor()

#     for article in articles:
#         try:
#             cur.execute(
#                 "INSERT INTO rrss_links (title, link, pubDate, channel) VALUES (%s, %s, %s, %s) ON CONFLICT (link) DO NOTHING",
#                 (article['title'], article['link'], article['pubDate'], article['channel'])
#             )
#         except Exception as e:
#             print(f"Error inserting article: {e}")

#     conn.commit()
#     cur.close()
#     conn.close()
#     print("Articles stored successfully.")

# if __name__ == "__main__":
#     store_articles()
