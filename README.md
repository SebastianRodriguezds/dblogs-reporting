## System Logs Report Generator
This project allows you to insert sample data into a MySQL database and generate visual and CSV reports from that data.
It consist of two main scripts:
* insert_logs.py → Insert sample users and logs into the dtabase.
* generate_report.py → Generates reports and visualizations based on the stored data.

## Requirements
Before running the scripts, make sure you have the following installed:
* Python 3.8+
* MySQL Server
* Python libraries:
 pin install mysql-connector-python pandas matplotlib seaborn

## Database Setup
1. Create a MySQL database named system_logs:
CREATE DATABASE system_logs;
USE system_logs;

2. Create the required tables:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    log_type VARCHAR(50),
    message TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

3. Update your MySQL credentials in both scripts if necessary:
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="system_logs"
)

## How to use
1. Insert Sample Data
Run the follwing command to populate the database with sample users and log records:
python scripts/insert_logs.py
This will insert:
* 3 samples users
* 50 random log records (INFO, WARNING, ERROR)

2. Generate Reports and Visualizations
Once the data is inserted, run:
python scripts/generate_reports.py

