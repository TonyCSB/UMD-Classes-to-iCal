import re
from course import Course

def main():
    createCourse(input("Enter a course: "))

def createCourse(courseInput):
    regex = '^([a-zA-Z]{4})\W*(\d{3}[a-zA-Z]?)\W*(\d{4})?$'
    match = re.search(regex, courseInput)
    courseId = match.group(1) + match.group(2)
    section = ""
    if match.group(3) is None:
        section = input("Enter the section number: ")
    else:
        section = match.group(3)
    course = Course(courseId, section, 202001)
    print(course)
    return course

main()