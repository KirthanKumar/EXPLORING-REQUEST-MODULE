import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.json())
# print(type(r.json())) # <class 'dict'>
# the above line is same as:
# https://httpbin.org/get?key1=value1&key2=value2


# this can also be done by using f-strings also:
key = "key1"
value = "value1"
r = requests.get(f"https://httpbin.org/get?{key}={value}")
print(r.json())