#!/usr/bin/env python3

from icalendar import Calendar, Event
from course import Course
from section import Section
from room import Building
import datetime, re, breaks

calendarName = "test.ics"

def generateCal(courseList):
    cal = Calendar()
    cal.add('x-wr-calname', 'Class Schedule')
    cal.add('tzid', 'America/New_York')

    termId = courseList[0].termId
    regex = "^(\d{4})(\d{2})$"
    match = re.search(regex, termId)
    
    year = match.group(1)
    semester = match.group(2)

    if semester == "01":
        dates = breaks.spring
    elif semester == "08":
        dates = breaks.fall

    for course in courseList:
        for section in course.sectionList:
            for date in dates:
                e = Event()
                e.add('summary', course.courseId)

                startTime = datetime.datetime.combine(date[0], section.start)
                e.add('dtstart', startTime)

                endTime = datetime.datetime.combine(date[0], section.end)
                e.add('dtend', endTime)

                e.add('exdate', datetime.datetime.combine(datetime.date(2020,2,19), section.start))

                days = []
                for day in section.day:
                    days.append(day.value)

                e.add('rrule', {'freq': 'weekly',
                                'wkst': 'su',
                                'until': datetime.datetime.combine(date[1], section.start),
                                'byday': days})

                e.add('location', section.room.getAddress())

                des = section.room.building + " " + section.room.room
                des += "\nSection: " + course.sectionId
                des += "\n" + ("Lecture" if section.isLecture else "Discussion")
                e.add('description', des)

                cal.add_component(e)
    
    with open(calendarName, 'wb') as ics_file:
        ics_file.write(cal.to_ical())

def main():
    c = Course("CMSC132", "0101", "202001")
    generateCal([c])

if __name__ == "__main__":
    main()
