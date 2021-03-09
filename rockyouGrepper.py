#!/usr/bin/python

import sys
import uuid

def main():

    if len(sys.argv) <= 2:
        sys.stdout.write("\t-::: rockyouGrepper.py :::-\n")
        sys.stdout.write("# Creates a smaller wordlist by grepping a custom wordlist against rockyou or large wordlist.\n")
        sys.stdout.write("\nUsage: ./rockyouGrepper.py [/path/to/rockyou.txt] [/path/to/user_wordlist]\n " % (sys.argv[0]))
        sys.stdout.flush()
        exit(0)

    rockyou = open(sys.argv[1], 'r')
    rockyouwords = rockyou.readlines()
    
    custom_wordlist = []
    
    user_list = open(sys.argv[2], 'r')
    user_list_words = user_list.readlines() #TODO: Fix encoding error with python3 readlines()
    
    for word in rockyouwords:
        for words in user_list_words:
            if words in word.lower():
                custom_wordlist.append(word.strip('\n'))
    
    tf = "newList_" + str(uuid.uuid4())[0:5] + ".txt"
    
    with open(tf, 'w') as f:
        for x in custom_wordlist:
            f.write('%s\n' % x)

    print("Your wordlist is at ./" + tf)

if __name__ == "__main__":
    main()
