
#This is a twitter enigma emulator.
#It is designed for fun and is not serious cryptography
#I am an American citizen; please do not rendition me.
##LulzTheNSA

#Get tweet, check length
def GetTweet():
	tweet = raw_input("Please write a tweet: ")	
	while len(tweet)>140:	
		tweet = raw_input("Please write a shorter tweet: ")
	print tweet
	return tweet

#PigIfy takes in a word, and outputs pig latin
def PigIfy(tweet):
	words = tweet.split()
	vowels = ["a", "e", "i", "o", "u", "y"]
	pig_list = []
	for i in words:
		flag = 0
		for j in vowels:
			if i[0].lower() == j:
				flag = 1
				break
		if i[0] == "#":
			pig_word = i
		#Insert regex to look for http: or . or / to skip word
		elif flag == 0:
			pig_word = i[1:]+i[0]+"ay"
		else:
			pig_word = i + "ay"
		pig_list.append(pig_word)
	pig = ""
	for i in pig_list:
		pig += i + " "
	return pig

def LeetIfy(tweet):
	words = tweet.split()
	leetDict = {"a":"@", "e":"3", "l":"1", "i":"|", "o":"0", "g":"6", "j":"9", "s":"z", "t":"7"}
	leet = ""
	for i in words:
		leet_word = i
		for j in range(len(i)):
			if i[j] == "#":
				break
			if i[j].lower() in leetDict:
				leet_word = leet_word[:j]+leetDict[i[j].lower()]+leet_word[(j+1):]
		leet+= leet_word + " "
	#cut the last space
	return leet

running = 1
while running == 1:
	tweet=GetTweet()
	print "Tweet= "+tweet
	print
	print "Press 1 to see your tweet in pig latin!"
	print "Press 2 to see your tweet in l33t sp3@k!"
	choice = raw_input(": ")
	while int(choice) > 2 & int(choice) < 0:
		print "Press 1 to see your tweet in pig latin!"
		print "Press 2 to see your tweet in l33t sp3@k!"
		choice = raw_input(": ")
	if choice == "1":
		pig_tweet=PigIfy(tweet)
		print "Pig Tweet= " + pig_tweet
	elif choice == "2":
		leet = LeetIfy(tweet)
		print "l33t Tweet= " + leet 
	else:
		print "Sorry that is not a valid option."
	cont = raw_input("Try Again (y/n)?")
	if cont.lower()=="n":
		running = 0
