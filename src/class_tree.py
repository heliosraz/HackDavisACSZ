import classObjects

classes=[]
class Class_Tree():
    def __init__(self):
        self.populate_classes()

    def populate_classes(self):
        class_data=open('class_name_data.csv', 'r')
        for line in class_data:
            name, prereq=line.split(',',1)
            code, temp=line.split('—')
            subject, number=code.split(' ')
            att_list=temp.split(' ')
            course_name=att_list[0]
            units=att_list[-2].replace(['(',')'],'')
            status=att_list[-1]
            new_class=classObjects.Class(subject, number, course_name, units, prereq)
            classes.append(new_class)
        print(classes)
        class_data.close()

if __name__=="__main__":
    new_tree=Class_Tree()
