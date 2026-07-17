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
    "^NSEBANK",         # Bank Nifty
    "^CNXIT",           # Nifty IT
    "^CNXAUTO",         # Nifty Auto
    "^CNXPHARMA",       # Nifty Pharma
    "^CNXPSUBANK",      # Nifty PSU Bank
    "^CNXMETAL",        # Nifty Metal
    "^CNXINFRA",        # Nifty Infrastructure
    "^CNXREALTY",       # Nifty Realty

    # =========================
    # UNITED STATES
    # =========================
    "^GSPC",            # S&P 500
    "^NDX",             # Nasdaq-100
    "^DJI",             # Dow Jones
    "^RUT",             # Russell 2000
    "^VIX",             # Volatility Index

    # =========================
    # COMMODITIES
    # =========================
    "GC=F",             # Gold
    "SI=F",             # Silver
    "CL=F",             # Crude Oil

    # =========================
    # CURRENCY
    # =========================
    "DX-Y.NYB",         # US Dollar Index (DXY)

    # =========================
    # CRYPTO
    # =========================
    "BTC-USD",          # Bitcoin
    "ETH-USD",          # Ethereum
]
