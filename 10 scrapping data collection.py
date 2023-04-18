import requests

# Data collection
links = ["https://www.codewithharry.com/blog", "https://www.codewithharry.com/videos", "https://www.codewithharry.com/contact"]

for link in links:
    r = requests.get(link)
    with open(f"htmls/{link.split('/')[-1]}.html", "w") as f:
        f.write(r.text)