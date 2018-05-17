# TIM LEAVEY
# SUPERHERO APP

# This program does NOT used prepared statements, meaning it's vulnerable to SQL injections.
# This was intentional as a lesson in what NOT to do.

import sys
import sqlite3

# Initial welcome display for user
print('Welcome to the superheroes archive!')
print('1. Superheroes')
print('2. Villains')
print('3. Teams')
print('4. Powers')
print('5. Colors')
user_choice = input('Your command: ')

# Connect to the database
connection = sqlite3.connect('homework07.sqlite3.db')
c = connection.cursor()

# SUPERHEROES
if user_choice == 1:
	# DISPLAY SUPERHERO LIST
	c.execute('SELECT superheroes.name, teams.name, villains.name FROM superheroes, teams, villains WHERE team_id=teams.id AND villains.id=villain_id;') 
	superheroes_data = c.fetchall()
	for superhero in superheroes_data:
		print superhero[0]
		print 'Team: ',superhero[1]
		print 'Nemesis: ',superhero[2]
		c2 = connection.cursor()
		# DISPLAYING ALL THE POWERS
		c2.execute("SELECT powers.name FROM powers JOIN powers_superheroes ON power_id=powers.id JOIN superheroes ON superhero_id=superheroes.id WHERE superheroes.name= '%s'" % superhero[0])
		powers_data = c2.fetchall()
		sys.stdout.write('Powers: ')
		for power in powers_data:
			if len(powers_data) > 1:
				if power != powers_data[-1]:
					sys.stdout.write(power[0]+', ')
				else:
					sys.stdout.write(power[0])
					print
			else:
				sys.stdout.write(power[0])
				print
		# DISPLAYING ALL THE COLORS
		c3 = connection.cursor()
		c3.execute("SELECT colors.name FROM colors JOIN colors_superheroes ON color_id=colors.id JOIN superheroes ON superhero_id=superheroes.id WHERE superheroes.name= '%s'" % superhero[0])
		colors_data = c3.fetchall()
		sys.stdout.write('Costume Colors: ')
		for color in colors_data:
			if len(colors_data) > 1:
				if color != colors_data[-1]:
					sys.stdout.write(color[0]+', ')
				else:
					sys.stdout.write(color[0])
					print
			else:
				sys.stdout.write(color[0])
				print		
		print
	user_adds_or_quits = raw_input('(A)dd a new superhero, or (Q)uit?')
	add_superhero = 'a'
	quit = 'q'
	# ADDING A SUPERHERO
	if user_adds_or_quits.lower() == add_superhero:
		print 'Adding a New Superhero'
		new_superhero = raw_input('Superhero Name: ')
		# VILLAIN INFO
		print 'Arch enemy:'
		c.execute('SELECT * FROM villains;')
		villains_data = c.fetchall()
		for one_villain in villains_data:
			villain_identifier = str(one_villain[0])
			print villain_identifier + ". " + one_villain[1]
		villain_id = input('')
		# TEAM INFO
		print 'Team:'
		c.execute('SELECT * FROM teams;')
		teams_data = c.fetchall()
		for one_team in teams_data:
			team_identifier = str(one_team[0])
			print team_identifier + ". " + one_team[1]
		team_id = input('')
		c.execute("INSERT INTO superheroes(name, villain_id, team_id) VALUES ('%s', '%s', '%s')" % (new_superhero, villain_id, team_id))
		connection.commit()
		# COLOR INFO
		print 'Colors:'
		c.execute('SELECT * FROM colors;')
		colors_data = c.fetchall()
		for one_color in colors_data:
			color_identifier = str(one_color[0])
			print color_identifier + ". " + one_color[1]
		color_id = input('')
		c2 = connection.cursor()
		c2.execute('SELECT id FROM superheroes;')
		superhero_ids = c2.fetchall()
		new_superhero_id = superhero_ids[-1][0]
		c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES ('%s', '%s')" % (color_id, new_superhero_id))
		yes = 'y'
		user_choice = yes
		# ADD MULTIPLE COLORS
		while user_choice.lower() == 'y':
			user_choice = raw_input('Add another color? (Y)es or (N)o: ')
			if user_choice.lower() == 'y':
				print 'Colors:'
				for one_color in colors_data:
					color_identifier = str(one_color[0])
					print color_identifier + ". " + one_color[1]
				color_id = input('')
				c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES ('%s', '%s')" % (color_id, new_superhero_id))
		connection.commit()
		# POWERS INFO
		print 'Powers:'
		c.execute('SELECT * FROM powers;')
		powers_data = c.fetchall()
		for one_power in powers_data:
			power_identifier = str(one_power[0])
			print power_identifier + ". " + one_power[1]
		power_id = input('')
		c2 = connection.cursor()
		c2.execute('SELECT id FROM superheroes;')
		superhero_ids = c2.fetchall()
		new_superhero_id = superhero_ids[-1][0]
		c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES ('%s', '%s')" % (new_superhero_id, power_id))
		yes = 'y'
		user_choice = yes
		# ADD MULTIPLE POWERS
		while user_choice.lower() == 'y':
			user_choice = raw_input('Add another power? (Y)es or (N)o: ')
			if user_choice.lower() == 'y':
				print 'Powers:'
				for one_power in powers_data:
					power_identifier = str(one_power[0])
					print power_identifier + ". " + one_power[1]
				power_id = input('')
				c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES ('%s', '%s')" % (new_superhero_id, power_id))
		connection.commit()		
		connection.close()
	# USER QUITS	
	elif user_adds_or_quits.lower() == quit:
		print 'Quitting'
		connection.close()
	else:
		print 'BAD INPUT... QUITTING'
		connection.close()

