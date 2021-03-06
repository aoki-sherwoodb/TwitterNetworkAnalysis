import tweepy
import pandas as pd
import numpy as np
import xlwt
from xlwt import Workbook

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret, tokens.ishishot)

auth.set_access_token(tokens.access_token,
tokens.access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True,wait_on_rate_limit_notify = True)

modi = "narendramodi"

friends = api.friends(modi, count = 5, skip_status = False, include_user_entities = False)
friends.remove(friends[6])

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#sheet1.write(0, 1, 'friend')
#sheet1.write(0, 2, 'extended friend')

i = 1
#for friend in friends:
 #   sheet1.write(i,1, friend.screen_name)
  #  sheet1.write(i,2, friend.id)
   # i += 1


for friend in friends:
    extFriends = api.friends(friend.id, count = 5, skip_status = False, include_user_entities = False)
    for extFriend in extFriends:
        #limit_handled(tweepy.Cursor(api.friends, friend.id, count = 3, skip_status = False, include_user_entities = False).items())
        sheet1.write(i,1, friend.screen_name)
        sheet1.write(i,2, extFriend.screen_name)
        i += 1

wb.save('xlwt bigger_group.xls')
