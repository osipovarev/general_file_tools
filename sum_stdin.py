#!/usr/bin/env python3
import sys
res = 0
stdin_all = sys.stdin.read()
# print(stdin_all)
for elem in stdin_all.split("\n"):
    numer = int(elem) if len(elem) > 0 else 0
    res += numer
print(res)
        
