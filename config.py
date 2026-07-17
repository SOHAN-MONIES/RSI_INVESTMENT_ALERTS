import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
INTERVAL = "1d"

RSI_LENGTH = 14

RSI_LEVEL = 30


WATCHLIST = [
    # =========================
    # INDIA
    # =========================
    "^NSEI",            # Nifty 50
    "^NSEBANK",         # Nifty Bank
    "^CNXIT",           # Nifty IT
    "^CNXAUTO",         # Nifty Auto
    "^CNXPHARMA",       # Nifty Pharma
    "^CNXPSUBANK",      # Nifty PSU Bank
    "^CNXINFRA",        # Nifty Infrastructure
    "^CNXCONSUMPTION",  # Nifty Consumption
    "^CNXMETAL",        # Nifty Metal
    "^CNXFMCG",         # Nifty FMCG
    "^CNXENERGY",       # Nifty Energy
    "^CNXREALTY",       # Nifty Realty
    "^CNXMEDIA",        # Nifty Media
    "^CNXFINSERVICE",   # Nifty Financial Services
    "^CNXMIDCAP",       # Nifty Midcap 100
    "^CNXSMLCAP",       # Nifty Smallcap 100

    # =========================
    # UNITED STATES
    # =========================
    "^GSPC",            # S&P 500
    "^NDX",             # Nasdaq-100
    "^DJI",             # Dow Jones
    "^RUT",             # Russell 2000
    "^VIX",             # Volatility Index
    "^SOX",             # Philadelphia Semiconductor Index

    # =========================
    # COMMODITIES
    # =========================
    "GC=F",             # Gold
    "SI=F",             # Silver
    "CL=F",             # WTI Crude Oil
    "NG=F",             # Natural Gas

    # =========================
    # CURRENCIES
    # =========================
    "DX-Y.NYB",         # US Dollar Index (DXY)
    "INR=X",            # USD/INR Exchange Rate

    # =========================
    # CRYPTO
    # =========================
    "BTC-USD",          # Bitcoin
    "ETH-USD",          # Ethereum
]
