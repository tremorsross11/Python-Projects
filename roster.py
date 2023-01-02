

import sqlite3

conn = sqlite3.connect('roster.db')
cur = conn.cursor()

cur.execute('INSERT INTO roster (name, species, IQ) VALUES (?, ?, ?)',
    ('Jean-Baptiste Zorg', 'Human', '122'))
cur.execute('INSERT INTO roster (name, species, IQ) VALUES (?, ?, ?)',
    ('Korben Dallas', 'Human', '100'))
cur.execute('INSERT INTO roster (name, species, IQ) VALUES (?, ?, ?)',
    ('Ak\'not', 'Mangalore', '-5'))
conn.commit()

print('Roster:')
cur.execute('SELECT name, species, IQ FROM roster')
for row in cur:
     print(row)

cur.execute('SELECT FROM roster WHERE species == "Human"')
conn.commit()

cur.close()
