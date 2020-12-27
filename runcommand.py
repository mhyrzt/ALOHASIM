#!/usr/bin/python3.8
from consts import NODE_NUMBERS
import os

PACKET_COUNT = 100
TIME_SCALE   = 25

COMMAND = "python3 framegen.py {NODE_COUNT} {PACKET_COUNT} {TIME_SCALE} | python3 main.py"
COMMAND = COMMAND.format(
    NODE_COUNT   = len(NODE_NUMBERS),
    PACKET_COUNT = PACKET_COUNT,
    TIME_SCALE   = TIME_SCALE
)
print(COMMAND)
os.system(COMMAND)