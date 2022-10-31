#Challenge 7
natural_palindromes = []
non_lychrel_numbers = []
lychrel_numbers = []

def check_palindrome(number): 
  if str(number) == str(number)[::-1]:
    return True
  else:
    return False

def add_reverse(number):
  return number + int(str(number)[::-1])

def check_lychrel(number):
  counter = 0
  while counter < 60:
    if check_palindrome(number):
      return True
    else:
      counter += 1
      number = add_reverse(number)
  return False

def main():
  integer_1 = int(input('Integer 1: '))
  integer_2= int(input('Integer 2: '))
  for i in range(integer_1, integer_2+1):
    if check_palindrome(i):
      natural_palindromes.append(i)
    else:
      if check_lychrel(add_reverse(i)):
        non_lychrel_numbers.append(i)
      else:
        lychrel_numbers.append(i)
        print(f'{i} is probably lychrel')
  print(f'Palindrome numbers = {len(natural_palindromes)}')
  print(f'Not Lychrel numbers = {len(non_lychrel_numbers)}')
  print(f'Lychrel = {len(lychrel_numbers)}')

if __name__ == '__main__':
  main()