import requests
# from PIL import Image
from io import BytesIO
# can download even mp3 by this

url = "url_of_pycharm_file.dmg"
r = requests.get(url)
fp = open("pycharm.dmg", "wb")
fp.write(r.content)
fp.close()

# make a file downloader gui using tkinter, add to resume
# IPRoyal can be used to proxy in freelancing. Use code as: CODE30 to get 30% discount.