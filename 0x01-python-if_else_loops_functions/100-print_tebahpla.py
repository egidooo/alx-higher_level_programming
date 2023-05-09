#!/usr/bin/python3
# 100-print_tebahpla.py

k = 0
for p in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(p - k)), end="")
    k = 32 if k == 0 else 0
