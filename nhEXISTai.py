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
        print(msg)

    elif req_pag.status_code == 404:
        msg = ("Magic number {0} does not exist ERROR 404".format(str(pag)))
        print(msg)
        return pag

    else:
        msg = ("Magic number {0} does not exist UNKNOWN ERROR"
               .format(str(pag)))
        print(msg)
        return pag

    """THE DELAY IS FOR SAFETY! DO NOT USE VERY SHORT VISIT TIMES
    (LESS THAN 1 SECOND) TO AVOID BEING BANNED ON THE WEBSITE!"""
    time.sleep(2)

def inputrange():
    
    star = int(input("Enter the first magic number to examine: "))
    end = int(input("enter the last magic number to examine: "))

    return star , end

def main(start=1, end=270000):

    start , end = inputrange()

    if start > end:
        msg = ("The end must be greater than the end")
        raise ValueError(msg)
    list = []

    for pag in range(start, end+1):
        Requests = req(pag)
        if Requests is not None:
            list.append(Requests)

    file_name = ('scraped ' + '(' + str(start) + "-" + str(end) + ')' + ".txt")
    file = open(file_name, "w")
    file.write("Nonexistent magic numbers in range: " + '(' + str(start) + "-"
               + str(end) + ')' + '\n')
    file.write(time.strftime("%d/%m/%y") + " "
               + time.strftime("%I:%M:%S") + '\n'*2)

    if len(list) == 0:
        file.write("No nonexistent magic numbers in range: " + '(' + str(start)
                   + "-" + str(end) + ')' + '\n')
    else:
        for pag in range(len(list)):
            file.write(str(list[pag]) + '\n')

    file.close()

    return print("The execution was successfully completed")



if __name__ == '__main__':
    main()
