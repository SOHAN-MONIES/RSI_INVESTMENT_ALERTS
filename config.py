import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
INTERVAL = "1d"

RSI_LENGTH = 14

RSI_LEVEL = 30


WATCHLIST = [
    # Indices
    "^NSEI",
    "^NSEBANK",
    "^CNXIT",

    # Broad Market
    "NIFTYBEES.NS",
    "JUNIORBEES.NS",

    # Sector ETFs
    "BANKBEES.NS",
    "PSUBNKBEES.NS",
    "ITBEES.NS",
    "PHARMABEES.NS",
    "AUTOBEES.NS",
    "CONSUMBEES.NS",
    "INFRABEES.NS",

    # Precious Metals
    "GOLDBEES.NS",
    "SILVERBEES.NS",

    # International
    "MON100.NS",
    "MAFANG.NS"
]
