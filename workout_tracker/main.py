import os
import requests
from datetime import datetime

APP_ID = os.environ["app_id_nutritionix"]
API_ID = os.environ["api_id_nutritionix"]

WEIGHT_KG = 68
HEIGHT_CM = 180
AGE = 19

input1 = input("what is your query")
query = str(input1)

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_ID,
}
params = {
    "query": query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(end_point, json=params, headers=header)
result = response.json()
today = datetime.now()
time_now = today.strftime("%H:%M:%S")
date_now = today.strftime("%d/%m/%Y")

header2 = {
    "Authorization": "Basic Z2FsbG9wbWFuOnNjaW9qaWpkcHdkcGQ="
}

data1 = {"workout":
    {
        "date": f"{date_now}",
        "time": f"{time_now}",
        "exercise": f"{result["exercises"][0]["user_input"]}",
        "duration": f"{result["exercises"][0]["duration_min"]}",
        "calories": f"{result["exercises"][0]["nf_calories"]}",
    }
}

workout_endpoint = "https://api.sheety.co/648b83c87d44aebfbed181bec458061e/myWorkoutGoogleSheets/workouts"
response0 = requests.post(workout_endpoint, json=data1, headers=header2)
print(response0.text)
