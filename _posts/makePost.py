import sys
import datetime

today = datetime.date.today()
fileName = str(today) + "-status"
monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
month = monthDict[today.month]
day = today.day

newPost = open(fileName+".md", "w")
newPost.write("--- \n layout: post \n  title: Status for" + str(month) + " " + str(day) + " \n author: Tad \n  ---")
newPost.close()

sys.exit(0) # quit Python

write()
