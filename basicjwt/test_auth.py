import requests

url = "http://localhost:5000/auth"

payload = ({'username':'user1', 'password':'abcxyz'})
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

r = requests.post(url, headers=headers, data=payload)
response = r.json()

print(response)