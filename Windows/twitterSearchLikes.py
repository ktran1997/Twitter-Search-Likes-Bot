import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("9PW2qIcuKZfMqzbFYUbam0SZF", 
	"rew7QnpbZF83tSkl0fh9utYTLFFPOE4VWrJGYbGioGpvwCwBIG")
auth.set_access_token("1276279253919608832-RXKuql22i7sf7URMretU49fAcu5ZUr", 
	"TntgXJpEq4rlzy3PT1gtbL0hLTAVI99kAKVQGIiURWBjg")

# Create API object
api = tweepy.API(auth)

saveFile = open('getLikedTweets.txt', 'a', encoding="utf-8")
saveFile.truncate(0)

for favorite in tweepy.Cursor(api.favorites, id="Kev1n_Trxn").items(20):
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



