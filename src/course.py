#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

class Course:

    # Initializer
    # to create the object, use Course(courseId, sectionId, termId)
    def __init__(self, courseId, sectionId, termId):
        print("hi")
