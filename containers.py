import re
from bs4 import BeautifulSoup
from parsers import ResultPageParser, ClassHeadingParser, ClassSectionParser, SingleSectionParser, MultiSectionParser, EnrollmentInfoParser

class ClassHeading:

    def __init__(self, chp):
        self.title = chp.title
        self.quantity = chp.quantity
        self.classes = []
        return

    def addClassToHeading(self, section):
        self.classes.append(section)
        return

class SingleRowSection:

    def __init__(self, overhead, handler):
        self.htmlKey = overhead.htmlKey
        self.nbr = overhead.nbr
        self.section = overhead.section
        self.status = overhead.status
        self.enrollmentInfo = None

        self.time = handler.time
        self.room = handler.room
        self.instr = handler.instr
        return

    def attachEnrollmentInfo(e):
        self.enrollmentInfo = e
        return

class MultiRowSection:

    def __init__(self, overhead, handler):
        self.htmlKey = overhead.htmlKey
        self.nbr = overhead.nbr
        self.section = overhead.section
        self.status = overhead.status
        self.enrollmentInfo = None

        self.time = handler.timeArray
        self.room = handler.roomArray
        self.instr = handler.instrArray
        return

class EnrollmentInfo:

    def __init__(self, enrollmentInfo):
        self.classCapacity = enrollmentInfo.classCapacity
        self.enrollmentTotal = enrollmentInfo.classTotal
        self.availableSeats = enrollmentInfo.classAvailable
        return

class RowValidator:

    def __init__(self, time):
        self.rows = self.getRows(time, '<')
        return

    def getRows(self, element, char):
        rows = 1
        
        for c in element:
            if c == char:
                rows += 1

        return rows