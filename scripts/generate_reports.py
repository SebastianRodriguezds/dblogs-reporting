import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# db conneciton
db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="system_logs",
)

# load data to dataFrame
users_df = pd.read_sql("SELECT * FROM users", con=db)
losg_df = pd.read_sql("SELECT * FROM logs", con=db)

#reports directory
reports_dir = os.path.join(os.path.dirname(__file__), "../reports")
os.makedirs(reports_dir, exist_ok=True)

# top 5 users with more errors
error_logs = losg_df[losg_df['log_type']== 'ERROR']
top_users = error_logs.groupby('user_id').size().sort_values(ascending=False).head(5)

# Save reports csv
top_users.to_csv(os.path.join(reports_dir, "top_users_errors.csv"), index=True)
losg_df.to_csv(os.path.join(reports_dir, "all_logs.csv"), index=False)

# visualization 1: Count of log types
plt.figure(figsize=(6,4))
sns.countplot(x='log_type', data=losg_df, order=['INFO', 'WARNING', 'ERROR'])
plt.title('Log Type Counts')
plt.xlabel('Log Type')
plt.ylabel('Count')
plt.savefig(os.path.join(reports_dir, "log_type_counts.png"))
plt.close()

#visualization 2
plt.figure(figsize=(6,4))
sns.barplot(x=top_users.index, y=top_users.values)
plt.title("Top 5 Users with most ERROR Logs")
plt.xlabel("User ID")
plt.ylabel("Number of ERROR Logs")
plt.savefig(os.path.join(reports_dir, "top_users_errors.png"))
plt.close()

print("Reports and visualizations generated successfully!")