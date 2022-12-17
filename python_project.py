import requests
import bs4
# ___Url for page website
url = 'https://btech.com/ar/laptop/laptops-1/huawei.html'
# ___use requests to fetch the url
page = requests.get(url)
# ___check the status
if (page.status_code ==200):
    # __save page and access to content
    srs = page.content
    # __use BeautifulSoup object to parse content
    soup = bs4.BeautifulSoup(srs, "html.parser")
    # __ general find the element containing
    all_details = soup.find_all("div", {"class": "plpContentWrapper"})
    for detail in all_details:
        lab_nam = detail.find("h2", {"class": "plpTitle"})
        lab_pric = detail.find("span", {'data-price-type': "finalPrice"})
        print(f"the name:{lab_nam.text}\n")
        print(f"the price:{lab_pric.text}")









