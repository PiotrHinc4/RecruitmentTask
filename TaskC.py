import requests

petId = 100000
pet_status="sold"
pet_data = {
    "id": petId,
    "status": pet_status
}

url = f'https://petstore.swagger.io/v2/pet'

response = requests.put(url, json=pet_data)

if response.status_code == 200:
    print("The server response:", response.status_code)
else:
    print(f"Something is wrong. Code status: {response.status_code}")
