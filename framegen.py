import sys
from random import randint

messages = [
    "hello",
    "hawaii",
    "aloha",
    "tehran",
    "iran",
    "whatsup?"
    "good",
    "byebye",
    "bonjour",
    "salam",
    "ok",
    "over",
    "missile"
]

MIN_NUMBER = 0
MAX_NUMBER = 1000 #ms

def randNumber(mi, ma):
    return randint(mi, ma)

node, count = 0, 0
try:
    node, count, a = [float(x) for x in sys.argv[1:]]
    MAX_NUMBER *= a
except:
    node, count = [float(x) for x in sys.argv[1:]]

for i in range(int(count)):
    n = randNumber(0, int(node) - 1)
    m = randNumber(0, len(messages) - 1)
    m = messages[m]
    t = randNumber(0, MAX_NUMBER)
    print(n, m, t)

print("END")