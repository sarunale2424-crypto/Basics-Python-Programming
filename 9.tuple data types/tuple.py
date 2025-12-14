#tuple
# group of values enclosed within ()
# t1 = (1,2,3,4)
# print(type(t1))
# print(t1)

#insertion order is preserved

#duplicates values are also allowed
# t2 = (1,2,3,4,1,2,3)
# print(t2)

#heterogenous(mixed) values are also allowed in tuples
# t3 = (10,3.14,True,"hello",10+12j)
# print(t3)

#tuples are immutable(unchangeable)
# t4 = (1,2,3,4)
# t4[0] = 10 #not allowed

# print(t4)

# t5 = (1,2,3,[4,5,6])

# # t5[3] = (40,50,60) # not allowed
# # print(t5)

# t5[3][0] = 40
# t5[3][1] = 50
# t5[3][2] = 60

# t5[3].append(70)

# print(t5)

#creating single valued tuple:

# t6 = (10,)
# print(t6)
# print(type(t6))


#traversing(accessing) values of typles

# t6 = (1,2,3,4,5)

# for value in t6:
#     print(value)


#multiplication operation in tuple

# t7 = (1,2,3)

# t8 =t7 *2

# print(t8)

#addition operation in tuples

# t9 = (1,2,3)
# t10 =(4,5,6)

# t11 = t9 + t10
# print(t11)

#indexing and slicing are applicable

t12 = (1,2,3,4) # left to right : starts from 0 and ends at len(tuple)-1
#right to left: starts from -1 and ends with len(tuple)
# print(t12[0])
# print(t12[3])


# print(t12[-1])

#slicing: part of tuple:
#left to right : starts from 0 to len(tuple)-1
#right to left: starts from -1 to len(tuple)+1
# print(t12[0: 3]) #1,2, 3
# print(t12[-1:-4:-1]) #4,3,2
print(t12[-1:-len(t12)-1:-1]) #4,3,2,1
print(t12[::-1])