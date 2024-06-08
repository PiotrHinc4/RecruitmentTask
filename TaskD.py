import requests

petId = 100000

url = f'https://petstore.swagger.io/v2/pet/{petId}'

response = requests.delete(url)

if response.status_code == 200:
    print("The server response:", response.status_code)
else:
    print(f"Something is wrong. Code status: {response.status_code}")
