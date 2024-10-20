
import matplotlib.pyplot as plt

def plot_weather_summaries(dates, avg_temps, max_temps, min_temps, alert_dates=[]):
    plt.figure(figsize=(10, 6))

   
    plt.plot(dates, avg_temps, label='Average Temperature (°C)', marker='o', color='blue')
    plt.plot(dates, max_temps, label='Max Temperature (°C)', marker='v', color='red')
    plt.plot(dates, min_temps, label='Min Temperature (°C)', marker='^', color='green')

  
    if alert_dates:
        for alert_date in alert_dates:
            plt.axvline(x=alert_date, color='orange', linestyle='--', label=f'Alert on {alert_date}')

 
    plt.title("Daily Weather Summary")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()


    plt.tight_layout()
    plt.show()


dates = ['2024-10-17', '2024-10-18', '2024-10-19', '2024-10-20']
avg_temps = [29.5, 30.1, 31.3, 32.2]
max_temps = [33.2, 34.1, 35.5, 36.7]
min_temps = [25.4, 26.3, 27.5, 28.1]
alert_dates = ['2024-10-19', '2024-10-20']  

plot_weather_summaries(dates, avg_temps, max_temps, min_temps, alert_dates)
