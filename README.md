# JHacks 2020
## UMD Classes to iCal

This program reads in courses that the user inputs (course and section number) per semester and outputs them into a standardized iCal format that can be imported into popular calendar applications including Google Calendar.

Features:

* All courses can be added and imported into other programs at once.
* Lecture and discussion sections are listed separately.
* Each class event includes a location (building name, room number, and full address) that is viewable within the user's calendar application.
* Breaks are taken into account. Classes are not listed if they would occur over a break. Break data is taken directly from the UMD website.

To generate an iCal file, the program will prompt the user for a course to enter. If only a course number is entered, it will prompt the user for the section number. Courses can also be entered with a section number. Once all courses have been entered, just press Enter to generate the file.

The program outputs a file `course_schedule.ics` which can then be imported into any calendar program that supports importing from iCal files.

### How to Install
1. Download the file as a zip file and extract the file.
2. Open `cmd` and `cd <current directory>`.
3. `pip3 install -r requirements.txt`
4. `pyinstaller src/main.py --noconfirm --onefile`
5. The executable file `main.exe` will be located at `dist` folder.
