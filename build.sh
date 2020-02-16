#!/usr/bin/env bash

pip3 install -r requirements.txt
pyinstaller src/main.py --noconfirm --onefile
