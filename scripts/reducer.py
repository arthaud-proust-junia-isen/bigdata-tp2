#!/usr/bin/env python

import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    word, count = line.strip().split("\t")
    counts[word] += int(count)

for word, total in counts.items():
    print("{}\t{}".format(word, total))
