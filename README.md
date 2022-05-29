# UMD Classes to iCal

This program reads in courses that the user inputs (course and section number) per semester and outputs them into a standardized iCal format that can be imported into popular calendar applications including Google Calendar.

## PROJECT IS NO LONGER BEING MAINTAINED

This project is no longer being maintained. All functions are provided as is, please proceed with your own discretion. You are more than welcomed to fork this project and continue further development.

## Features:

* Course data can be imported through your login info directly NOW
* All courses can be added and imported into other programs at once.
* Lecture and discussion sections are listed separately.
* Each class event includes a location (building name, room number, and full address) that is viewable within the user's calendar application.
* Breaks are taken into account. Classes are not listed if they would occur over a break. Break data is taken directly from the UMD website.

To generate an iCal file, the program will prompt the user for a course to enter. If only a course number is entered, it will prompt the user for the section number. Courses can also be entered with a section number. Once all courses have been entered, just press Enter to generate the file.

The program outputs a file `course_schedule.ics` which can then be imported into any calendar program that supports importing from iCal files.

## Input Format

### Automatic Scraper (with support for cli input)

~~Try `src/main.py <username> <password> <termid>` for commandline argument input~~

See [Usage](##Usage)

### Term ID
In the form of `YYYYMM`, such as `202001`.
- 01 for Spring
- 05 for Summer
- 08 for Fall
- 12 for Winter

### Course ID
Must contains the four letter department code and three digit course code. (Optional: Include the section id at the end) For example: `CMSC132`, `CMSC 132`, `CMSC132-0101`, `CMSC132 0101`.

### Section ID
Must be in the format of four code. Such as `0101`.

## Usage
```[Bash]
usage: src/main.py [-h] [-a | -m] [-u USERNAME] [-p PASSWORD] [-t TERMID]

optional arguments:
  -h, --help            show this help message and exit
  -a, --automatic       Run the calendar generator in automatic mode
  -m, --manual          Run the calendar generator in manual mode
  -u USERNAME, --username USERNAME
                        UMD directory id for auto scraping
  -p PASSWORD, --password PASSWORD
                        Password for your directory id
  -t TERMID, --termID TERMID
                        Term ID to be scraped
```

## Disclaimer

The password is not stored in plain text, and is used to authenticate with UMD CAS only. It is not backed up to any third-party server or storage.

Any information generated through this program is saved locally only.
