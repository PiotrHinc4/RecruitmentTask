import requests

url = f'https://petstore.swagger.io/v2/pet'

data = {
    "id": 100000,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Piotr",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

response = requests.post(url, json=data)


if response.status_code == 200:
    print("The animal has been added!")
    print("The server response:", response.status_code)
else:
    print(f"The animal hasn't been added. Code status: {response.status_code}")
