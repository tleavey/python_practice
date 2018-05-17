# Tim Leavey
# Seed Program

import sqlite3

# Connect to the database
connection = sqlite3.connect('homework07.sqlite3.db')
c = connection.cursor()
# Villains
c.execute("INSERT INTO villains(name) VALUES ('Joker')")
c.execute("INSERT INTO villains(name) VALUES ('Darkseid')")
c.execute("INSERT INTO villains(name) VALUES ('Magneto')")
# Teams
c.execute("INSERT INTO teams(name) VALUES ('A-Team')")
c.execute("INSERT INTO teams(name) VALUES ('X-Men')")
c.execute("INSERT INTO teams(name) VALUES ('Justice League')")
# Powers
c.execute("INSERT INTO powers(name) VALUES ('Flight')")
c.execute("INSERT INTO powers(name) VALUES ('Invisibility')")
c.execute("INSERT INTO powers(name) VALUES ('X-Ray Vision')")
c.execute("INSERT INTO powers(name) VALUES ('Teleportation')")
c.execute("INSERT INTO powers(name) VALUES ('Immortality')")
c.execute("INSERT INTO powers(name) VALUES ('Telekinesis')")
c.execute("INSERT INTO powers(name) VALUES ('Super Rich')")
# Colors
c.execute("INSERT INTO colors(name) VALUES ('Blue')")
c.execute("INSERT INTO colors(name) VALUES ('Green')")
c.execute("INSERT INTO colors(name) VALUES ('Purple')")
c.execute("INSERT INTO colors(name) VALUES ('Yellow')")
c.execute("INSERT INTO colors(name) VALUES ('Orange')")
c.execute("INSERT INTO colors(name) VALUES ('White')")
c.execute("INSERT INTO colors(name) VALUES ('Black')")
# Superheroes
c.execute("INSERT INTO superheroes(name, villain_id, team_id) VALUES ('Batman','1','3')")
c.execute("INSERT INTO superheroes(name, villain_id, team_id) VALUES ('Superman','2','3')")
c.execute("INSERT INTO superheroes(name, villain_id, team_id) VALUES ('Wolverine','3','2')")
# Powers_Superheroes
c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES (1, 7)")
c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES (2, 1)")
c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES (2, 3)")
c.execute("INSERT INTO powers_superheroes(superhero_id, power_id) VALUES (3, 5)")
# Colors_Superheroes
c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES (1, 2)")
c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES (3, 3)")
c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES (6, 2)")
c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES (7, 1)")
c.execute("INSERT INTO colors_superheroes(color_id, superhero_id) VALUES (1, 3)")

connection.commit()
connection.close()

