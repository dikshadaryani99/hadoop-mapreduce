"""reducer.py"""

from operator import itemgetter
import sys
import ast

# input_str = [{(1,1):   [("A",1,1), ("B",1,5), ("A",2,2), ("B",2,7)]},
# {(1,2) :  [("A",1,1), ("A",2,2), ("B",1,6), ("B",2,8)]},


# {(2,1)   :[("A",1,3),("A",2,4) ,("B",1,5) ,("B",2,7)]},
# {(2,2) :  [("A",1,3),("A",2,4) ,("B",1,6) ,("B",2,8)]}]

# input comes from STDIN
rows_final = 0
cols_final = 0
myset = set()
dic = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t')
    # print (type(key))
    # print (value[7])
    # print(type(value[9]))
    # print(value[9])

    


    key = tuple(map(eval, key.strip('()').split(',')))
    value = tuple(value.strip('()').split(','))
    rows_final = int(value[3])
    cols_final = int(value[4])
    # print(value[0])
    # print (type(key))
    # print (type(value))
    if key in myset:
        dic[key].append(value)
    else:
        myset.add(key)
        dic[key] = [value]

# print(dic)

matrix = [[column for column in range(cols_final)] for row in range(rows_final)]
for value in dic:
    lista = []
    listb = []
    # print(value[0])
    # print(value[1])
    # print(dic[value])
    for each in dic[value]:
        # print(each)
        if(each[0] == 'A'):
            lista.append(each)
        else:
            listb.append(each)
        
    sorted_lista = sorted(lista, key=lambda x: x[1])
    sorted_listb = sorted(listb, key=lambda x: x[1])
    # print(sorted_lista)
    # print(sorted_listb)
    sum  = 0
    for i in range (len(sorted_lista)):
        sum += (int(sorted_lista[i][2]) * int(sorted_listb[i][2]))
    matrix[value[0] - 1][value[1] - 1] = sum
    # print('({},{})\t{}'.format( value[0], value[1], sum))

    
for row in range(rows_final):
    for column in range(cols_final):
        print(matrix[row][column], end=" ")
    print()




# for line in input_str:
#     # print(line)
#     key = list(line.keys())[0]
#     print(key)
#     values = line[key]
#     lista = []
#     listb = []
#     for each in values:
        
#         if(each[0] == 'A'):
#             lista.append(each)
#         else:
#             listb.append(each)
        
#     sorted_lista = sorted(lista, key=lambda x: x[1])
#     sorted_listb = sorted(listb, key=lambda x: x[1])
#     sum  = 0
#     for i in range (len(sorted_lista)):
#         sum += (sorted_lista[i][2] * sorted_listb[i][2])
#     print('({},{})\t{}'.format( key[0], key[1], sum))
