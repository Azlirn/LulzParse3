# !/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import time
import support


# TODO: Add flag to allow csv files to be processed
# TODO: Add options for other pasting sites like Ghostbin
# TODO: Check for duplicate records in database (old alerts)

# In the current configuration, this script should be able to process:
# 200,000 rps (records per second)

LulzParse = support.Lulz3Support()


def mainMenu():

    # clear screen on start
    os.system('cls' if os.name == 'nt' else 'clear')

    print '''
     _           _    ______                     _____
    | |         | |   | ___ \                   |____ |
    | |    _   _| |___| |_/ /_ _ _ __ ___  ___      / /
    | |   | | | | |_  /  __/ _` | '__/ __|/ _ \     \ |
    | |___| |_| | |/ /| | | (_| | |  \__ \  __/ .___/ /
    \_____/\__,_|_/___\_|  \__,_|_|  |___/\___| \____/

        '''
    print '\n[*] Thanks to leakedsource.com for providing an awesome list of domains to ignore.\n'

    menu = {'1': "Pastebin", '2': "Ghostbin", '3': "Text File", '4': "CSV File", '5': "Exit"}
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print entry, menu[entry]

        selection = raw_input("\n{*} Please Select: ")
        if selection == '1':
            pastebinMain()
        elif selection == '2':
            print "Option not available at this time, please try again later"
        elif selection == '3':
            print "Option not available at this time, please try again later"
        elif selection == '4':
            print "Option not available at this time, please try again later"
        elif selection == '5':
            break
        else:
            print "Unknown Option Selected!"
            reload(mainMenu())


def pastebinMain():
    print '[*] Enter the ID of the pastebin you would like to check...'
    print "{*} Example: For the link - http://pastebin.com/PRc9Zczf \"PRc9Zczf\" is your ID"
    pastebinID = raw_input('\n{*} ID: ')

    # run a check on the user input to make sure it is valid.
    url = 'https://pastebin.com/raw/%s' % pastebinID
    try:
        if LulzParse.urlChecker(url):
            print '\n[*] === ID is Valid === [*]'
        else:
            print "[!] %s did not return a good response... Try again..." % url
            time.sleep(1)
            reload(mainMenu())

        print "\n[*] Checking records to see if file containing your ID was previously processed..."

        if LulzParse.checkForDuplicateFiles(pastebinID):
            filePath = LulzParse.checkForDuplicateFiles(pastebinID)
            print '\n[!] It appears you may be trying to process a dump that has previously been parsed.'
            print '{*} A file was found here: %s' % filePath
            print '\n{*} Would you like to process this file anyway?'
            print '{*} WARNING: THIS MAY OVERWRITE ANY OLD DATA!\n'
            menu = {'Y :': "Continue", 'N :': "Don't Process", 'Q :': "Exit Program"}
            status = True
            while status is True:
                options = menu.keys()
                for entry in options:
                    print entry, menu[entry]
                selection = raw_input("\n{*} Please Select: ")
                if selection == 'Y':
                    status = False
                    try:
                        pasteFile = LulzParse.downloadPastebin(pastebinID, url)
                        LulzParse.rmDomain(pastebinID, pasteFile)
                    except Exception as e:
                        print '\n[!] ERROR: Exception occurred in LulzParse3.pastebinMain() while attempting to process a possible duplicate dump +++> %s' % e
                elif selection == 'N':
                    print '[*] Exiting Application'
                    time.sleep(2)
                    exit()
                elif selection == 'Q':
                    print '[*] Exiting Application'
                    time.sleep(2)
                    exit()
                else:
                    print "[!] Unknown Option Selected!"
                    time.sleep(2)
                    exit()
            else:
                exit()

        else:
            print '\n[*] Congratulations Paul! This dump appears to be new!'
            time.sleep(1)
            raw_input("\n[!] Press any key to start...\n")
            try:
                webcontent = LulzParse.downloadPastebin(pastebinID, url)
                LulzParse.rmDomain(pastebinID, webcontent)
            except Exception as e:
                print '\n[!] ERROR: Exception occurred in LulzParse3.pastebinMain() +++> %s' % e



    except Exception as e:
        print '\n[!] ERROR: Unhandled Exception occurred in LulzParse3.pastebinMain +++> %s' % e


if __name__ == '__main__':
    mainMenu()
