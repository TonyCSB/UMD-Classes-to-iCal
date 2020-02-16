#!/usr/bin/env python3
from get_input import getInput
from course import Course
from iCal import generateCal

def main():
    courseList = getInput()
    print("Course input successfully, generating iCal file now...")
    generateCal(courseList)
    print("iCal file generated, please import it into Calendar of your choice!")

if __name__ == "__main__":
    main()