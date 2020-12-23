'''
Create a program which automates open and locate a street address on the web browser

This is what your program does:

Gets a street address from the command line arguments or clipboard
Opens the web browser to the Google Maps page for the address
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Read the clipboard contents.
Call the webbrowser.open() function to open the web browser.

'''

# needed modules:
import webbrowser, sys, pyperclip

# Step 1: figure out the URL
# the street input is either the command input or the clipboard content
# proper url: https://www.google.com/maps/place/your_address_string


# Step 2: handle address input
if len(sys.argv) > 1:
    # TODO: Get the address from command line
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # TODO: get the address from clipboard
    address = pyperclip.paste()  # access and paste the content of the clipboard
    print(address)

# run and show the address on Google map
webbrowser.open('https://www.google.com/maps/place/' + address)

