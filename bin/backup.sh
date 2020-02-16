#!/bin/bash
git pull origin master

git add -A
git commit -m "Update $(date "+%Y.%m.%d-%H:%M:%S")"
git push origin master

echo -e "\ngit push complete\n"
