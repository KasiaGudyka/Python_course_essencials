# program shows today's date and a current time for London, Warsaw, Moscow and Tokyo

# importing the data on current date and time
from datetime import datetime

# creating variable for the date
now = datetime.now()

# setting a time for Warsaw, Moscow and Tokyo
warsaw = str(now.hour + 1) + ":" + str(now.minute) + ":" + str(now.second)
moscow = str(now.hour + 3) + ":" + str(now.minute) + ":" + str(now.second)
tokyo = str(now.hour + 9) + ":" + str(now.minute) + ":" + str(now.second)

# adjusting the time if it's past midnight for Warsaw, Moscow and Tokyo
if warsaw > '24':
  warsaw = str(now.hour - 2) + ":" + str(now.minute) + ":" + str(now.second) + " (the next day)"
if moscow > '24':
  moscow = str(now.hour - 20) + ":" + str(now.minute) + ":" + str(now.second) + " (the next day)"
if tokyo > '24':
  tokyo = str(now.hour - 15) + ":" + str(now.minute) + ":" + str(now.second) + " (the next day)"


# printing the results
print ('Today\'s date: %02d/%02d/%04d \n\nCurrent time in: \nLondon: %02d:%02d:%02d\nWarsaw: %s \nMoscow: %s \nTokyo: %s' % 
       (now.month, now.day, now.year, now.hour, now.minute, now.second, warsaw, moscow, tokyo))
