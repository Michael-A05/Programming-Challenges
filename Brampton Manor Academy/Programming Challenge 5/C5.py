#Challenge 5

def calculation(slayer):
  slayer_str = str(slayer)
  layers = int(slayer_str[1:] + slayer_str[0])
  if (3*slayer) == layers:
    return True
  else:
    return False

def introduction():
   print("Guess a six-digit number SLAYER \
so that the following equation is true, \
where each letter stands for the digit \
in the position shown: \
SLAYER + SLAYER + SLAYER = LAYERS")

def run(): 
  slayer = int(input("Enter your guess for SLAYER: "))
  if calculation(slayer):
    print("Your guess is correct:")
    print(f"SLAYER + SLAYER + SLAYER = {3*slayer}")
    print(f"LAYERS = {((str(slayer))[1:])+((str(slayer))[0])}")
    print("Thanks for playing.")
  else:
    print("Your guess is incorrect:")
    print(f"SLAYER + SLAYER + SLAYER = {3*slayer}")
    print(f"LAYERS = {((str(slayer))[1:])+((str(slayer))[0])}")
    print("Thanks for playing.")
    print("\n")
    return run()

if __name__ == '__main__':
  introduction()
  run()