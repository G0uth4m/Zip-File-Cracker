# Zip-File-Cracker
A python2 based tool to recover(crack) passwords of zip files.

## Usage :

```
$ python zipCrack.py -h
Usage: zipCrack.py [options]

Options:
  -h, --help  show this help message and exit
  -f FILE     Zip file to be cracked
  -d FILE     Wordlist
```
Default wordlist is included - 1mm.txt

## Example :

```
$ python zipCrack.py -f test.zip -d 1mm.txt
[+] Password cracked: india
[+] 1580 password attempts per second.
```

## Author
* **Goutham** - [G0uth4m](https://github.com/G0uth4m)
