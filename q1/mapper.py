"""mapper.py"""

import sys

for line in sys.stdin:
   
    line = line.strip()
    words = line.split()
    # print(words)
    # words = map(eval, words)
    # for each in words:
    #     print(type(each))
    print('({})\t({},{},{},{})'.format(words[2],words[0], words[3], words[4], words[5]))


  
