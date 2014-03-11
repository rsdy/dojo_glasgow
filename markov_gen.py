from pymarkov import markov
import sys


with open(sys.argv[1]) as file_in:
    aye = file_in.read()
    m_dict = markov.train([aye], 2)
no_of_ideas =  int(sys.argv[2]) + 1
ideas = [markov.generate(m_dict, 4, 2) for i in range(1, no_of_ideas)]

for i in ideas:
    print(i)
