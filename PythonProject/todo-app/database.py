import sqlite3
import os
from cryptography.fernet import Fernet

# Generate an encryption key (run once and save securely)
# key = Fernet.generate_key()
# Save this key in an environment variable
key = os.getenv('ENCRYPTION_KEY')
cipher_suite = Fernet(key)

def add_task_to_db(task):
    encrypted_task = cipher_suite.encrypt(task.encode())
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (encrypted_task,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT id, task FROM tasks')
    tasks = c.fetchall()
    # Decrypt tasks before returning
    decrypted_tasks = [(task[0], cipher_suite.decrypt(task[1]).decode()) for task in tasks]
    conn.close()
    return decrypted_tasks