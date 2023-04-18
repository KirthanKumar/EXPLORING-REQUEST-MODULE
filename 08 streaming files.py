# when u are downloading some file, u will get to know how much is downloaded and how much is left to download.
import requests
from io import BytesIO
from tqdm import tqdm # used to show progress bar

url = "url_of_pycharm_file.dmg"
r = requests.get(url, stream=True)
totalExpectedBytes = int(r.headers['Content-Length'])
print(totalExpectedBytes)
bytesReceived = 0
progress_bar = tqdm(total=totalExpectedBytes, unit='iB', unit_scale=True)

with open('pycharm.dmg', 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        print(f"{bytesReceived} recieved out of total {totalExpectedBytes}")
        progress_bar.update(128)
        f.write(chunk)
        bytesReceived += 128
progress_bar.close()