import requests
from bs4 import BeautifulSoup
import re
# import classentry
url = "https://ucdavis.pubs.curricunet.com/Catalog/degrees"
page = requests.get(url)
class_names=[]
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
    if "graduate" not in href:
        major_url=base_url+str(href)
        print(major_url)
        major_page = requests.get(major_url)
        major_soup = BeautifulSoup(major_page.content, "html.parser")
        # find all specific class blocks
        class_entryinfos = major_soup.find_all("div", class_="container-fluid course-summary-wrapper")
        class_prereqinfos=major_soup.find_all("div", class_="col-xs-12 col-sm-12 col-md-12 text-left full-width-column")
        # initializing class name list
        for classentryinfo in class_entryinfos:
            class_temp=classentryinfo.find("div", class_="col-xs-10 col-sm-10 col-md-10 text-left left-column")
            class_names.append(class_temp.text)
        for prereqentry in class_prereqinfos:
            prereqentry=str(prereqentry.find_all('span')[2]).replace('<span>','').replace('</span>','')
            print(prereqentry)
            temp_pr=""
            for prereq in prereqentry.split(';'):
                prereqs=re.findall(r'[A-Z]{3} [0-9]{3}',prereq)+re.findall(r'[A-Z]{3} [0-9]{3}[A-Z]',prereq)
                print(prereqs)
                if len(prereqs)>1:
                    prereqs='/'.join(prereqs)
                temp_pr=temp_pr+(str(prereqs).replace('[','').replace(']','')).replace('\'','').replace('\'','')+','
            temp_pr.replace(temp_pr[-1],'')
            class_prereqs.append(temp_pr)

            temp_pr=''
        class_data=open('class_name_data.csv', 'w')
        for index in range(len(class_names)):
            class_data.write(",".join([class_names[index],class_prereqs[index]])+"\n")
        class_data.close()
