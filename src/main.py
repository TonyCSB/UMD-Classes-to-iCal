#!/usr/bin/env python3
from get_input import getInput
from course import Course
from iCal import generateCal
from CAS import login
from scraper import scrape
from user import User
import os, time

def main():
    reply = input("Would you like to enter the course (M)anually or import from your schedule (A)utomatically? (M/A) ").lower().strip()

    if reply[0] == 'm':
        cal = manual()
    elif reply[0] == 'a':
        cal = automatic()
    else:
        i = 5
        while i >= 0:
            print("Invalid response, self detonation initiates in {0} seconds.".format(i), end="\r", flush=True)
            time.sleep(1)
            i -= 1

        print("\nBOOM!")
        return False

    os.system("start " + cal)

    while input("Press <ENTER> to quit.") != "":
        pass

def automatic():
    username = input("Please input your username: ").strip()
    password = input("Please input your password: ").strip()
    user = User(username, password)

    try:
        user = login(user, username, password)
    except ValueError as e:
        print(e)
    
    print("Login successfully.")
    termid = input("Please input the term id to be imported (eg. 202001): ")
    print("Scraping your schedule data...")

    print("Project under development...")
    data = scrape(user, termid)
    return ""

def manual():
    courseList = getInput()
    print("\n\nCourse input successfully, generating iCal file now...")
    calendar = generateCal(courseList)
    print("\niCal file generated, please import it into Calendar of your choice!")

    return calendar

if __name__ == "__main__":
    main()
