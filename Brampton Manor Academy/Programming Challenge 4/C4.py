temperatures = [10.0, 0.0, -10.0]
speeds = [15, 25, 35]
dictionary = dict(zip(temperatures, speeds))

def quantify(air_temp, air_speed):
  windchill = 35.74 + 0.6215* air_temp - 35.75* air_speed ** 0.16 + 0.4275 * air_temp* air_speed**0.16
  return windchill

i = 0
while i < len(temperatures):
  windchill = quantify(temperatures[i], speeds[i])
  print(f"Temperature of {temperatures[i]} and speed of {speeds[i]} gives windchill of:  {windchill}")
  i= i +1

user_temp = float(input("Temperature: "))
user_speed = int(input("Speed: "))

windchill = quantify(user_temp, user_speed)
print(f'Windchill: {windchill}')
#for i in range(0,len(temperatures)):
  #windchill = quantify(temperatures[i], speeds[i])
  #print(temperatures[i], speeds[i], windchill)

#wct_index = zip(temperatures, speeds)
#wct_index_list = list(wct_index)
#print(wct_index_list)

