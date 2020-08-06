#!/usr/bin/env python3
import argparse
import sys
from collections import deque
from itertools import islice

parser = argparse.ArgumentParser(description='head and tail a file')
parser.add_argument('file', type=argparse.FileType('rt', encoding='UTF-8'))
parser.add_argument('-s','--start', type=int, default=3)
parser.add_argument('-e','--end', type=int, default=3)
args = parser.parse_args()

print ("".join(islice(args.file,0,args.start)),end="")
print ("".join(deque(args.file, args.end)))