# MaxMassage
Best SMS bombing script for all Social Media  and Massaging Platform


## Prerequisites

In order to run the python script, your system must have the following programs/packages installed.
* Python 3.8: Download it from https://www.python.org/downloads
* Pyautogui: Run in command prompt pip install pyautogui or pip3 install pyautogui





# Automate Messages Python Script

This is a simple script that sends multiple messages using python script. This is used for educational purposes only. Please don't ruin anyone's phone by sending multiple messages.

## Demo
* Video clip on youtube of the script execution. 


## Approach
* First need to clone this respiratory.
* Open Any massaging platform.
* Run python script script.py using py script.py in the terminal.
* The script will ask you to enter the number of messages and message content in the terminal, after entered both information successfully you keep the cursor in the message bar in the Massaging application to whom you want to send the message.
* The script will sleep for 5 seconds and then begin to send messages continuously until and unless messages not send all.

Note: Please use just use for fun not to ruin anyone's phone.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Code
```
import pyautogui
import time

number_of_messages = int(input('Enter number of messages: '))
message_content = input('Enter message content: ')

time.sleep(5)

for num in range(number_of_messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')

print('Script executed successfully')
```

## Windows:

* git clone MaxMassage
* cd MaxMassage 
* python3 script.py
* Enter number of messages: 1000
* Enter message content: Hiiii
* Press Enter


## Linux:

* git clone MaxMassage
* cd MaxMassage 
* python3 script.py
* Enter number of messages: 1000
* Enter message content: Hiiii
* Press Enter

## Termux:

* pkg update
* pkg install python3 python3-pip git -y
* git clone MaxMassage
* cd MaxMassage 
* python3 script.py
* Enter number of messages: 1000
* Enter message content: Hiiii
* Press Enter

## MacBook

* git clone MaxMassage
* cd MaxMassage 
* python3 script.py
* Enter number of messages: 1000
* Enter message content: Hiiii
* Press Enter
