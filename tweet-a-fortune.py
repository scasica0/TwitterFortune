
import random
import sqlite3
from twitter import *


def main():   

#authenticate Twitter Account (tokens and consumer keys have been removed)
    t = Twitter(
    auth=OAuth(TOKEN, TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)
    )
    
#seeds random number    
    random.seed(a=None, version=2)

#connection to fortune database
    conn = sqlite3.connect('freebsd_fortunes_clean.sl3')
    c = conn.cursor()
    
    while True:

        fortuneTuple = []
#generates random number between 1 and 14334 (total number of rows for fortune)
        fortuneNum = random.randint(1, 14334)

#selects fortune from fortune database given random number
        stmt = "select aphorism from fortunes where id=%d" % fortuneNum

#forms tuple from database and converts to string
        for row in c.execute(stmt):
            fortuneTuple += row   
        fortune = ''.join(fortuneTuple)

#verification that length is less than 140 characters & if so, post to twitter
        if len(fortune) < 140:
            t.statuses.update(
            status= fortune)
            break

    conn.close()

#randomly select image in directory
    imageNum = random.randint(1, 5)

    if imageNum == 1:
        image = "test1.png"
    elif imageNum == 2:
        image = "test2.png"
    elif imageNum == 3:
        image = "test3.png"
    elif imageNum == 4:
        image = "test4.png"
    elif imageNum == 5:
        image = "test5.png"

#post image to twitter
    with open(image, "rb") as imagefile:
        params = {"media[]": imagefile.read()}
    t.statuses.update_with_media(**params)

if __name__== "__main__":
    main()
        
