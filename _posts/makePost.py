import sys
import datetime

today = datetime.date.today()
fileName = str(today) + "-status"
monthDict={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
month = monthDict[today.month]
day = today.day

newPost = open(fileName+".md", "w")
newPost.write("---\nlayout: post \ntitle: Status for " + str(month) + " " + str(day) + " \nauthor: Tad\n---\n \n## What did I work on today? \n \n* \n  \n## What should I be working on tomorrow \n* \n \n \n \n--- \n \n### Listening to: \n <iframe src='https://embed.spotify.com/?uri=spotify:track:3bSU0s2VRIP7w82DwJietw' width='300' height='380' frameborder='0' allowtransparency='true'></iframe> \n <i class='fa fa-code' style='color:pink'> </i> ")
newPost.close()

sys.exit(0) # quit Python
