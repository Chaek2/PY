import requests

res = requests.post("http://127.0.0.1:3000/api/main/0?title=Test")
print(res.json()) 