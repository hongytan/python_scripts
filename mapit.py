# USAGE: python3 mapit.py address
# Lets you map an address from the command line
# This opens up google maps

import webbrowser, sys, pyperclip

if len(sys.argv) > 2:
    address = ' '.join(sys.argv[2:])
    webbrowser.open('https://google.com/maps/place/'+address)
    webbrowser.open('https://google.com/maps/place/'+address)
