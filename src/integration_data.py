from requests import get
headers = {"accept" : "application/json"}

# months / weeks / days / minutes + 1,3,5,10,15,30,60,240..
url = "https://api.upbit.com/v1/candles/months?market=KRW-BTC&count=8"
response = get(url, headers=headers)

for result in eval(response.text):
    print(f"data : {result['candle_date_time_kst']}")
    print(f"open : {result['opening_price']}")
    print(f"high : {result['high_price']}")
    print(f"low : {result['low_price']}")
    print(f"close : {result['trade_price']}")
    print(f"volume : {result['candle_acc_trade_volume']}")
    print()