def getmeters(rods):
  meters = 5.0292 * rods
  return meters

def getfurlongs(rods):
  furlongs = rods / 40
  return furlongs

def getmiles(rods):
  miles = getmeters(rods) / 1609.34
  return miles

def getfeet(rods):
  feet = getmeters(rods) / 0.3048
  return feet

def gettime(rods):
  speed = 3.1
  time = (getmiles(rods) / speed) * 60
  return time

def run():
  rods = float(input("Input rods: "))
  print(f"Your Input: {rods}")
  print("")
  print("Conversions")
  print(f" Meters:{getmeters(rods)}")
  print(f" Feet:{getfeet(rods)}")
  print(f" Miles:{getmiles(rods)}")
  print(f" Feet:{getfeet(rods)}")
  print(f" Time:{gettime(rods)}")

run()