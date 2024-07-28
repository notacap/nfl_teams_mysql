import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
username = 'lol not telling you'
password = 'lol definitely not telling you'
host = 'localhost'
database = 'nfl_stats'

# Create a database engine without specifying the database
engine = create_engine(f'mysql://{username}:{password}@{host}')

# Create the database if it doesn't exist
with engine.connect() as connection:
    connection.execute(text(f'CREATE DATABASE IF NOT EXISTS {database}'))

# Now connect to the database
engine = create_engine(f'mysql://{username}:{password}@{host}/{database}')

# Drop the existing teams table
with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS teams"))

# Load teams data from the CSV file
teams_data = pd.read_csv(r'C:\Users\PC\Desktop\code\data_files\nfl_teams.csv')

# Define the column names to match your CSV file
teams_data.columns = [col.title() for col in teams_data.columns]

# Drop the unwanted Id column
teams_data = teams_data.drop(columns=['Id'])

# Load teams data into the database
teams_data.to_sql("teams", engine, if_exists="replace", index=False)

# Read the data from the teams table
teams_data = pd.read_sql_table("teams", engine)

# Display the data
print(teams_data)