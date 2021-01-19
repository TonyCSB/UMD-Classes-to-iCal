#!/usr/bin/env python3
from get_input import getInput
from iCal import generateCal
from CAS import login
from scraper import scrape
from user import User
from getpass import getpass
import os, time, sys, argparse

parser = argparse.ArgumentParser()


def main():
    addArgument()
    args = parser.parse_args()
    # automatic=False, manual=False, password=None, termID=None, username=None

    if not args.automatic and not args.manual:
        reply = input("Would you like to enter the course (M)anually or import from your schedule (A)utomatically? (M/A) ").lower().strip()
        if reply[0] == 'm':
            args.manual = True
        elif reply[0] == 'a':
            args.automatic = True
        else:
            i = 5
            while i >= 0:
                print("Invalid response, self detonation initiates in {0} seconds.".format(i), end="\r", flush=True)
                time.sleep(1)
                i -= 1

            print("\nBOOM!")
            return False

    if args.manual:
        courseList = manual()
        print("Course input successfully, generating iCal file now...")
    elif args.automatic:
        courseList = automatic(args.username, args.password, str(args.termID))
        if courseList is None:
            while input("Press <ENTER> to quit.") != "":
                return False
        print("Course scraped successfully, generating iCal file now...")

    calendar = generateCal(courseList)
    print("\niCal file generated, please import it into Calendar of your choice!")

    os.system("start " + calendar)

    while input("Press <ENTER> to quit.") != "":
        pass


def automatic(username=None, password=None, termid=None):
    if username is None:
        username = input("Please input your username: ").strip()
    if password is None:
        password = getpass("Please input your password: ").strip()

    user = User(username, password)

    try:
        user = login(user, username, password)
    except ValueError as e:
        print(e)
        exit(1)

    print("Login successfully.")
    if termid is None:
        termid = input("Please input the term id to be imported (eg. 202001): ")
    print("Scraping your schedule data...")

    data = scrape(user, termid)
    return data


def manual():
    return getInput()


def addArgument():
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-a", "--automatic", action='store_true', help="Run the calendar generator in automatic mode")
    mode.add_argument("-m", "--manual", action='store_true', help="Run the calendar generator in manual mode")
    parser.add_argument("-u", "--username", type=str, help="UMD directory id for auto scraping")
    parser.add_argument("-p", "--password", type=str, help="Password for your directory id")
    parser.add_argument("-t", "--termID", type=int, help="Term ID to be scraped")


if __name__ == "__main__":
    main()
