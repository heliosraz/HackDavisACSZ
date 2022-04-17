import sys
import classObjects
import student
import readpdf

class Student(self):
    classes
    def __init__(transcript_path:str):
        new_pdfreader=readpdf(transcript_path)
        classes=new_pdfreader.get_classes()
        for indclass in classes:
            subject, class_number=indclass.split(' ')
