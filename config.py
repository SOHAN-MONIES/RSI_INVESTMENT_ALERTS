import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
INTERVAL = "1d"

RSI_LENGTH = 14

RSI_LEVEL = 30


WATCHLIST = {
    # INDIA
    "^NSEI": "Nifty 50",
    "^NSEBANK": "Bank Nifty",
    "^CNXIT": "Nifty IT",
    "^CNXAUTO": "Nifty Auto",
    "^CNXPHARMA": "Nifty Pharma",
    "^CNXPSUBANK": "Nifty PSU Bank",
    "^CNXINFRA": "Nifty Infrastructure",
    "^CNXMETAL": "Nifty Metal",
    "^CNXFMCG": "Nifty FMCG",
    "^CNXENERGY": "Nifty Energy",
    "^CNXREALTY": "Nifty Realty",
    "^CNXMEDIA": "Nifty Media",
    "JUNIORBEES.NS": "Nifty Next 50",
    "MIDCAPETF.NS": "Midcap ETF",

    # UNITED STATES
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq-100",
    "^DJI": "Dow Jones",
    "^RUT": "Russell 2000",
    "^VIX": "VIX",
    "^SOX": "Semiconductor Index",

    # COMMODITIES
    "GC=F": "Gold",
    "SI=F": "Silver",
    "CL=F": "Crude Oil",
    "NG=F": "Natural Gas",

    # CURRENCIES
    "DX-Y.NYB": "US Dollar Index",
    "INR=X": "USD/INR",

    # CRYPTO
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
}
