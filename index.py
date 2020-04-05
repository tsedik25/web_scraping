import requests
from bs4 import BeautifulSoup

def get_html_text(url):
    response = requests.get(url)
    response_page = response.text
    response_status = response.status_code

    if response_status == 200:
        return response_page
    elif response_status == 403:
        raise Exception("try after some minutes again")
    else:
        raise Exception("oops something went wrong")


response_page = get_html_text("https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht")

response_page_soup = BeautifulSoup(response_page, "html.parser")

container = response_page_soup.find("table", {"class":"chart full-width"})
trs = container.find("tbody").findAll("tr")

try:
    f = open("movies.csv", "w")
    f.write("name, image \n")

    for tr in trs:
        title = tr.find("td", {"class": "titleColumn"}).a.text
        image = tr.find("td", {"class": "posterColumn"}).a.img['src']
        writethis = f"{title}, {image} \n"
        f.write(title + ",\"" + image + "\"\n")
except Exception as e:
    print(e)
else:
    f.close()

