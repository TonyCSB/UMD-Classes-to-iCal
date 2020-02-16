#!/usr/bin/env bash

pip3 install pyinstaller
pyinstaller src/main.py --noconfirm --onefile
