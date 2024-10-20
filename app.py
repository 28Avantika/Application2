from flask import Flask, render_template, request
from flask_socketio import SocketIO
import sqlite3
import requests
from datetime import datetime
from weather_scheduler import start_run_weather_task

app = Flask(__name__)
socketio = SocketIO(app)

@app.template_filter('datetime')
def datetime_filter(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%d/%m/%Y, %I:%M:%S %p').replace("PM","pm")



@app.route('/')
def weather_summary():
    # Fetch stored weather data from the SQLite database
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather order by dt")
    summaries = cursor.fetchall()
    conn.close()

    return render_template('index.html', summaries=summaries)

api_key="1a2276fa9291f0b267abf643b37191b0"
status = requests.get(f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}")


if(status.status_code==401):
    print("API KEY IS NOT VALID")
else:
    if __name__ == '__main__':
        start_run_weather_task(socketio,api_key)
        socketio.run(app)
    
    