#smashreddit tier list bot

import praw
import os
import re

#login
def login():
	reddit = praw.Reddit(client_id = 'dKSMxFdhjE0JrA',
					client_secret = '8sWnOE94WCMs9aJL9_pZZmkF2GA',
					username = 'tierbot',
					password = 'tierbot1234',
					user_agent = 'tierbot by /u/adknight_')
	print("logged in!")
	return reddit

#subreddits
def subreddit_set(r):
	s = r.subreddit('smashbros')
	print("subreddit set!")
	return s

#phrase to activate bot
def keyphrase():
	keyphrase = '!tier '
	print("keyphrase set!")
	return keyphrase

#obtains the word right AFTER keyphrase
def obtain_valid_word(comment_body):
	comment_body = re.split('\n| ', comment_body)
	return comment_body[1]

# look for keyphrase and return the response
def run_bot(s, keyphrase, comments_replied_to):

	for comment in s.stream.comments():
		if keyphrase in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			word = obtain_valid_word(comment.body)
			try:
				if (word == "melee"):
					comment.reply("The current Melee tierlist can be found [here](https://smashboards.com/tiers/#Melee)")
					comments_replied_to.append(comment.id)
					
					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")
					
					print('posted melee')
				elif (word == "64"):
					comment.reply("The current Smash 64 tierlist can be found [here](https://smashboards.com/tiers/#Smash64)")
					comments_replied_to.append(comment.id)

					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")
					
					print('posted 64')
				elif (word == "pm"):
					comment.reply("The current Project M tierlist can be found [here](https://smashboards.com/tiers/#ProjectM)")
					comments_replied_to.append(comment.id)
					
					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")
					
					print('posted pm')
				elif (word == "brawl"):
					comment.reply("The current Brawl tierlist can be found [here](https://smashboards.com/tiers/#Brawl)")
					comments_replied_to.append(comment.id)
					
					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")

					print('posted brawl')
				elif (word == "smash4"):
					comment.reply("The current Smash 4 tierlist can be found [here](https://smashboards.com/tiers/#WiiU)")
					comments_replied_to.append(comment.id)

					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")

					print('posted smash4')
				else:
					comment.reply("Sorry, that is an invalid game! Try again by commenting either 64, melee, brawl, pm, or smash4! (ex:!tier melee)")
					comments_replied_to.append(comment.id)

					with open ("comments_replied_to.txt", "a") as f:
						f.write(comment.id + "\n")

					print('posted invalid game')
			#except catches if word is invalid
			except:
				print('to frequent')

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
	
	return comments_replied_to

#main
r = login()
s = subreddit_set(r)
keyphrase = keyphrase()

#keeps track of the comments we replied to
comments_replied_to = get_saved_comments()

#to make it loop forever, use while True: run_bot(r, keyphrase)
while True:
	run_bot(s, keyphrase, comments_replied_to)