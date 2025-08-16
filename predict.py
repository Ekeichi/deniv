import sqlite3
import pandas as pd

conn = sqlite3.connect("data/strava.db")
df = pd.read_sql("SELECT * FROM activities", conn)

print(df.head())


