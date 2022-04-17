# importing required modules
import PyPDF2
import sys
import re


class pdfReader():
    def __init__(self, file_path:str):
        self.file_path=file_path
        self.classes=[]
        # creating a pdf file object
        pdfFileObj = open(self.file_path, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # creating a page object
        pageObj = pdfReader.getPage(0)
        self.text=pageObj.extractText()
        # closing the pdf file object
        pdfFileObj.close()
        print(self.get_classes(self.text))

    def get_classes(self, text:str):
        result=[]
        if "UNDERGRADUATE ACADEMIC RECORD" not in text:
             return 'no transcript file given'
        else:
            result.append(re.findall(r'[A-Z]{3} {8}[0-9]{3}',text))
            result.append(re.findall(r'[A-Z]{3} {7}[0-9]{3}[A-Z]',text))
            return result

def main(path:str):
    new_pdfreader=pdfReader(path)

if __name__=="__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print('no transcript file given')
