import urllib
import urllib2
import re
createfile = open('targets.txt', 'w').close()
print 'Crawler Bot by 3XPL0173R~X3D\nfacebook.com/wax.vampire'
print 'Howdy Bradah?Good to see ya!'
print 'I can be your exploit crawler :D feed me something I ask'
suffix = raw_input('What suffix to search after urls?(ex. /user/ or /admin/login.php)\n')
texts = raw_input('Any custom texts to look for?(ex. Welcome to drupal or Enter username and password)\nTo skip this, type N\n')
ipstart = raw_input('Enter the IP start range(ex. 127.0.0.1):\n')
ipend = raw_input('Enter the final IP range(ex. 127.0.0.255):\n')
last = 'NULL'
last2 = 'NULL'
if '.' in ipstart:
    last = ipstart.split('.', 3)
if '.' in ipend:
    last2 = ipend.split('.', 3)
lastip = str(last2[0]) + '.' + str(last2[1]) + '.' + str(last2[2]) + '.' + str(last2[3])
i = 0
while True:
    add = int(last[3])+i
    workingip = str(last[0]) + '.' + str(last[1]) + '.' + str(last[2]) + '.' + str(add)
    print 'Thanks for the commands, I am on ma work!'
    print 'Currently checking on IP:', workingip
    reverse_lookup = 'NULL'
    try:
        reverse_lookup = urllib.urlopen('http://api.hackertarget.com/reverseiplookup/?q=' + workingip).read()
        if 'error check your search parameter' in reverse_lookup:
            print 'Your given domain seems incorrect!Please double check or reverse lookup is'
            print 'UNAVAILABLE for your domain!'
            input('Skipping ...')
            continue
        elif 'No records' in reverse_lookup:
            print 'Records seem to be'
            print 'UNAVAILABLE for your domain!'
            input('Skipping ...')
            continue
        elif '502 Bad' in reverse_lookup:
            print 'HackerTarget Server Down!'
            print 'Try later!'
            input('Press enter to exit ...')
            exit(0)
    except IOError:
        print 'Internet error or Reverse lookup server down!Try again!'
    cache = re.findall('[\w.]+', reverse_lookup)
    loop = 0
    while loop < len(cache):
        print 'checking on,', cache[loop] + suffix
        temp = cache[loop] + suffix
        if 'http://' not in temp:
            temp = 'http://' + temp
        try:
            resp = urllib2.urlopen(temp).code
            if resp == 200:
                temp1 = urllib.urlopen(temp).read()
                if texts and texts != 'N' in temp1:
                    print 'This site contains what you are looking for :D ...'
                    print 'Saving information to file ...'
                    abouttosave = open('targets.txt', 'a')
                    abouttosave.write(temp + '\n')
                    abouttosave.close()
                elif texts != 'N' and texts not in temp1:
                    print temp, 'does not contain your given words ...'
                    print 'Skipping ...'
                    loop += 1
                    continue
                elif texts == 'N':
                    print 'Woohoo!I found a site for you! :D'
                    print 'Saving information to file ...'
                    abouttosave = open('targets.txt', 'a')
                    abouttosave.write(temp + '\n')
                    abouttosave.close()
                    print 'Saved as \'targets.txt\' ...'
        except urllib2.URLError, checkurl:
            if checkurl == 404:
                print temp, 'seems to be not found ...'
                print 'Skipping ...'
                loop += 1
                continue
            else:
                print temp, 'is unreachable or doesn\'t exist ...'
                print 'Skipping ...'
                loop += 1
                continue
        loop += 1
    if lastip == workingip:
        break
    i += 1
