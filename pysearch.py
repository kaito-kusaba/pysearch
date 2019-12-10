from googlesearch import search
import webbrowser
import os
from halo import Halo
from termcolor import colored, cprint
import requests

clear = lambda: os.system('cls')
connection = 'None'
spinner1 = Halo(text='Checking connection: ', text_color='cyan', spinner='dots' , placement='right')
def logo():
    print(colored('''
=============================================
                                      _
                                     | |
  _ __  _   _ ___  ___  __ _ _ __ ___| |__
 | '_ \| | | / __|/ _ \/ _` | '__/ __| '_ \\
 | |_) | |_| \__ \  __/ (_| | | | (__| | | |
 | .__/ \__, |___/\___|\__,_|_|  \___|_| |_|
 | |     __/ |
 |_|    |___/

=============================================
''', 'yellow', attrs=['bold']))

clear()
while True:
    while connection != 'success':
        logo()
        spinner1.start()
        try:
            requests.get('https://google.com')
            spinner1.stop()
            print(colored('Checking connection: ', 'cyan', attrs=['bold']) + colored('Success!', 'green', attrs=['bold']))
            connection = 'success'
            input('Push enter to continue...')
            clear()
        except:
            spinner1.stop()
            print(colored('Checking connection: ', 'cyan', attrs=['bold']) + colored('Failed!', 'red', attrs=['bold']))
            connection = 'failed'
            input('Push enter to retry...')
            clear()
    break


logo()
rNumber = 0
results = []
query = input('Search: ')
# language = input('Language (en, jp, etc.): ')
number = input('Amount of results: ')

while True:
    try:
        number = int(number)
        print(f"\n{colored('=============================================', 'yellow', attrs=['bold'])}\n")
        break
    except:
        print('Please enter a integer!\n')
        number = input('Amount of results: ')

for r in search(query, tld='com', lang='en', num=number, start=0, stop=number, pause=2.0):
    rNumber += 1
    results.append(r)
    print(f"\n{colored(rNumber, 'red', attrs=['bold'])}. {colored(r, 'cyan', attrs=['bold'])}")

option = 'y'
while True:
    if option == 'y':
        choice = input('\nChoose link: ')
        while True:
            try:
                choice = int(choice)
                if choice <= rNumber and choice > 0:
                    url = results[choice - 1]
                    webbrowser.open(url, new=0, autoraise=True)
                    option = input('Continue (y/n): ')
                    break
                else:
                    print('\nPlease choose one of the links available!')
                    break
            except:
                print('\nPlease enter a integer!')
                break
    elif option == 'n':
        break
    else:
        print('\nPlease choose valid a option!')
        option = input('Continue (y/n): ')
os.system('del .google-cookie')
clear()
