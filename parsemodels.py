import re
from bs4 import BeautifulSoup
from containers import ClassHeading, SingleRowSection, MultiRowSection, EnrollmentInfo, RowValidator
from parsers import ResultPageParser, ClassHeadingParser, ClassSectionParser, SingleSectionParser, MultiSectionParser, EnrollmentInfoParser
from structure import ClassStructure

class EnrollmentParser:

    def __init__(self, html):
        parser = EnrollmentInfoParser(html)
        self.enrollment = EnrollmentInfo(parser)
        return

    def getDictionary(self):
        array = []
        dictionary = {}
        dictionary['classcapacity'] = self.enrollment.classCapacity
        dictionary['enrollmenttotal'] = self.enrollment.enrollmentTotal
        dictionary['availableseats'] = self.enrollment.availableSeats
        array.append(dictionary)
        return array

class Parser:

    def __init__(self, html):
        str = html
        doc = BeautifulSoup(str)

        rpp = ResultPageParser(doc)
        self.classStructure = ClassStructure()

        for i in range(0, rpp.headingSize(), 1):
            heading = self.getHeadingInfo(rpp, i)
            self.classStructure.createSectionHeader(heading)
            self.addClassesPerHeading(rpp, i)

        return

    def getParserNoRow(self, parser):
        return SingleSectionParser(parser.getTime(), parser.getRoom(), parser.getInstr())

    def getParser(self, row, parser):
        return MultiSectionParser(row.rows, parser.getTime(), parser.getRoom(), parser.getInstr())

    def getSection(self, ov, inv):
        if hasattr(inv, 'timeArray'):
            return MultiRowSection(ov, inv)
        else:
            return SingleRowSection(ov, inv)

    def getHeadingInfo(self, parser, i):
        return ClassHeading(ClassHeadingParser(parser.headings[i], parser.classesPerHeading[i]))

    def getValidator(self, parser):
        return RowValidator(parser.getTime())

    def getOverhead(self, parser):
        return ClassSectionParser(parser.getNbr(), parser.getSection(), parser.getStatus())

    def addClassesPerHeading(self, parser, headingNumber):
        size = int(self.classStructure.getClassHeader(headingNumber).quantity)

        for i in range(0, size, 1):
            validator = self.getValidator(parser)
            classSection = self.getClassSection(validator, parser)
            self.classStructure.addClassToHeader(headingNumber, classSection)
            parser.incrementCounter()

        return

    def getClassSection(self, rows, pars):
        overhead = self.getOverhead(pars)

        if rows.rows == 1:
            handler = self.getParserNoRow(pars)
            return self.getSection(overhead, handler)
        else:
            handler = self.getParser(rows, pars)
            return self.getSection(overhead, handler)

        return

    def printClassStructure(self):
        for i in range(0, len(self.classStructure.classHeadings), 1):
            print (self.classStructure.getClassHeader(i).title).encode('utf-8')

            for j in range(0, int(self.classStructure.getClassHeader(i).quantity), 1):
                section = self.classStructure.getClassSection(i, j)
                print section.nbr, section.time, section.room, section.instr, section.status

            print

        return

    def getDictionary(self):
        array = []

        for i in range(0, len(self.classStructure.classHeadings), 1):
            name = self.classStructure.getClassHeader(i).title
            title = name[name.find('-')+2:]
            title = re.sub('\s+', ' ', title)
            subtitle = name[:name.find('-')-1]

            for j in range(0, int(self.classStructure.getClassHeader(i).quantity), 1):
                dictionary = {}
                section = self.classStructure.getClassSection(i, j)
                dictionary['title'] = title
                dictionary['subtitle'] = subtitle
                dictionary['nbr'] = section.nbr
                dictionary['time'] = section.time
                dictionary['room'] = section.room
                dictionary['instr'] = section.instr
                dictionary['status'] = section.status
                dictionary['htmlKey'] = section.htmlKey
                dictionary['section'] = section.section
                array.append(dictionary)

        return array

