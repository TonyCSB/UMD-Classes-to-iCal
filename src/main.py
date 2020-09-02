#!/usr/bin/env python3
from get_input import getInput
from iCal import generateCal
from CAS import login
from scraper import scrape
from user import User
from getpass import getpass
import os, time, sys


def main():
    reply = input("Would you like to enter the course (M)anually or import from your schedule (A)utomatically? (M/A) ").lower().strip()

    if reply[0] == 'm':
        courseList = manual()
        print("Course input successfully, generating iCal file now...")
    elif reply[0] == 'a':
        courseList = automatic()
        if courseList is None:
            while input("Press <ENTER> to quit.") != "":
                return False
        print("Course scraped successfully, generating iCal file now...")
    else:
        i = 5
        while i >= 0:
            print("Invalid response, self detonation initiates in {0} seconds.".format(i), end="\r", flush=True)
            time.sleep(1)
            i -= 1

        print("\nBOOM!")
        return False

    calendar = generateCal(courseList)
    print("\niCal file generated, please import it into Calendar of your choice!")

    os.system("start " + calendar)

    while input("Press <ENTER> to quit.") != "":
        pass


def automatic(username=None, password=None, termid=None):
    if username is None or password is None:
        username = input("Please input your username: ").strip()
        password = getpass("Please input your password: ").strip()

    user = User(username, password)

    try:
        user = login(user, username, password)
    except ValueError as e:
        print(e)

    print("Login successfully.")
    if termid is None:
        termid = input("Please input the term id to be imported (eg. 202001): ")
    print("Scraping your schedule data...")

    data = scrape(user, termid)
    return data


def manual():
    return getInput()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        courseList = automatic(sys.argv[1], sys.argv[2], sys.argv[3])

        if courseList is not None:

            print("Course scraped successfully, generating iCal file now...")

            calendar = generateCal(courseList)
            print("\niCal file generated, please import it into Calendar of your choice!")

            os.system("start " + calendar)

            while input("Press <ENTER> to quit.") != "":
                pass
    elif len(sys.argv) == 1:
        main()
    else:
        print("Incorrect amount of argument given")
