import time
from pybit.unified_trading import HTTP
from config import CURRENCY

bybit = HTTP(testnet=False)

def get_prices():
    message = "📈 *Текущая обстановка на рынке* \n" \
              "────────────────────\n"
    for currency in CURRENCY:
        try:
            response = bybit.get_tickers(category="linear", symbol=currency)
            price = float(response['result']['list'][0]['lastPrice'])
            display_name = currency.replace("USDT", "") if "USDT" in currency else currency
            message += f"  {display_name}: {price:.2f} USDT\n"
        except Exception as e:
            display_name = currency.replace("USDT", "") if "USDT" in currency else currency
            message += f"⚠️ {display_name}: Ошибка ({e})\n"
    message += "────────────────────\n"
    message += f"Обновлено: {time.strftime('%H:%M')}"
    return message