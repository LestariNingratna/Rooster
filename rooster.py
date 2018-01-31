from sys import exit

def golden():
	next = raw_input("\n> ")
	
	if next == "egg number 1":
		print "Congratulation! You chose the correct egg. You win!\n\n"
		print "000000000000000_000000000000000"
		print "00000000000000___00000000000000"
		print "0000000000000_____0000000000000"
		print "000000000000_______000000000000"
		print "00000000000_________00000000000"
		print "0____________ YOU ___________00"
		print "000_________ ........_________ 0000"
		print "00000 _______ROCK!!_______ 00000"
		print "0000000_________________0000000"
		print "000000_________0_________000000"
		print "00000_______0000000_______00000"
		print "0000_____0000000000000_____0000"
		print "000___0000000000000000000___000"
		print "00_0000000000000000000000000_00"
		print "8888888888888888888888888888888"
		print "8888___88888888888888888___8888"
		print "888_____888888888888888_____888"
		print "888_____888888888888888_____888"
		print "888_____888888888888888_____888"
		print "888_____888888888888888_____888"
		print "888_____888888888888888_____888"
		print "888_____888888888888888_____888"
		print "888_____88____888____88_____888"
		print "888_____8______8______8_____888"
		print "888_____8______8______8_____888"
		print "888_____8______8______8_____888"
		print "888_____8______8______8_____888"
		print "888_____8____888888888888888888"
		print "888_____8___88_____________8888"
		print "888_____8__88_______________888"
		print "888______888_________________88"
		print "888________88_________________8"
		print "888__________88_______________8"
		print "888____________88_____________8"
		print "888_____________88___________88"
		print "888______________8___________88"
		print "888_______________8__________88"
		print "888_______________8_________888"
		print "8888_______________________8888"
		print "88888_____________________88888"
		print "8888888888888888888888888888888"
	elif next == "egg number 2":
		dead("Sorry, you picked the wrong egg. Enjoy your fake egg.")
	else:
		print "I got no idea what that means."
		golden()
				
def catmeow():
	next = raw_input("\n> ")
	
	if next == "attack":
		dead("the cat chased you and killed you.")
	elif next == "run":
		print "you espaced from grumpy cat. Good job!"
		print "\nNow there's a busy road in front of you. Will you \'1. cross the road\' or \'2. stay still\'?"
		road()
	else:
		print "I got no idea what that means."
		catmeow()
		
def road():
	next = raw_input("\n> ")
	
	if next == "1":
		print "\nThere's a car coming at you at high speed."
		print "The only way to save you from being flattened by car is answering this riddle correctly.\n"
		print "Why did chicken cross the road?\n\n 1. to get to the other side\n 2. to get the golden egg\n"
		riddle()
	elif next == "2":
		dead ("you wander around until you starve")
	else:
		print "I got no idea what that means."
		road()
	
def riddle():
	next = raw_input("\n> ")
	
	if next == "1":
		dead("Rest In Peace.")
	elif next == "2":
		print "You managed to dodge your death and cross the road safely."
		print "Now finally you can see the museum right in front of you."
		print "The front door is open. You walk inside the museum. You see 2 golden eggs. One of them is only a replica and another one is the real golden egg."
		print "Which one do you choose?"
		print "\negg number 1\negg number 2"
		golden()
	else:
		print "I got no idea what that means."
		riddle()
		
def doggo():
	next = raw_input("\n> ")
	
	if next == "attack":
		dead("Moon moon chased you and raped you to death.")
	elif next == "run":
		print "you escaped from moon moon. Good job!"
		print "\nNow there's a busy road in front of you. Will you \'1. cross the road\' or \'2. stay still\'?"
		road()
	else:
		print "I got no idea what that means."
		doggo()
		
	
def farm():
	next = raw_input("\n> ")
	
	if next == "1":
		print "\nYou're now outside and free!\n\nWhich direction do you want to take?\n"
		print "1. north\n2. west\n3. south\n4. east"
		escapingrun()
	elif next == "2":
		dead("\nThe owner catched you and brought you out and then he slaughters you.")
	else:
		print "I got no idea what that means."
		farm()
		
def escapingrun():
	next = raw_input("\n> ")
	
	if next == "1":
		print "you're back to the chicken farm. \'sneak out\' or \'stay\'?"
		farm()
	elif next == "2":
		print "\nYou see a grumpy cat looking at you.\n\nrun\nattack\n\nWhich one do you choose?"
		catmeow()
	elif next == "3":
		dead("you wander around until you starve.")
	elif next == "4":
		print "\nYou see a giant moon moon looking at you.\n\nrun\nattack\n\nWhich one do you choose?"
		doggo()
	else:
		print "I got no idea what that means."	
		escapingrun()
	

def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "---------------------------------------------------------------------------------------------\n"
	print "Welcome to The Adventure of a Rooster!\n"
	print "---------------------------------------------------------------------------------------------\n"
	print "You're in chicken farm. You live a peaceful life as a rooster. But other chickens buzzing about The Golden egg."
	print "They said this golden egg is in a museum far away from chicken farm."
	print "You see your owner opens the door. You can \'1. sneak out\' or \'2. stay\'. Which one do you choose?"
	farm()
	
start()