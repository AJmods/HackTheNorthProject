import requests

URL = 'http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p={PartnerID}&t.k={Key}&action=employers&q=pharmaceuticals&userip={IP_address}&useragent=Mozilla/%2F4.0'

headers = {'user-agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=headers)

print(response)