import requests
import json
category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': ''})

response = json.loads(response.text)
print(response[0]["quote"])
