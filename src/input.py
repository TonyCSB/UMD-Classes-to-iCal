import re
from course import Course

def main():
    termId = input("Enter the term ID: ")
    courseInput = input("Enter a course: ")
    while courseInput != "":
        createCourse(courseInput, termId)
        courseInput = input("Enter a course: ")

def createCourse(courseInput, termId):
    regex = r'^([a-zA-Z]{4})\W*(\d{3}[a-zA-Z]?)\W*(\d{4})?$'
    match = re.search(regex, courseInput)
    courseId = match.group(1) + match.group(2)
    section = ""
    if match.group(3) is None:
        section = input("Enter the section number: ")
    else:
        section = match.group(3)
    course = Course(courseId, section, termId)
    print(course)
    return course

if __name__ == "__main__":
    main()
