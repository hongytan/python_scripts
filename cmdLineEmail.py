# python3 
# USAGE: python3 cmdLineEmail.py <email> <message>
# Use the command line to send a <message> to <email>
# NOTE: Currently the 'Subject' section is left blank.
# NOTE: Account is deleted. Program doesn't work with current account.

from selenium import webdriver
import sys

email = sys.argv[1]
message = ' '.join(sys.argv[2:])

# Connect to chrome and open a browser
PATH = 'C:\\Users\\hongt\\Downloads\\chromedriver.exe'
browser = webdriver.Chrome(PATH)

# Go to this link
browser.get("https://www.gmail.com")

# Get the username input element
username = browser.find_element_by_name('identifier')

# Put in username
username.send_keys('bobbybob147258369@gmail.com')

# Click "Next" button
browser.find_elements_by_tag_name('button')[-1].click()

# Wait for password page to load
browser.implicitly_wait(4)

# Put in password
browser.find_element_by_name("password").send_keys('Abc123qwe')

# Click "next button"
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

#
#
# Logged in!
# Now we need to send an email to <email> with <message>

# Click on Compose - to write email
browser.find_element_by_class_name('T-I-KE').click()

# Wait for New Message to load
browser.implicitly_wait(4)

# Put <email> in 'To'
browser.find_element_by_tag_name('textarea').send_keys(email)

# Put <message> in message box
browser.find_element_by_class_name('LW-avf').send_keys(message)

# Send the email
browser.find_element_by_class_name('dC').click()
