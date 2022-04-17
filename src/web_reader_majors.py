import requests
from bs4 import BeautifulSoup
import os

# import classentry
url = "https://ucdavis.pubs.curricunet.com/Catalog/degrees"
page = requests.get(url)
class_prereqs=[]
major_hrefs=[]
# find page content
soup = BeautifulSoup(page.content, "html.parser")
# get all major urls
block=soup.find_all("div", class_="page-content-section-wrapper")
links=block[0].find_all("a")

for link in links:
    href=link.get("data-urlalias")
    major_hrefs.append(str(href))

base_url = "https://ucdavis.pubs.curricunet.com/Catalog/"

for href in major_hrefs:
    class_names=[]
    if "graduate" not in href:
        major_url=base_url+str(href)
        print(major_url)
        major_page = requests.get(major_url)
        major_soup = BeautifulSoup(major_page.content, "html.parser")
        # find all specific class blocks
        class_entryinfos = major_soup.find_all("div", class_="row course-row-core block-entry course-entry pdf-flex-nowrap")
        # initializing class name list
        if len(class_entryinfos)>0:
            for classentryinfo in class_entryinfos:
                class_temp=classentryinfo.find("div", class_="col-xs-2 col-sm-2 col-md-2 three-column left-column text-left text-start")
                class_names.append(class_temp.text)
            class_data=open(os.path.dirname(__file__)+"/major_files/"+href+"_req.csv", 'w+')
            for class_name in class_names:
                class_data.write(class_name+"\n")
            class_data.close()
