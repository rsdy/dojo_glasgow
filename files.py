import sys
import random

out_arr = []
for fname in sys.argv[1:]:
    with open(fname) as f:
        out_arr.append(list(set(f.read().split())))

word_length = len(min(out_arr, key=lambda x: len(x)))
#for a in out_arr:
    #random.shuffle(a)

print ' '.join(word for words in out_arr for word in words[:word_length])
