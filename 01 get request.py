# https://requests.readthedocs.io/en/latest/
import requests

r = requests.get("https://google.com")
# print(r.text)  # the source code of above mentioned url is fetched. If in any case internet is down, the data can be stored in this way.
with open("index.html", "w") as f:
    f.write(r.text)