import requests
import gspread
import datetime as dt
import os
from dotenv import load_dotenv,dotenv_values
load_dotenv()
exercise_input=input("tell me which exercise you did :")
parameters={
    "query":exercise_input
}
header={
    "x-app-id":os.getenv("X-APP-ID"),
    "x-app-key":os.getenv("X-APP-key")
}


response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=parameters,headers=header)
# print(response.status_code)
# print(response.text)
data=response.json()
#print(data)

today=dt.date.today()
# print(today)

gs=gspread.service_account(filename="mr_bathri.json")
cs=gs.open("Copy_of_My_Workouts").sheet1
time_duration=dt.datetime.now().strftime("%X")

cs.append_row([str(today),str(time_duration),str(data["exercises"][0]["name"]),str(data["exercises"][0]["duration_min"]),str(data["exercises"][0]["nf_calories"])])


