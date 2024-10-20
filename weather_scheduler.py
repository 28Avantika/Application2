import time
import requests
import threading
import time
import sqlite3
socketio=None

def fetch_and_save_weather_data(city,api_key):
    # Example using OpenWeatherMap API (replace with a real API URL and key)
    

    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"
    
    response = requests.get(url)
    weather_data = response.json()

    # Extract relevant information
    main_condition = weather_data['weather'][0]['main']  # Main weather condition (Rain, Snow, etc.)
    temp = weather_data['main']['temp']  # Current temperature in Celsius
    feels_like = weather_data['main']['feels_like']  # Perceived temperature in Celsius
    timestamp = weather_data['dt']  # Time of the data update (Unix timestamp)

    # Save the data into the SQLite database
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                      (city TEXT, main TEXT, temp REAL, feels_like REAL, dt INTEGER)''')
    
    # Insert data into the table
    cursor.execute("INSERT INTO weather (city, main, temp, feels_like, dt) VALUES (?, ?, ?, ?, ?)",
                   (city, main_condition, temp, feels_like, timestamp))
    
    conn.commit()
    conn.close()

    # Return the data for potential real-time updates
    return [city, main_condition, temp, feels_like, timestamp]

def run_weather_task(socketio,api_key):
    while True:
        # List of cities to fetch weather for
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        
        for city in cities:
            summary = fetch_and_save_weather_data(city,api_key)
            print(f"Weather data for {city} has been fetched and saved.")
            
            # Emit the data to all connected clients via SocketIO
            socketio.emit('new_weather_data', {'summary': summary})

        # Wait for 5 minutes before running the task again
        # time.sleep(300)
        time.sleep(5)


def start_run_weather_task(socketio,api_key):
    # Create a thread for the weather task
    weather_thread = threading.Thread(target=run_weather_task, args=(socketio,api_key))
    
    # Set the thread as a daemon so it closes when the main app closes
    weather_thread.daemon = True
    
    # Start the thread
    weather_thread.start()