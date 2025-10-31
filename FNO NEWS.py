import streamlit as st
import requests
import pandas as pd
import os


# Load API Key (Streamlit Secrets)
if "GOOGLE_API_KEY" in st.secrets:
API_KEY = st.secrets["GOOGLE_API_KEY"]
elif "GOOGLE_API_KEY" in os.environ:
API_KEY = os.environ["GOOGLE_API_KEY"]
else:
API_KEY = None


# NSE F&O Stocks List (Latest from NSE)
fno_stocks = [
"AARTIIND","ABB","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIPORTS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","ASTRAL","ATUL","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","BSOFT","CAMS","CANBK","CANFINHOME","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DIVISLAB","DLF","DRREDDY","EICHERMOT","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFCFIRSTB","IEX","IGL","INDHOTEL","INDIGO","INDUSINDBK","INDUSTOWER","INFY","IOC","IRCTC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","KOTAKBANK","LICI","LT","LTF","LTIM","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX","METROPOLIS","MOTHERSON","MPHASIS","MRF","MUTHOOTFIN","NAM-INDIA","NATIONALUM","NAUKRI","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT","PETRONET","PFC","PIDILITIND","PIIND","PNB","POWERGRID","PVRINOX","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","STAR","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]


# Streamlit UI
st.set_page_config(page_title="F&O Stock News App", layout="wide")
st.title("📈 F&O Stock News Feed — Google News API")
st.write("Live news on all NSE F&O stocks.")


if not API_KEY:
st.error("⚠️ API key not found. Add GOOGLE_API_KEY in .env file.")
st.stop()


# Sidebar
selected_stock = st.sidebar.selectbox("Select F&O Stock", sorted(fno_stocks))
st.sidebar.info("Showing latest headlines for selected stock.")


# Time period filters
import datetime as dt
periods = {
"1 Week": dt.date.today() - dt.timedelta(days=7),
"1 Month": dt.date.today() - dt.timedelta(days=30),
"3 Months": dt.date.today() - dt.timedelta(days=90),
"6 Months": dt.date.today() - dt.timedelta(days=180),
}
selected_period = st.sidebar.selectbox("Time Range", list(periods.keys()))
start_date = periods[selected_period]


# Google News API Endpoint
url = f"https://newsapi.org/v2/everything?q={selected_stock}%20NSE&from={start_date}&sortBy=publishedAt&apiKey={API_KEY}"


response = requests.get(url)


if response.status_code != 200:
st.error("Error fetching news. Check API key or quota.")
st.stop()


data = response.json()
articles = data.get("articles", [])


if not articles:
st.warning("No news found for this stock today.")
st.stop()


# Display Articles
for article in articles:
st.subheader(article["title"])
st.write(article["description"])
st.write(f"🕒 {article['publishedAt']}")
st.markdown(f"[Read Full Article]({article['url']})")
st.markdown("---")"""
Streamlit F&O Stock News App
---------------------------
This app fetches news for all NSE F&O stocks using the Google News API
and displays them in a dashboard.

Before running:
1️⃣ Sign up for a Google News API key at https://newsapi.org/
2️⃣ Create a file `.env` with:  GOOGLE_API_KEY=YOUR_API_KEY
3️⃣ Install dependencies:
   pip install streamlit pandas requests python-dotenv

Run the app:
   streamlit run fno_news_app.py

Deploy on GitHub + Streamlit Cloud by pushing this file and adding requirements.txt
"""

import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load API Key
env_path = ".env"
if os.path.exists(env_path):
    load_dotenv(env_path)
API_KEY = os.getenv("GOOGLE_API_KEY")

# NSE F&O Stocks List (Latest from NSE)
fno_stocks = [
"AARTIIND","ABB","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIPORTS","ALKEM","AMBUJACEM","APOLLOHOSP","ASIANPAINT","ASTRAL","ATUL","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","BSOFT","CAMS","CANBK","CANFINHOME","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DIVISLAB","DLF","DRREDDY","EICHERMOT","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRINFRA","GODREJCP","GODREJPROP","GRASIM","HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER","HINDPETRO","HINDUNILVR","IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFCFIRSTB","IEX","IGL","INDHOTEL","INDIGO","INDUSINDBK","INDUSTOWER","INFY","IOC","IRCTC","ITC","JINDALSTEL","JSWSTEEL","JUBLFOOD","KOTAKBANK","LICI","LT","LTF","LTIM","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX","METROPOLIS","MOTHERSON","MPHASIS","MRF","MUTHOOTFIN","NAM-INDIA","NATIONALUM","NAUKRI","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT","PETRONET","PFC","PIDILITIND","PIIND","PNB","POWERGRID","PVRINOX","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","STAR","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UPL","VEDL","VOLTAS","WIPRO","ZEEL"]

# Streamlit UI
st.set_page_config(page_title="F&O Stock News App", layout="wide")
st.title("📈 F&O Stock News Feed — Google News API")
st.write("Live news on all NSE F&O stocks.")

if not API_KEY:
    st.error("⚠️ API key not found. Add GOOGLE_API_KEY in .env file.")
    st.stop()

# Sidebar
selected_stock = st.sidebar.selectbox("Select F&O Stock", sorted(fno_stocks))
st.sidebar.info("Showing latest headlines for selected stock.")

# Time period filters
import datetime as dt
periods = {
    "1 Week": dt.date.today() - dt.timedelta(days=7),
    "1 Month": dt.date.today() - dt.timedelta(days=30),
    "3 Months": dt.date.today() - dt.timedelta(days=90),
    "6 Months": dt.date.today() - dt.timedelta(days=180),
}
selected_period = st.sidebar.selectbox("Time Range", list(periods.keys()))
start_date = periods[selected_period]

# Google News API Endpoint
url = f"https://newsapi.org/v2/everything?q={selected_stock}%20NSE&from={start_date}&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)

if response.status_code != 200:
    st.error("Error fetching news. Check API key or quota.")
    st.stop()

data = response.json()
articles = data.get("articles", [])

if not articles:
    st.warning("No news found for this stock today.")
    st.stop()

# Display Articles
for article in articles:
    st.subheader(article["title"])
    st.write(article["description"])
    st.write(f"🕒 {article['publishedAt']}")
    st.markdown(f"[Read Full Article]({article['url']})")
    st.markdown("---")
