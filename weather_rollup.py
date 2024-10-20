
import sqlite3

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS weather_summary (
                    city TEXT, 
                    date TEXT, 
                    avg_temp REAL, 
                    max_temp REAL, 
                    min_temp REAL, 
                    dominant_condition TEXT)''')


def insert_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition):
    cursor.execute('''INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''', (city, date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()

conn.close()

import statistics

def calculate_daily_summary(city, daily_data):
    temps = [data['temp'] for data in daily_data]
    conditions = [data['condition'] for data in daily_data]
    
    avg_temp = statistics.mean(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    dominant_condition = max(set(conditions), key=conditions.count)

    return avg_temp, max_temp, min_temp, dominant_condition
