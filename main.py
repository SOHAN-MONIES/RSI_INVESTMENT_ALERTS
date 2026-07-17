import json
import os
from datetime import datetime

import requests
import yfinance as yf

from config import *

STATE_FILE = "state.json"


def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": msg,
        },
        timeout=10,
    )


def calculate_rsi(close, period=14):
    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


# ----------------------------
# Load previous alert state
# ----------------------------
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
else:
    state = {}

# ----------------------------
# Report Header
# ----------------------------
today = datetime.now().strftime("%d %b %Y")

summary = f"""📊 Market Daily Report
📅 {today}

"""

for ticker, name in WATCHLIST.items():

    try:

        if INTERVAL == "15m":
            period = "60d"
        elif INTERVAL == "1h":
            period = "730d"
        else:
            period = "1y"

        df = yf.download(
            ticker,
            period=period,
            interval=INTERVAL,
            auto_adjust=True,
            progress=False,
            multi_level_index=False,
        )

        if df.empty:
            print(f"{name}: No data")
            continue

        close = df["Close"].squeeze()

        if len(close) < RSI_LENGTH + 2:
            print(f"{name}: Not enough data")
            continue

        rsi = calculate_rsi(close, RSI_LENGTH)

        prev = float(rsi.iloc[-2])
        curr = float(rsi.iloc[-1])
        price = float(close.iloc[-1])

        # ----------------------------
        # Status
        # ----------------------------
        if curr <= 30:
            emoji = "🔴"
            status = "BUY"
        elif curr <= 40:
            emoji = "🟡"
            status = "WATCH"
        elif curr >= 70:
            emoji = "🟣"
            status = "SELL?"
        else:
            emoji = "🟢"
            status = "NORMAL"

        summary += (
            f"{emoji} {name}\n"
            f"   💰 {price:.2f} | RSI {curr:.2f} | {status}\n\n"
        )

        # ----------------------------
        # Buy Alert
        # ----------------------------
        crossed = prev > RSI_LEVEL and curr <= RSI_LEVEL

        already = state.get(ticker, False)

        if crossed and not already:

            message = f"""🚨 BUY ALERT

📈 Asset : {name}

💰 Price : {price:.2f}

📊 RSI({RSI_LENGTH}) : {curr:.2f}

📉 Previous RSI : {prev:.2f}

🟢 Potential buying opportunity.
"""

            send(message)

            state[ticker] = True

            print(f"✅ ALERT SENT -> {name}")

        elif curr > RSI_LEVEL:
            state[ticker] = False

        print(f"{name:<25} Price={price:.2f} RSI={curr:.2f}")

    except Exception as e:
        print(f"{name}: {e}")

# ----------------------------
# Send Daily Report
# ----------------------------
send(summary)

# ----------------------------
# Save Alert State
# ----------------------------
with open(STATE_FILE, "w") as f:
    json.dump(state, f, indent=4)
