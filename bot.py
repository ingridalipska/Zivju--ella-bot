import os
import requests

TELEGRAM_TOKEN = "9271045647:AAG3PgiLCYJdFwGJ_0ZjvQvznmp85hPxTEQ"
CHAT_ID = "7443132080"

# Aptieku meklēšanas saites Möller's 250ml eļļai
URLS = {
    "Azeta": "https://www.azeta.lv/search?q=moller+zivju+ella+250ml",
    "Internetaptieka": "https://www.internetaptieka.lv/lv/search?q=moller+zivju+ella+250ml",
    "Moonmart": "https://moonmart.lv/search?q=moller+zivju+ella+250ml",
    "BENU": "https://www.benu.lv/meklesana?q=moller+zivju+ella+250ml",
    "Apotheka": "https://www.apotheka.lv/meklesana?q=moller+zivju+ella+250ml",
    "Mēness Aptieka": "https://www.menessaptieka.lv/meklesana?q=moller+zivju+ella+250ml"
}

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def check_prices():
    report = "🐟 *Möller's zivju eļļas (250 ml) cenas un saites:*\n\n"
    
    for name, link in URLS.items():
        report += f"🔹 *{name}*:\n🔗 [Skatīt piedāvājumus]({link})\n\n"
            
    send_telegram(report)

if __name__ == "__main__":
    check_prices()
