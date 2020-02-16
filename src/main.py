#!/usr/bin/env python3
from get_input import getInput
from course import Course
from iCal import generateCal
import os

def main():
    courseList = getInput()
    print("\n\nCourse input successfully, generating iCal file now...")
    calendar = generateCal(courseList)
    print("\niCal file generated, please import it into Calendar of your choice!")

    input("Press <ENTER> to quit.")

if __name__ == "__main__":
    main()