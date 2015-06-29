from parsers import ResultPageParser, ClassHeadingParser, ClassSectionParser, SingleSectionParser, MultiSectionParser, EnrollmentInfoParser
from containers import ClassHeading

class ClassStructure:

    def __init__(self):
        self.classHeadings = []
        return

    def createSectionHeader(self, chp):
        self.classHeadings.append(chp)
        return

    def addClassToHeader(self, position, section):
        self.classHeadings[position].addClassToHeading(section)

    def getSectionHeaderCount(self):
        return len(self.classHeadings)

    def getClassHeader(self, index):
        return self.classHeadings[index]

    def getClassSection(self, index1, index2):
        return self.classHeadings[index1].classes[index2]