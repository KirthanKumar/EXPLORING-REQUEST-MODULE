import requests

http_proxy = "http://iproyal227480:K2qcexTX@geo.iproyal.com:12321"
https_proxy = "http://iproyal227480:K2qcexTX@geo.iproyal.com:12321"
# ftp_proxy = "http://10.10.1.10:3128"

proxies = {
    "http": http_proxy,
    "https": https_proxy
    # "ftp": ftp_proxy
}

r = requests.get("http://httpbin.org/get", proxies=proxies)
print(r.text)