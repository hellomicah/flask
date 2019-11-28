import requests, json

url = "http://localhost:5000/auth"

payload = '{"username":"user1", "password":"abcxyz"}'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=payload)

print(response)