# VILLAINS
elif user_choice == 2:
	# DISPLAY VILLAIN LIST
	print 'Villains: '
	c.execute('SELECT name FROM villains;')
	villains_names =  c.fetchall()
	for name in villains_names:
		print name[0]
	user_adds_or_quits = raw_input('(A)dd a new villain, or (Q)uit?')
	add_villain = 'a'
	quit = 'q'
	# ADD NEW VILLAIN TO DB
	if user_adds_or_quits.lower() == add_villain:
		print 'Adding a New Villain'
		new_villain = raw_input('Villain Name: ')
		c.execute("INSERT INTO villains(name) VALUES ('%s')" % new_villain)
		connection.commit()
		connection.close()
	# QUIT
	elif user_adds_or_quits.lower() == quit:
		print 'Quitting'
		connection.close()
	else:
		print 'BAD INPUT... QUITTING'
		connection.close()

# TEAMS
elif user_choice == 3:
	# DISPLAY TEAM LIST
	print 'Teams: '
	c.execute('SELECT name FROM teams;')
	team_names =  c.fetchall()
	for name in team_names:
		print name[0]
	user_adds_or_quits = raw_input('(A)dd a new team, or (Q)uit?')
	add_team = 'a'
	quit = 'q'
	# ADD NEW TEAM
	if user_adds_or_quits.lower() == add_team:
		print 'Adding a New Team'
		new_team = raw_input('Team Name: ')
		c.execute("INSERT INTO teams(name) VALUES ('%s')" % new_team)
		connection.commit()
		connection.close()
	# QUIT
	elif user_adds_or_quits.lower() == quit:
		print 'Quitting'
		connection.close()
	else:
		print 'BAD INPUT... QUITTING'
		connection.close()

# POWERS
elif user_choice == 4:
	# DISPLAY POWERS LIST
	print 'Powers: '
	c.execute('SELECT name FROM powers;')
	power_names =  c.fetchall()
	for name in power_names:
		print name[0]
	user_adds_or_quits = raw_input('(A)dd a new power, or (Q)uit?')
	add_power = 'a'
	quit = 'q'
	# ADD NEW POWER TO DB
	if user_adds_or_quits.lower() == add_power:
		print 'Adding a New Power'
		new_power = raw_input('Power Name: ')
		c.execute("INSERT INTO powers(name) VALUES ('%s')" % new_power)
		connection.commit()
		connection.close()
	# QUIT
	elif user_adds_or_quits.lower() == quit:
		print 'Quitting'
		connection.close()
	else:
		print 'BAD INPUT... QUITTING'
		connection.close()

# COLORS
elif user_choice == 5:
	# DISPLAY COLOR LIST
	print 'Costume Colors: '
	c.execute('SELECT name FROM colors;')
	color_names =  c.fetchall()
	for name in color_names:
		print name[0]
	user_adds_or_quits = raw_input('(A)dd a new team, or (Q)uit?')
	add_color = 'a'
	quit = 'q'
	# ADD NEW COLOR TO DB
	if user_adds_or_quits.lower() == add_color:
		print 'Adding a New Color'
		new_color = raw_input('Color Name: ')
		c.execute("INSERT INTO colors(name) VALUES ('%s')" % new_color)
		connection.commit()
		connection.close()
	# QUIT
	elif user_adds_or_quits.lower() == quit:
		print 'Quitting'
		connection.close()
	else:
		print 'BAD INPUT... QUITTING'
		connection.close()
else:
	print('Bad input. Numbers 1 - 5 only.')
	connection.close()