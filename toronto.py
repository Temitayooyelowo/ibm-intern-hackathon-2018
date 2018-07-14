import requests
import time
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def scrape_prof_info (url, prof_name, student_research_interest, hyper_link):
    print "In toronto.py scrape_prof_info"
    time.sleep(2)

    new_request = requests.get(url, headers=headers)
    temp_soup = BeautifulSoup(new_request.content, "html.parser")
    prof_image_info = temp_soup.find("img")
    # prof_research_interest = temp_soup.find_all("p", {"class": ""})[3].text.lower()

    prof_image_alt = prof_image_info.get("alt")
    prof_image_src= prof_image_info.get("src")

    print prof_image_alt
    print prof_image_src

    # print prof_research_interest
    print ''

def scrape_all_prof (student_research_interest):
    hyper_link = []
    student_research_interest = student_research_interest.lower()
    print "In toronto.py scrape_all_prof"
    url = "https://www.ece.utoronto.ca/faculty/directory/"

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    g_data = soup.find_all("div", {"class":"threecol"})

    for prof in g_data:
        for item in prof.find_all("li", {"class": ""}):
            my_item = item.find("a")

            prof_page_href = my_item.get("href")
            prof_name = my_item.text
            print prof_page_href
            print prof_name
            print ''

            time.sleep(1)
            scrape_prof_info(prof_page_href, prof_name, student_research_interest, hyper_link)

scrape_all_prof("")
