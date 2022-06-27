import json
from time import sleep
import requests

import waifusgonewild
import thick_hentai
import ecchi

input("Press Enter to start>>")
url = "https://www.reddit.com/r/hentai.json"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
data = requests.get(url, headers=headers).json()
def getData():
    for ch in data["data"]["children"]:
        pic_url = ch["data"].get("url_overridden_by_dest")
        if pic_url:
            file_name = pic_url.split("/")[-1]
            if not "." in file_name:
                continue
            with open(r"files/" + file_name, "wb") as f_out:
                print("Downloading {}".format(pic_url))
                c = requests.get(pic_url, headers=headers).content
                f_out.write(c)
while True:
    getData()
    waifusgonewild.getData()
    thick_hentai.getData()
    ecchi.getData()
    print("waiting 4 hours for next download...")
    sleep(14400)