import zipfile
from time import time
import optparse

def zipCrack(zfile, dictionary):
    try:
        myZip = zipfile.ZipFile(zfile)
    except zipfile.BadZipfile:
        print "[!] There was an error opening your zip file."
        return

    password = ''
    
    timeStart = time()
    with open(dictionary, "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                myZip.extractall(pwd = password)
                totalTime = time() - timeStart
                print "\033[92m[+] Password cracked: %s" % password
                print "\033[92m[+] %i password attempts per second." % (pass_count/totalTime)
                return
            except Exception as e:
                if str(e[0]) == 'Bad password for file':
                    pass # TODO: properly handle exceptions?
                elif 'Error -3 while decompressing' in str(e[0]):
                    pass # TODO: properly handle exceptions?
                else:
                    print e
        print "\033[91m[-] Sorry, password not found."


def main():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest = "zfile", help = "Zip file to be cracked", metavar="FILE")
    parser.add_option("-d", dest = "dictionary", help = "Wordlist", metavar="FILE")

    (options, args) = parser.parse_args()

    zfile = str(options.zfile)
    dictionary = str(options.dictionary)

    if(zfile == None or dictionary == None):
        print parser.usage
    else:
        zipCrack(zfile, dictionary)   

if(__name__ == "__main__"):
    main()      

