import sys

args = (sys.argv[1:])
args = sys.argv[1:]
# more the one arg
if(len(args) == 0):
  print("")
  exit()

if(len(args) > 1):
  print("AssertionError: more than one argument is provided")
  exit()

# Check if is number
for n in args[0]:
  if (n < '0' or n > '9'):
    print("AssertionError: argument is not integer")
    exit()

# check if integer
nbr = int(args[0])
if (isinstance(nbr, int) == False):
  print("AssertionError: argument is not integer")
  exit()

# Check odd or even or 0
if(nbr == 0):
  print("I’m Zero.")
  exit()

if(nbr%2 == 0):
  print("I’m Even.")
else:
  print("I’m Odd.")
