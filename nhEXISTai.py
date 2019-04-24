"""
    nhEXISTai is a is a small script that shows what pages of nh // entai.net
    exist or not and returns to the list of pages that do not exist.
"""

import requests
import time


def req(pag):

    req_pag = requests.get('https://nhentai.net/g/'+str(pag)+'/')

    if req_pag.status_code == 200:
        msg = ("Magic number {0} exist".format(str(pag)))

    else:
        msg = ("Magic number {0} does not exist".format(str(pag)))
        file = open('Nonexistent_magic_numbers.txt', "a")
        file.write(str(pag) + '\n')
        file.close()

    """ THE DELAY IS FOR SAFETY! DO NOT USE VERY SHORT VISIT TIMES
    (LESS THAN 1 SECOND) TO AVOID BEING BANNED ON THE WEBSITE!"""
    time.sleep(1)

    return print(msg)


def make_file():
    file = open('Nonexistent_magic_numbers.txt', "w")
    file.write("Nonexistent magic numbers" + '\n')
    file.write(time.strftime("%d/%m/%y") + " "
               + time.strftime("%I:%M:%S") + '\n'*2)
    file.close()


def main(start=1, end=270000):

    make_file()

    for pag in range(start, end+1):
        req(pag)

    print("The execution was successfully completed")


if __name__ == '__main__':
    main()
