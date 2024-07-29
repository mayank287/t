import datetime

def create_weather_data(start_date, end_date):


  weather_data = []
  current_date = start_date
  while current_date <= end_date:
    weather_data.append({
      'date': current_date,
      'max_temp': random.randint(20, 35),
      'min_temp': random.randint(15, 25),
      'humidity': random.randint(50, 80)
    })
    current_date += datetime.timedelta(days=1)
  return weather_data

def find_highest_lowest_temps(weather_data):


  max_temp = float('-inf')
  min_temp = float('inf')
  for day in weather_data:
    max_temp = max(max_temp, day['max_temp'])
    min_temp = min(min_temp, day['min_temp'])
  return max_temp, min_temp

def days_above_30(weather_data):


  count = 0
  for day in weather_data:
    if day['max_temp'] > 30:
      count += 1
  return count

def average_humidity(weather_data):


  total_humidity = sum(day['humidity'] for day in weather_data)
  return total_humidity / len(weather_data)

if __name__ == "__main__":
  start_date = datetime.date(2024, 8, 1)
  end_date = datetime.date(2024, 8, 10)
  weather_data = create_weather_data(start_date, end_date)

  highest_temp, lowest_temp = find_highest_lowest_temps(weather_data)
  print("Highest temperature:", highest_temp, "°C")
  print("Lowest temperature:", lowest_temp, "°C")

  days_above_30_count = days_above_30(weather_data)
  print("Number of days above 30°C:", days_above_30_count)

  avg_humidity = average_humidity(weather_data)
  print("Average humidity:", avg_humidity, "%")
