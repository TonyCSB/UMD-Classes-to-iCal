#!/usr/bin/env python3

from icalendar import Calendar, Event
from course import Course
from section import Section
from room import Building
import datetime, re

def generateCal(courseList):
    cal = Calendar()
    cal.add('x-wr-calname', 'Class Schedule')
    cal.add('tzid', 'America/New_York')

    for course in courseList:
        for section in course.sectionList:
            e = Event()
            e.add('summary', course.courseId)

            startTime = datetime.datetime.combine(datetime.date(2020, 2, 16), section.start)
            e.add('dtstart', startTime)

            endTime = datetime.datetime.combine(datetime.date(2020,2,16), section.end)
            e.add('dtend', endTime)

            # TODO: [exdate] for breaks
            # TODO: finish repeat rules

            days = []
            for day in section.day:
                days.append(day.value)

            e.add('rrule', {'freq': 'weekly',
                            'wkst': 'su',
                            'until': datetime.datetime(2020,5,20,0,0,0),
                            'byday': days})

            e.add('location', section.room.getAddress())

            des = section.room.building + " " + section.room.room
            des += "\nSection: " + course.sectionId
            des += "\n" + ("Lecture" if section.isLecture else "Discussion")
            e['description'] = des

            cal.add_component(e)
    
    with open('test.ics', 'wb') as ics_file:
        ics_file.write(cal.to_ical())

def main():
    c = Course("CMSC132", "0101", "202001")
    generateCal([c])

if __name__ == "__main__":
    main()
