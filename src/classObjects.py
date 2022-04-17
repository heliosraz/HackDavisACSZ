#Class Class

from typing import List
class Class:

#string: str
#int: int
#float: float

    # type hinting: variableName: type
    def __init__(self, subject: str, code: str, name:str, numbUnits: int, preReqs: str) -> None:
        self.subject = subject
        self.code= code
        self.name=name
        self.numbUnits = numbUnits
        self.preReqs = preReqs

    @staticmethod
    def createClass(name: str, numbUnits: int, preReqs: List["Class"]) -> "Class":
        ...
    '''
    # puts prereqs in order by name, and then from largest number to smallest number
    @staticmethod
    def reqOrder(preReqs: List["Class"]) -> List["Class"]:
        # puts prereqs in order by name
        preReqs

        # puts prereqs
    '''

    def printClassName(self) -> None:
        print(f"{self.subject+sefl.code}\n{self.numbUnits}\n")
        for x in self.preReqs:
            className = self.preReqs[x].name
            print(className)

            #organize by number
