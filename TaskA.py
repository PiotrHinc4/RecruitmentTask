import requests
import json

url = "https://petstore.swagger.io/#/pet/addPet"

data = {
    "pets": [
        {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
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
        },
        {
            "id": 100001,
            "category": {
                "id": 10001,
                "name": "Feather"
            },
            "name": "parot",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 10001,
                    "name": "Feather"
                }
            ],
            "status": "available"
        },
    ]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("The animal has been added!")
    print("The server response:", response.json())
else:
    print(f"The animal hasn't been added. Code status: {response.status_code}")
    print("The server response:", response.text)