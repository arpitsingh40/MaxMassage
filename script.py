import pyautogui
import time

# Author AREXX

number_of_messages = int(input('Enter number of messages: '))
message_content = input('Enter message content: ')

time.sleep(5)

for num in range(number_of_messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')

print('Script executed successfully')
