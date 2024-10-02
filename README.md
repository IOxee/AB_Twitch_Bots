
    ░█████╗░██╗░░░██╗████████╗░█████╗░  ██████╗░░█████╗░███╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║
    ███████║██║░░░██║░░░██║░░░██║░░██║  ██████╦╝███████║██╔██╗██║
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══██╗██╔══██║██║╚████║ (by IOxee)
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██████╦╝██║░░██║██║░╚███║
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝

                    Moderation Tool for Twitch


The script is a moderation tool for Twitch that automates the process of detecting and blocking bots in a live chat. The program scans the chat log and compares the lines with a whitelist of allowed users. If a bot is detected, the program executes a series of commands in the chat to block it.

The program can also scan files hosted on a content delivery network (CDN) if this option is enabled in the settings. After blocking a certain number of bots, the program waits for some time before continuing to prevent antiflood.

It is important to note that the program hijacks the keyboard of the user who uses it while it is active. This means that the user will not be able to use the keyboard to perform other actions on his computer while the program is running.

The program configuration is read from a JSON file in the program's configuration directory. The configuration file includes options such as the whitelist of allowed users, the list of commands to block bots, the option to scan CDN files and other important parameters.

In short, the script is a moderation tool for Twitch that automates the process of blocking bots in live chat. It is important to note that the program hijacks the keyboard of the user who uses it while it is active. With the program, streamers can maintain a clean and safe chat for their Twitch community.

## Requirements
Python 3.8 or higher

Python Packages:
- pyautogui
- requests
- json
- random
- psutil
- time

## Execution
`pip install -r requirements.txt`

`python main.py`

## Configuration
The program configuration is read from a JSON file in the program's configuration directory. The configuration file includes options such as the whitelist of allowed users, the list of commands to block bots, the option to scan CDN files and other important parameters.

## Changelog - V(1.1.0)
- Added the option to set how many days from the date of extraction it takes for the bot to be considered malicious.
- Updated requirements.txt removed required versions.
- Added more moderator bots to the whitelist.