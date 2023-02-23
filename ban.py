import json, random, time, psutil, requests, os
import pyautogui as pg

antifloodCounter = 0
bannedBotsCouter = 0
cdn_files = []

with open("config/config.json") as config_file:
    config = json.load(config_file)

with open('lang/' + config['lang'] + '_lang.json') as lang_file:
    lang = json.load(lang_file)

with open(config['whitelist']) as whitelist_file:
    whitelist = [line.strip() for line in whitelist_file]


def getCDN():
    for i in range(len(config['cdn'])):
        url = config['cdn'][i]
        domain = url.split('/')[2]
        filename = f'{domain}_{time.localtime().tm_yday}.txt'
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
                cdn_files.append(filename)
        else:
            print(f'Error downloading {url}')

    if not cdn_files:
        print(lang['no_cdn'])


def banBots(line):
    global antifloodCounter, bannedBotsCouter
    if bannedBotsCouter <= config['manyBansBeforeWaiting']:
        if config['showDebugPrints']:
            print(lang['ban'] + line)

        antifloodCounter += 1
        bannedBotsCouter += 1

        for command in config['executeCommands']:
            pg.write(config['alphanumericCharacterToUse'] + command + line)
            pg.press(config['keyToPressAfterCommand'])

        if antifloodCounter == config['manyBansAntiflood']:
            if config['showDebugPrints']:
                print(lang['waiting_seconds'].format(config['secondsToWaitAfterXBansAntiflood']))
                
            time.sleep(config['secondsToWaitAfterXBansAntiflood'])

            if config['showDebugPrints']:
                print(lang['starting_again'])
                
            antifloodCounter = 0
    else:
        if config['showDebugPrints']:
            print(lang['waiting_seconds'].format(config['secondsToWaitAfterXBans']))

        time.sleep(config['secondsToWaitAfterXBans'])
        bannedBotsCouter = 0


def killProcess():
    for proc in psutil.process_iter():
        try:
            for process in config['processesToKill']:
                if proc.name() == process:
                    proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


time.sleep(config['delayBeforeStart'])
print(lang['starting'])

if config['active_scanning_cdn']:
    print(lang['scanning_cdn'])
    getCDN()

if config['typeScanning'] == 'Both':
    files_to_scan = config['files'] + cdn_files
elif config['typeScanning'] == 'OnlyLocal':
    files_to_scan = config['files']
elif config['typeScanning'] == 'OnlyCDN':
    files_to_scan = cdn_files
else:
    files_to_scan = []
    print(lang['no_files'])

for filename in files_to_scan:
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() in whitelist:
                continue
            else:
                banBots(line)

if config['youWantCloseAfterFinsihed']:
    killProcess()
