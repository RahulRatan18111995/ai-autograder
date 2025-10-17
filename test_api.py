import requests
import os
import json

url = "http://127.0.0.1:8000/generate"
payload = {
    "email":"you@example.com",
    "secret":"a4e748dae8dec14e8efc92a738c33ad0",
    "task":"todo list",
    "round":1,
    "nonce":"abc123",
    "brief":"Build a simple todo list app",
    "evaluation_url":"http://example.com/notify"
}
r = requests.post(url, json=payload, timeout=30)
print(r.status_code)
try:
    print(r.json())
except Exception:
    print(r.text)
