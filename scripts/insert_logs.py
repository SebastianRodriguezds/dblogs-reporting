import mysql.connector
from datetime import datetime, timedelta
import random

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="admin",
    database="system_logs"
)

cursor = db.cursor()

# test users
users = [
    ("Alice", "alice@email.com"),
    ("Bob", "bob@email.com"),
    ("Charlie", "charlie@email.com")
]

cursor.executemany("INSERT INTO users (username, email) VALUES (%s, %s)", users)
db.commit()

# aleatory logs
log_types_list  = ["INFO", "WARNING", "ERROR"]

for i in range(50):
    user_id = random.randint(1, 3)
    log_type= random.choice(log_types_list )
    message = f"Sample log message {i+1}"
    created_at = datetime.now() - timedelta(days=random.randint(0, 5))
    cursor.execute(
        "INSERT INTO logs (user_id, log_type, message, created_at) VALUES (%s, %s, %s, %s)",
        (user_id, log_type, message, created_at)
    )

db.commit()
cursor.close()
db.close()

print("Data inserted successffully!")
