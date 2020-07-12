import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API Key", 
	"API Secret Key")
auth.set_access_token("Access Token", 
	"Access Token Secret")

# Create API object
api = tweepy.API(auth)

saveFile = open('getLikedTweets.txt', 'a', encoding="utf-8")
saveFile.truncate(0)

for favorite in tweepy.Cursor(api.favorites, id="Username of Person Searching").items(20):
	saveFile.write("%s %s %s %s \n"%(
		'Screen Name: '+str(favorite.user.screen_name)+',', 
		'Name: '+str(favorite.user.name)+',', 
		'Tweet Id: https://twitter.com/user/status/'+str(favorite.id)+',',
		'Tweet Text: '+str(favorite.text)
		))

saveFile.close()

searchFile = open('getLikedTweets.txt', 'r', encoding="utf-8")
print("Hello, Which tweet would you like to find? ")
userInput = input()

for line in searchFile:
    if userInput in line: 
    	line.replace(',','\n')
    	print(line)

searchFile.close()



