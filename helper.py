from random import randrange 
from random import randint
#combat round 1 

p1 = raw_input("What is the first player's name? ")
p2 = raw_input("What is the second player's name? ")
p3 = raw_input("What is the third player's name? ")
p4 = raw_input("What is the fourth player's name? ")

#p1_init = randrange(1,21)
#p2_init = randrange(1,21)
#p3_init = randrange(1,21)
#p4_init = randrange(1,21)

'''
def player_init(self,player,a,b):
	return self.randrange(int(a),int(b+1))
'''

def player_init(player):
	return randint(1,21)

p1_init = player_init(p1)
print p1_init
p2_init = player_init(p2)
print p1_init
p3_init = player_init(p3)
print p1_init
p4_init = player_init(p4)
print p1_init


custom = 0 
#insert try/catch phrase to catch exceptions 

def action(choice):
	if choice == 'move': 
		return p1_init - 2
	elif choice == 'attack':
		if weapon == 'light weapon':
			return p1_init - 4 
		elif weapon == 'heavy weapon':
			return p1_init - 7 
		else: 
			return p1_init - custom 
	elif choice == 'cast spell':
		return p1_init - 3 
	else: 
		return p1_init 
print "Okay, your action is set for this turn."

p1_action = raw_input('What action would the first player like to take? ')
p1_final = action(p1_action)

p2_action = raw_input('What action would the second player like to take? ') 
p2_final = action(p2_action)

p3_action = raw_input('What action would the third player like to take? ')
p3_final = action(p3_action)

p4_action = raw_input('What action would the fourth player like to take? ')
p4_final = action(p4_action)

'''
p1_action = raw_input('What action would the first player like to take? ')
if p1_action == 'move': 
	p1_final = p1_init - 2
elif p1_action == 'attack':
	if p1_weapon == 'light weapon':
		p1_final = p1_init - 4 
	elif p1_weapon == 'heavy weapon':
		p1_final = p1_init - 7 
	else: 
		p1_final = p1_init - custom 
elif p1_action == 'cast spell':
	p1_final = p1_init - 3 
else: 
	p1_final = p1_init 
print "Okay, your action is set for this turn."

p2_action = raw_input('What action would the second player like to take? ')
if p2_action == 'move': 
	p2_final = p2_init - 2
elif p2_action == 'attack':
	if p2_weapon == 'light weapon':
		p2_final = p2_init - 4 
	elif p2_weapon == 'heavy weapon':
		p2_final = p2_init - 7 
	else: 
		p2_final = p2_init - custom 
elif p2_action == 'cast spell':
	p2_final = p2_init - 3 
else: 
	p2_final = p2_init 
print "Okay, your action is set for this turn."

p3_action = raw_input('What action would the third player like to take? ')
if p3_action == 'move': 
	p3_final = p3_init - 2
elif p3_action == 'attack':
	if p3_weapon == 'light weapon':
		p3_final = p3_init - 4 
	elif p3_weapon == 'heavy weapon':
		p3_final = p3_init - 7 
	else: 
		p3_final = p3_init - custom 
elif p3_action == 'cast spell':
	p3_final = p3_init - 3 
else: 
	p3_final = p3_init 
print "Okay, your action is set for this turn."

p4_action = raw_input('What action would the fourth player like to take? ')
if p4_action == 'move': 
	p4_final = p4_init - 2
elif p4_action == 'attack':
	if p4_weapon == 'light weapon':
		p4_final = p4_init - 4 
	elif p4_weapon == 'heavy weapon':
		p4_final = p4_init - 7 
	else: 
		p4_final = p4_init - custom 
elif p4_action == 'cast spell':
	p4_final = p4_init - 3 
else: 
	p4_final = p4_init 
print "Okay, your action is set for this turn."
'''
order = [p1_final, p2_final, p3_final, p4_final] 
print sorted(order,reverse=True)

