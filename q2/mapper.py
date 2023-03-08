"""mapper.py"""

import sys
# Open the file for reading
# with open('newinput.txt', 'r') as f:
#     # Read the entire file contents
#     input_str = f.read()

# # Print the input string
# print(input_str)

# input_str = [["A", 2, 1, 1, 1],
# ["A" ,2 ,1, 2, 2],
# ["A" ,2 ,2 ,1 ,3],
# ["A" ,2 ,2 ,2 ,4],
# ["B" ,2 ,1 ,1 ,5],
# ["B", 2, 1, 2, 6],
# ["B" ,2 ,2 ,1, 7],
# ["B" ,2, 2 ,2 ,8]]

for line in sys.stdin:
   
    line = line.strip()
    words = line.split()
    # print(line)
    matrix_name = words[0]
    if(matrix_name == 'A'):

        # (i, k), (A, j, Aij)) for all k 
        k_temp = int(words[1])
        for k in range (1, k_temp + 1):
            print('({},{})\t(A,{},{},{},{})'.format(words[2], k, words[3], words[4], words[5], words[6]))

    else:
        # (i, k), (B, j, Bjk)) for all i 
        k_temp = int(words[1])
        for k in range (1, k_temp + 1):
            print('({},{})\t(B,{},{},{},{})'.format( k, words[3], words[2], words[4] ,words[5], words[6]))
    



# for line in input_str:
   
#     # line = line.strip()
#     # words = line.split()
#     # print(line)
#     matrix_name = line[0]
#     if(matrix_name == 'A'):

#         # (i, k), (A, j, Aij)) for all k 
#         k_temp = line[1]
#         for k in range (1, k_temp + 1):
#             print('({},{})\t(A,{},{})'.format(line[2], k, line[3], line[4]))

#     else:
#         # (i, k), (B, j, Bjk)) for all i 
#         k_temp = line[1]
#         for k in range (1, k_temp + 1):
#             print('({},{})\t(B,{},{})'.format( k, line[3], line[2], line[4]))
    











# (1,1), (A,1,1)









# ((1, 1), (A, 1, 1)) 
#           j=2   ((1, 1), (A, 2, 2))   (1,1), (A,2,2)
#      i=2  j=1   ((2, 1), (A, 1, 3))    (2,1), (A,1,3)
#           j=2   ((2, 1), (A, 2, 4))     (2,1), (A,2,4)

# k=2  i=1  j=1   ((1, 2), (A, 1, 1))        (1,2), (A,1,1)
#           j=2   ((1, 2), (A, 2, 2))   (1,2), (A,2,2)
#      i=2  j=1   ((2, 2), (A, 1, 3))    (2,2), (A,1,3)
#           j=2   ((2, 2), (A, 2, 4))    (2,2), (A,2,4)





# (1,1), (B,2,6)
# (1,2), (B,2,6)
# (2,1), (B,1,7)
# (2,2), (B,1,7)
# (2,1), (B,2,8)
# (2,2), (B,2,8)


# ((1, 1), (B, 1, 5))    (1,1), (B,1,5)
#   ((1, 2), (B, 1, 6))   
#   ((1, 1), (B, 2, 7))
#    ((1, 2), (B, 2, 8)) 

#    ((2, 1), (B, 1, 5))   (1,2), (B,1,5)
#    ((2, 2), (B, 1, 6))   
#   ((2, 1), (B, 2, 7))
#   ((2, 2), (B, 2, 8)) 

# (1,1), (B,1,5)
# (2,1), (B,1,5)
# (1,2), (B,1,6)
# (2,2), (B,1,6)
# (1,1), (B,2,7)
# (2,1), (B,2,7)
# (1,2), (B,2,8)
# (2,2), (B,2,8)