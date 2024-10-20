
ALERT_THRESHOLD = 35  
ALERT_COUNT = 2

def check_alerts(city, temp_history):
    if len(temp_history) >= ALERT_COUNT:
        recent_temps = temp_history[-ALERT_COUNT:]
        if all(temp > ALERT_THRESHOLD for temp in recent_temps):
            print(f"ALERT: Temperature exceeded {ALERT_THRESHOLD}°C in {city} for {ALERT_COUNT} updates!")


city_temp_history = {}

def update_city_history(city, temp):
    if city not in city_temp_history:
        city_temp_history[city] = []
    city_temp_history[city].append(temp)
    check_alerts(city, city_temp_history[city])
