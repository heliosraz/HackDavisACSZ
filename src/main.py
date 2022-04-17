import classObjects

classes=[]
def populate_classes():
    class_data=open('class_name_data.csv', 'r')
    for line in class_data:
        code, temp=str.split('-', line)
        subject, number=str.split(' ', code)
        course_name, units, status=temp.split('(',')')
        new_class=classObject(subject, number, name, units)
        classes.append()
    print(classes)

def main():
    populate_classes()


if __name__=="__main__":
    main()
