#!/usr/bin/env python3
from icalendar import Calendar, Event
from course import Course
from section import Section, Day
from room import Building
from breaks import breaks, fall, spring
import datetime, re

calendarName = "course_schedule.ics"

def generateCal(courseList):
    cal = Calendar()
    cal.add('x-wr-calname', 'Class Schedule')
    cal.add('tzid', 'America/New_York')

    termId = courseList[0].termId
    regex = r"^(\d{4})(\d{2})$"
    match = re.search(regex, termId)
    
    year = match.group(1)
    semester = match.group(2)

    if semester == "01":
        year = int(year) - 1
        breaks(year)
        dates = spring
    elif semester == "08":
        breaks(int(year))
        dates = fall

    for course in courseList:
        if not course.online:
            for section in course.sectionList:
                for date in dates:
                    e = Event()
                    e.add('summary', course.courseId)

                    firstDay = date[0]
                    matched = False
                    while not matched:
                        for d in section.day:
                            if firstDay.weekday() == d.value[0]:
                                matched = True
                                break
                        if not matched:
                            firstDay += datetime.timedelta(days = 1)

                    startTime = datetime.datetime.combine(firstDay, section.start)
                    e.add('dtstart', startTime)

                    endTime = datetime.datetime.combine(firstDay, section.end)
                    e.add('dtend', endTime)

                    days = []
                    for day in section.day:
                        days.append(day.value[1])

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

    return calendarName

def main():
    c = Course("CMSC132", "0101", "202001")
    generateCal([c])

if __name__ == "__main__":
    main()
