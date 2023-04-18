import requests
r = requests.post('https://httpbin.org/post?a=b', data={'kirthan': 'value'}) # https://httpbin.org is a tool/site to test requests.
print(r.text)