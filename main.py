import os, time, json
from sys import stdout

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

with open("config/config.json") as config_file:
    config = json.load(config_file)

with open('lang/' + config['lang'] + '_lang.json') as lang_file:
    lang = json.load(lang_file)

banner = """

░█████╗░██╗░░░██╗████████╗░█████╗░  ██████╗░░█████╗░███╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║
███████║██║░░░██║░░░██║░░░██║░░██║  ██████╦╝███████║██╔██╗██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══██╗██╔══██║██║╚████║ (by IOxee)
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██████╦╝██║░░██║██║░╚███║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝

                Moderation Tool for Twitch
"""


def show_menu():
    purple()
    print(banner)
    white()
    for option in lang['menu_messages']:
        print(option['numberation'] + ". " + option['option'])
        time.sleep(0.1)

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        choice = input(lang['menu_select'])

        if choice == "1":
            print(lang['extracting_bots'])
            os.system('python extract.py')

            time.sleep(3)
            print(lang['bots_extracted'].format(sum(1 for line in open("content/output_file"))))

            proceed = input(lang['do_you_wish_to_continue'])
            if proceed == "Y" or proceed == "y":
                print(lang['start_with_bans'])
                os.system('python ban.py')
            else:
                print(lang['exiting'])
                time.sleep(2)

        elif choice == "2":
            print(lang['extracting_bots'])
            os.system('python extract.py')

            time.sleep(3)
            print(lang['bots_extracted'].format(sum(1 for line in open("content/output_file"))))

            time.sleep(2)
            print(lang['exiting'])

            time.sleep(2)
        elif choice == "3":
            print(lang['start_with_bans'])
            os.system('python ban.py')

            time.sleep(2)
            print(lang['exiting'])
        elif choice == "4":
            print(lang['program_exiting'])
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(lang['invalid_input'])
    except KeyboardInterrupt:
        print(lang['program_exiting'])
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
