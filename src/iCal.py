#!/usr/bin/env python3

from icalendar import Calendar, Event
from course import Course
from section import Section
from room import Building
import datetime

def generateCal(courseList):
    cal = Calendar()
    cal.add('x-wr-calname', 'Class Schedule')
    cal.add('tzid', 'America/New_York')

    for course in courseList:
        for section in course.sectionList:
            e = Event()
            e['summary']  = course.courseId
            # TODO: finish date and time processing
            e['dtstart'] = "20200216T" + section.start.strftime("%H%M%S")
            e['dtend'] = "20200216T" + section.end.strftime("%H%M%S")
            # TODO: deal with the extra backslash and finish repeat rules
            e['rrule'] = "FREQ=WEEKLY;WKST=SU;UNTIL=20200513T035959Z;BYDAY=MO,WE"
            e['location'] = section.room.getAddress()
            e['description'] = section.room.building + " " + section.room.room
            cal.add_component(e)
    
    with open('test.ics', 'wb') as ics_file:
        ics_file.write(cal.to_ical())

    # Read in the file
    with open('test.ics', 'r') as file :
        filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('\;', ';')

    # Write the file out again
    with open('test.ics', 'w') as file:
        file.write(filedata)

def main():
    c = Course("CMSC132", "0101", "202001")
    generateCal([c])

if __name__ == "__main__":
    main()
