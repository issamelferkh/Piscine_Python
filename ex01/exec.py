import sys

args = (sys.argv[1:])
args_str = ""
for arg in args:
  args_str = args_str + " " + arg
trim = args_str.strip()
rev = trim[::-1]
final = rev.swapcase()
print(final)

