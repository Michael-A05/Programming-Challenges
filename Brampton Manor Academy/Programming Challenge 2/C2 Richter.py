richtervalues = [1.0, 5.0, 9.1, 9.2, 9.5]

def richtertojoules(richter):
  joules = 10 ** (1.5 * richter + 4.8)
  return joules

def joulestotnt(richter):
  tnt = 10 ** (1.5 * richter + 4.8) / 4.184 * 10 ** 9
  return tnt

for value in richtervalues:
  print(value)
  print(richtertojoules(value))
  print(joulestotnt(value))



def run():
  richter = float(input("Please enter a Richter Scale value: "))
  print(f"Richter value:{richter}")
  print(f"Equivalence in Joules:{richtertojoules(richter)}")
  print(f"Equivalence in tons of TNT:{joulestotnt(richter)}")

run()