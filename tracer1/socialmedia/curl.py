import urllib3, json, requests


# http = urllib3.PoolManager()
# api_url = "http://127.0.0.1:8000/users/"
# r = http.request('GET', api_url)
# r_data = json.loads(r.data)
# print r_data

r1 = requests.post('http://127.0.0.1:8000/users/post/', data='Saurabh Sathe')
print r1.text

