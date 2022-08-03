# The goal of this program is to practice Python constructs

def getNumber():

   symbols = input("Enter a digit: ")

   number = int(symbols)

   return number


def sumTwo(a,b):

   c = a + b

   return c


def sumDigits(x):

  return sum([int(i) for i in str(x)])


x = sumTwo(3,5)

print(x) 