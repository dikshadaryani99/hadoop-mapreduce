"""reducer.py"""

from operator import itemgetter
import sys
import ast



# input comes from STDIN
myset = set()
dic = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t')
    # print (type(key))
    # print (type(value))
    key = key.strip('()')
    # key = tuple(map(eval, key.strip('()').split(',')))
    value = tuple(value.strip('()').split(','))
    # print (key)
    # print (value)
    tempvalue = value[:-1]
    
    tempvalue = tuple(map(eval, tempvalue))
    
    tempvalue = list(tempvalue)
    tempvalue.append(value[-1])
    tempvalue = tuple(tempvalue)
    # print(tempvalue)
    if key in myset:
        dic[key].append(tempvalue)
    else:
        myset.add(key)
        dic[key] = [tempvalue]

# print(dic)
# p = 0
newdict = {}
state_with_more_than_6per = 0
state_that_won_atleast_1_seat = 0
no_of_state_parties = 0
total_seats = 0

for value in dic:
    
    votes_mile = 0
    votes_dale = 0
    state_party = ''
    p = 0
    for each in dic[value]:
        # print(each)
        votes_mile += each[1]
        votes_dale += each[2]
        state_party = each[3]
        p =  each[0]
    # print(votes_dale)
    # print(votes_mile)
    # print(state_party)
    # print(p)
    # print()
    per = (votes_mile * 100) / votes_dale
    seats = per // p
    total_seats += seats
    if(per > 6):
        state_with_more_than_6per += 1

    if(state_party == "YES"):
        no_of_state_parties += 1
    
    if(seats > 0):
        state_that_won_atleast_1_seat += 1
    # print()
    # print()
    # print()
    
#     he party wins 3 seats from at least three different states.
# 2. At a general election, the party polls 6% of votes in any four or more states, and in addition, it
# wins four seats (in any state/s)
# 3. The party gets recognition as a state party in four states.

if(total_seats >= 3 and state_that_won_atleast_1_seat >= 3):

    print("YES")
elif(no_of_state_parties >= 4):
    print("YES")
elif(state_with_more_than_6per >= 4 and total_seats >= 4):
    print("YES")

else:
    print("NO")
   

    

