import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('tasks.db')

# Create a cursor object
cursor = conn.cursor()

# Create the 'tasks' table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL
)
''')

print("Database and table created successfully!")

# Commit changes and close the connection
conn.commit()
conn.close()
