import requests
from bs4 import BeautifulSoup
# import classentry

class_names=[]
class_prereqs=[]


class CourseWebReader:
    def __init__(self, url: str):
        self.url = url
        self.page = requests.get(URL)
        # find page content
        soup = BeautifulSoup(self.page.content, "html.parser")
        # find all specific class blocks
        self.class_entryinfos = soup.find_all("div", class_="container-fluid course-summary-wrapper")
        # initializing class name list
        self.class_names=[]
        get_classnames()

# getting class name data
    def get_classnames():
        for classentryinfo in self.class_entryinfos:
            class_temp=classentryinfo.find("div", class_="col-xs-10 col-sm-10 col-md-10 text-left left-column")
            class_names.append(class_temp.text)







# for classentryinfo in classentryinfos:
#
#     print(classentryinfo, end="\n"*2)
