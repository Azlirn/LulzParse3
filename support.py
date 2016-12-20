import LulzParse3
import time
import re
import os
import urllib2


class Lulz3Support:
    def __init__(self):

        self.today = time.strftime("%Y-%b-%d")
        self.year = time.strftime("%Y")
        self.month = time.strftime("%B")

        # Variables used throughout the script
        self.regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                                 "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                                 "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

        self.govDomains = ['.gov', '.edu', '.us', 'k12', '.edu', 'police.', 'fire.', 'nsn.', 'pd.', 'hs.', 'cs.',
                           'housing.', 'ha.', 'town', 'cityof']

        self.emailDomains = ['@hotmail.com', '@yahoo.com', '@gmail.com', '@aol.com', '@hotmail.fr', '@live.com',
                             '@yahoo.fr', '@yahoo.com.tw', '@hotmail.co.uk', '@ymail.com', '@msn.com',
                             '@breakthru.com', '@rediffmail.com', '@live.fr', '@yahoo.co.in', '@yahoo.co.uk',
                             '@yahoo.co.br', '@hotmail.es', '@hotmail.it', '@libero.it', '@web.de', '@yahoo.in',
                             '@outlook.com', '@yahoo.es', '@rocketmail.com', '@comcast.net', '@bol.com.br',
                             '@gmx.de', '@yahoo.com.mx', '@yahoo.it', '@mail.com', '@live.co.uk', '@live.com.mx',
                             '@hotmail.de', '@yahoo.co.id', '@yahoo.ca', '@yahoo.de', '@scbglobal.net', '@orange.fr',
                             '@live.it', '@ig.com.br', '@googlemail.com', '@aim.com', '@yahoo.com.ar', '@abv.bg',
                             '@att.net', '@alice.it', '@yahoo.com.hk', '@yahoo.com.au', '@hotmail.com.br',
                             '@verizon.net', '@live.ca', '@hotmail.com.ar', '@excite.com', '@laposte.net',
                             '@btinternet.com', '@virgilio.it', '@wanadoo.fr', '@bellsouth.net', '@email.com',
                             '@icloud.com', '@yahoo.com.cn', '@facebook.com', '@cox.net', '@windowslive.com',
                             '@tiscali.it', '@live.nl', '@free.fr', '@freenet.de', '@seznam.cz', '@gmx.net', '@o2.pl',
                             '@earthlink.net', '@t-online.de', '@yahoo.com.vn', '@latinmail.com', '@live.com.ar',
                             '@hotmail.ca', '@live.com.au', '@yahoo.co.jp', '@me.com', '@yahoo.gr', '@gmx.at',
                             '@yahoo.com.sg', '@live.cl', '@netscape.net', '@juno.com', '@freemail.hu', '@gmx.xom',
                             '@charter.net', '@live.de', '@uol.com.br', '@ovi.com', '@live.com.pt', '@viola.fr',
                             '@bigpond.com', '@sapo.pt', '@yahoo.com.ph', '@terra.com.br', '@inbox.lv', '@mail.ru',
                             '@yandex.ru', '@myspace', '@126.com', '@163.com', '@qq.com', '@roadrunner.com']

    # def rmDomain(self, webContent, ID):
    #     start_time = time.time()
    #     hitcounter = 0
    #     pcounter = 0
    #
    #     try:
    #         with open(newfile, 'w') as nFile:
    #             try:
    #                 for line in webContent:
    #                     pcounter = pcounter + 1
    #                     lowerLine = line.lower()
    #                     if not any(domain in lowerLine for domain in self.emailDomains):
    #                         nFile.write(line)
    #                         hitcounter = hitcounter + 1
    #                 print '\r[*] {%s} lines read...' % (pcounter),
    #                 nFile.close()
    #
    #             except Exception as e:
    #                 print '[!] Error Occurred: %s' % e
    #                 #
    #                 # Uncomment the below if you would like the script to restart to 'main' if it encounters an error
    #                 #
    #
    #                 # print '[*] Restarting script...'
    #                 # time.sleep(5)
    #                 # reload(main())
    #
    #     except Exception as e:
    #         print "[!] Error reading paste content: %s" % e
    #         time.sleep(3)
    #         reload(LulzParse3.main())
    #
    #     ctime = time.time() - start_time
    #
    #     print '\n[*] %s was saved' % newfile
    #     print '[*] There are %s lines in your saved file.' % hitcounter
    #     print '[*] You processed %s total lines.\n' % pcounter
    #
    #     print "[*] === Completed in %s seconds === [*]" % ctime
    #
    #     print "\n[!] === Checking Possible SLTT Matches ===\n"
    #     time.sleep(2)
    #     self.chkRemaining(newfile)

    # def file_to_str(self, file):
    #     """Returns the contents of filename as a string."""
    #     with open(file) as f:
    #         return f.read().lower()  # Case is lowered to prevent regex mismatches.

    # def get_emails(self, s):
    #     """Returns an iterator of matched emails found in string s."""
    #     # Removing lines that start with '//' because the regular expression
    #     # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    #     return (email[0] for email in re.findall(self.regex, s) if
    #             not email[0].startswith('//') or email[0].startswith('\''))

    # def chkRemaining(self, newfile):
    #     start_time = time.time()
    #     hitcounter = 0
    #
    #     possibleMatches = open('PossibleMatches_' + newfile, 'a')
    #
    #     try:
    #         with open(newfile, 'r') as chkFile:
    #             for line in chkFile:
    #                 for email in self.get_emails(line):
    #                     if any(item in email for item in self.govDomains):
    #                         hitcounter = hitcounter + 1
    #                         possibleMatches.write(line)
    #
    #     except Exception as e:
    #         print "[!] Error Processing File: %s" % e
    #         time.sleep(5)
    #         reload(LulzParse3.main())
    #
    #     ctime = time.time() - start_time
    #
    #     print '\n[*] I identified %s potential SLTT records in your saved file.' % hitcounter
    #
    #     if hitcounter >= 1:
    #         print "[*] This dump should be processed."
    #         print "[**] Possible matches stored to your working directory"
    #     else:
    #         print "Ignore this shit..."
    #
    #     print "\n[*] === Completed check in %s seconds === [*]" % ctime
    #     time.sleep(2)
    #     exit()

    # A method that downloads a pastebin post, provided a unique pastebin ID. The pastebin post is saved to the
    # 'data/pastebin/year/month/today' directory.
    # The use of this method implies that the Pastebin URL has already been verified as existing.
    def downloadPastebin(self, pasteID, url):
        path = 'data/pastebin/%s/%s/%s/%s' % (self.year, self.month, self.today, pasteID)

        # Create a folder in the data/pastebin/year/month/today/pasteID directory to store the downloaded paste.
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            print '\n[!] ERROR: Exception occurred in LulzParse.downloadPastebin() while attempting to create a new directory +++> %s' % e

        # Call a method to check for duplicate pastebin dumps. If an old dump is found, exit the program.
        print '{*} Downloading a copy of the original paste to \"data/pastebin/%s/%s/%s/%s\" for historical purposes...' % (
            self.year, self.month, self.today, pasteID)
        pasteFile = "%s/ORIGINAL_%s.txt" % (path, pasteID)

        response = urllib2.urlopen(url)
        webContent = response.read()
        file = open(pasteFile, 'w')
        file.write(webContent)
        file.close()

        # Return the content of the paste in the webContent variable. This eliminates the need to open the pastebin file
        # in the future, allowing it to be processed from memory. Adding this should increase the speed of pastebin
        # processing.
        return webContent

    # This method checks the pastebin directory for IDs that match the user input and returns True if one is a filename
    # containing the ID is found. This is used to check for duplicate pastebin dumps that have already been processed.
    def checkForDuplicateFiles(self, ID):
        path = "data/"
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if ID in file:
                        files.append(file)
                        filePath = str(os.path.abspath(file))
                        return filePath
        except Exception as e:
            print '\n[!] ERROR: Exception occurred in LulzParse.checkForDuplicateFiles() while attempting to check for duplicate dump files +++> %s' % e

    # A method to take the a provided URL and determine if the code is "good" or "bad" based on the returned HTTP response
    def urlChecker(self, url):
        try:
            connection = urllib2.urlopen(url)
            connectionCode = connection.getcode()
            connection.close()
        except urllib2.HTTPError, e:
            connectionCode = e.getcode()

        if connectionCode == 200:
            return True
        else:
            print "[!] %s did not return a good response... Try again..." % url
            print "{!} URL returned status code: %s" % connectionCode
            time.sleep(3)
            reload(LulzParse3.main())
        return connectionCode
