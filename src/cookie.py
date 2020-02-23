#!/usr/bin/env python3
import pickle, requests

# This module is intend to save and load cookie after login

def saveCookie(session:requests.session):
    with open('.cookie', 'wb') as f:
        pickle.dump(session.cookies, f)

def loadCookie(session:requests.session):
    with open('.cookie', 'rb') as f:
        session.cookies.update(pickle.load(f))