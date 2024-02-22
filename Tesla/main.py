STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
import smtplib
# api_key="WNDHWJJD3ZAHL506"
# parameters={
#     "function":"TIME_SERIES_DAILY",
#     "symbol":"IBM",
#     "appid":api_key
# }
# response=requests.get(url="https://www.alphavantage.co/query",params=parameters)

response=requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=WNDHWJJD3ZAHL506")
# print(response.status_code)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
print(data)
yesterday_data=[value for (key,value) in data.items()]
yesterday=yesterday_data[0]["4. close"]
before_yesterday=yesterday_data[1]["4. close"]
diff=abs(float(yesterday)-float(before_yesterday))
print(diff)
percentage=((diff)/(float(yesterday)/2))*100
# print(type(percentage))
print(f"{round(percentage,1)}%")


if percentage>1:
    # print("Get News")
    news=requests.get(url=f" https://newsapi.org/v2/everything?qInTitle={COMPANY_NAME}&apiKey=f1febfd78353421e98169be146911aa2")
    # print(news.status_code)
    news.raise_for_status()
    news_data=news.json()["articles"]
    three_articles=news_data[:3]
    # print(three_articles)
    # print(news_data)

    my_mail="20d3725bathrinath@gmail.com"
    password="kzkjwppvxdmsyysh"
    tesla_news=[f"headlines:{article['title']} \n\n Brief:{article['description']}" for article in three_articles] 

    with smtplib.SMTP("smtp.gmail.com") as trade_news:
        trade_news.starttls()
        trade_news.login(user=my_mail,password=password)
        trade_news.sendmail(from_addr=my_mail,to_addrs="bitbatbathri0608@gmail.com",msg=f"Subject:Trading News!!! \n\n\n {tesla_news}")



     


