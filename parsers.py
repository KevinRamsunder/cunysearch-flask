import re
from bs4 import BeautifulSoup

class ResultPageParser:

    def __init__(self, doc):
        self.parseCounter = 0
        self.headings = doc.find_all('div', {'id' : re.compile('^win0divGPSSR_CLSRSLT_WRK_GROUPBOX2')})
        self.classesPerHeading = doc.find_all('table', {'id' : re.compile('ACE_\$ICField104')})
        self.nbr = doc.find_all('a', {'id' : re.compile('^MTG_CLASS_NBR')})
        self.section = doc.find_all('a', {'id' : re.compile('^MTG_CLASSNAME')})
        self.status = doc.find_all('img', {'class' : re.compile('SSSIMAGECENTER')})
        self.room = doc.find_all('span', {'id' : re.compile('^MTG_ROOM')})
        self.time = doc.find_all('span', {'id' : re.compile('^MTG_DAYTIME')})
        self.instr = doc.find_all('span', {'id' : re.compile('^MTG_INSTR')})
        return

    def incrementCounter(self):
        self.parseCounter += 1
        return

    def headingSize(self):
        return len(self.headings)

    def getHeadings(self):
        return self.headings[self.parseCounter]

    def getClassesPerHeading(self):
        return self.classesPerHeading[self.parseCounter]

    def getNbr(self):
        return self.nbr[self.parseCounter]

    def getSection(self):
        return self.section[self.parseCounter]

    def getStatus(self):
        return self.status[self.parseCounter]

    def getRoom(self):
        return self.room[self.parseCounter]

    def getTime(self):
        return self.time[self.parseCounter]

    def getInstr(self):
        return self.instr[self.parseCounter]

class ClassHeadingParser:

    def __init__(self, title, quantity):
        self.title = title.text
        self.title = self.title[1:len(self.title)-1]
        self.quantity = len(quantity.find_all('div', {'id' : re.compile('^win0divMTG_CLASS_NBR')}))
        return

class ClassSectionParser:

    def __init__(self, nbr, section, status):
        self.nbr = nbr.text
        self.section = section.text.replace('\n', ' ')
        self.htmlKey = section['id']
        self.status = status['alt']
        return

class SingleSectionParser:

    def __init__(self, time, room, instr):
        self.rowCount = 1
        self.time = time.text
        self.room = room.text
        self.instr = instr.text
        return

class MultiSectionParser:

    def __init__(self, rowCount, time, room, instr):
        self.rowCount = rowCount
        tTime = time.html.replace('<br />', '\n')
        tRoom = room.html.replace('<br />', '\n')
        tInstr = instr.html.replace('<br />', '\n')
        self.timeArray = tTime.split('\n')
        self.roomArray = tRoom.split('\n')
        self.instrArray = tInstr.split('\n')
        return

class EnrollmentInfoParser:

    def __init__(self, htmlPage):
        soup = BeautifulSoup(htmlPage)
        cap = soup.find('span', {'id' : re.compile('SSR_CLS_DTL_WRK_ENRL_CAP')})
        tot = soup.find('span', {'id' : re.compile('SSR_CLS_DTL_WRK_ENRL_TOT')})
        avail = soup.find('span', {'id' : re.compile('SSR_CLS_DTL_WRK_AVAILABLE_SEATS')})
        self.classCapacity = int(cap.text)
        self.classTotal = int(tot.text)
        self.classAvailable = int(avail.text)
        return

