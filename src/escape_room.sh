#!/bin/bash

if ! [[ -x "$(command -v pip3)" ]]
then
    echo 'pip3 is not installed, to install pip3, please go to https://pypi.org/project/pip/' >$2
    exit 1

fi
echo 'Now installing Escape Room..'
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
echo 'Everything has been installed.  Enjoy playing!'
python3 main.py
deactivate