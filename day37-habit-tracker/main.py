import requests
import datetime

USERNAME = "danwil05"
TOKEN = "ajdoadoijawiod208dau"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph01",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.date(2024, 1, 29)
pixel_endp = "https://pixe.la/v1/users/danwil05/graphs/graph01"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9",
}
response = requests.post(url=pixel_endp, json=pixel_config, headers=headers)
print(response.text)
