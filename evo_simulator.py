from random import randint
import sys

def simulate(n):
  lst = [0] * n
  lst[0] = 1
  recieved = []
  recieved.append(0)
  while len(recieved) > 0:
    next_recieved = []
    for ind in recieved:
      to_send = [randint(0, len(lst)-1) for _ in range(0, 4)]
      for package in to_send:
        if lst[package] == 1:
          pass
        else:
          lst[package] = 1
          next_recieved.append(package)
    recieved = next_recieved
  return (sum(lst) / n) * 100


def my_algorithm(n):
  lst = [0] * n
  lst[0] = 1
  recieved = []
  recieved.append(0)
  while len(recieved) > 0:
    next_recieved = []
    for ind in recieved:
      to_send = [(recieved[0] + 1) % len(lst)]
      for package in to_send:
        if lst[package] == 1:
          pass
        else:
          lst[package] = 1
          next_recieved.append(package)
    recieved = next_recieved
  return (sum(lst) / n) * 100





args = sys.argv[1:]
n, i = 0, 0
if args[0] == '-n':
  n = int(args[1])
if args[2] == '-n':
  n = int(args[3])

if args[0] == '-i':
  i = int(args[1])
if args[2] == '-i':
  i = int(args[3])

if len(args) > 4 and args[4] == "--my-algorithm":
  s = 0
  for _ in range(i):
    s += my_algorithm(n)
  s /= i
  print("In " + str(s) + "%% cases all nodes recieved the packet")
else:
  s = 0
  for _ in range(i):
    s += simulate(n)
  s /= i
  print("In " + str(s) + "%% cases all nodes recieved the packet")

#print(sys.argv)