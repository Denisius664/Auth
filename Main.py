import time
from pathlib import Path
from termcolor import colored
import All_logic
from selenium import webdriver
import pickle

print('''       
    [0;1;34;94m▄▄[0m                         [0;37m▄▄[0m       
   [0;34m████[0m                [0;37m██[0m      [0;37m█[0;1;30;90m█[0m       
   [0;34m████[0m    [0;37m██[0m    [0;37m██[0m  [0;37m███[0;1;30;90m████[0m   [0;1;30;90m██▄████▄[0m 
  [0;37m██[0m  [0;37m██[0m   [0;37m██[0m    [0;1;30;90m██[0m    [0;1;30;90m██[0m      [0;1;30;90m█[0;1;34;94m█▀[0m   [0;1;34;94m██[0m 
  [0;37m██████[0m   [0;1;30;90m██[0m    [0;1;30;90m██[0m    [0;1;30;90m█[0;1;34;94m█[0m      [0;1;34;94m██[0m    [0;1;34;94m██[0m 
 [0;1;30;90m▄██[0m  [0;1;30;90m██▄[0m  [0;1;30;90m██▄▄▄[0;1;34;94m███[0m    [0;1;34;94m██▄▄▄[0m   [0;1;34;94m█[0;34m█[0m    [0;34m██[0m 
 [0;1;30;90m▀▀[0m    [0;1;30;90m▀[0;1;34;94m▀[0m   [0;1;34;94m▀▀▀▀[0m [0;1;34;94m▀▀[0m     [0;34m▀▀▀▀[0m   [0;34m▀▀[0m    [0;34m▀▀[0m 
''')

cite = input(colored('Enter your site address>>: ', 'cyan'))
login = input(colored('Enter your login>>: ', 'cyan'))
password = input(colored('Enter your password>>: ', 'cyan'))
answer_sa = input(colored('Want to press extra button(default=n)>>: ', 'magenta'))
timeout_before = input('Timeout before(default=0)>>: ')
timeout_after = input('Timeout after(default=0)>>: ')
output = input(colored('Give name to out file(defaults=cookies)>>: ', 'magenta'))
if len(output) == 0:
    output = 'cookies'
if len(timeout_before) == 0:
    timeout_before = 0
else:
    timeout_before = int(timeout_before)
if len(timeout_after) == 0:
    timeout_after = 0
else:
    timeout_after = int(timeout_after)

driver = webdriver.Firefox()

try:
    # Get page
    driver.get(cite)
    time.sleep(timeout_before + 2)
except:
    print(colored('Invalid url ', 'red'))

if answer_sa == 'y' or answer_sa == 'yes':
    All_logic.special_action(driver, 1)

try:
    # Find input fields and login button
    fields = All_logic.find_fields(driver)
    print(colored('Login fields and button was found', 'blue'))
    # Login process
    All_logic.login(fields, login, password)
    time.sleep(timeout_after + 2)
    print(colored('The user was login', 'blue'))
except:
    print(colored('except when finding login, password fields and login button', 'red'))
    driver.close()
    exit()


# Write to file
cookies = driver.get_cookies()
driver.close()

path_cookies = Path('cookies')
path_cookies.mkdir(parents=True, exist_ok=True)
pickle.dump(cookies, open('cookies/' + output + '.pkl', 'wb'))
print(colored('The cookie was write to file ' + output + '.pkl', 'yellow'))
# Close driver
