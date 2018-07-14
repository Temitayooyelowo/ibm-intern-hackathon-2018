import requests
from bs4 import BeautifulSoup

def scrape_prof_info (url, student_research_interest, hyper_link):
    print("In carleton .py scrape_prof_info")

    new_request = requests.get(url)
    temp_soup = BeautifulSoup(new_request.content, "html.parser")
    prof_details = temp_soup.find_all("article")
    prof_name = temp_soup.find("h1", {"class": "banner__heading"}).text

    for info in prof_details:
        try:
            prof_research_interest = info.find_all('p', {"class": ""})[0].text.lower()
            prof_image_info = info.find_all('img')[0]
            prof_image_alt = prof_image_info.get("alt")
            prof_image_src= prof_image_info.get("src")

            does_prof_have_interest = student_research_interest in prof_research_interest
            if(does_prof_have_interest):
                hyper_link.append({"name": prof_name, "image_alt": prof_image_alt, "image_src": prof_image_src, "web_page_url": url})
        except:
            pass


def scrape_all_prof (student_research_interest):
    hyper_link = []
    student_research_interest = student_research_interest.lower()
    print("In carleton .py scrape_all_prof")
    url = "https://carleton.ca/scs/our-people/school-of-computer-science-faculty/faculty/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    g_data = soup.find_all("a", {"class":"card__link"})

    for link in g_data:
        prof_page_href = link.get("href")
        scrape_prof_info(prof_page_href, student_research_interest, hyper_link)

    return hyper_link
    #print_professors(hyper_link)

def print_professors (hyper_link):
    # print hyper_link
    for item in hyper_link:
        print(item["name"])
        print(item["image_alt"])
        print(item["image_src"])
        print(item["web_page_url"])
        print('')

# scrape_all_prof('security')
# print_professors()
