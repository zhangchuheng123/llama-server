import requests
import pdb

with open('full_message.txt', 'r') as f:
   full_message = f.read()

with open('short_message.txt', 'r') as f:
   short_message = f.read()

api_key = "EMPTY"
headers = {"Content-Type": "application/json", "api-key": api_key}
data = {"messages": [{"role": "user", "content": short_message}], "max_seq_len": 5000, "temperature": 0.7, "top_p": 0.9}

pdb.set_trace()
port = 5331
url = 'http://localhost:{port}/api/completion'.format(port=port)
res = requests.post(url, json=data, headers=headers, timeout=30)
resp_json = res.json()
response = resp_json["choices"][0]["message"]["content"]
print(response)
