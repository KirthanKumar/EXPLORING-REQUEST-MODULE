import os
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

for file in os.listdir("htmls"):
    with open(f"htmls/{file}") as f:
        htmlContent = f.read()
        soup = BeautifulSoup(htmlContent, "html.parser")
        # print(soup)
        # print(soup.title)
        for link in soup.findAll("a"):
            print(link.get("href"))