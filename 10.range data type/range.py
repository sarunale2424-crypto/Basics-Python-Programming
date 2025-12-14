#range:
#represents sequence of values(integer)

# 1,2,3,4,5,...
# 1,3,5,7,9,11,...
# 1,4,7,10,...

#range() function
#1.range(n)
#it generates sequence of values from 0 to n-1

# r1 = range(10) # 0,1,2,3,4,5,6,7,8,9
# print(type(r1))
# print(r1)
# for v in r1:
#     print(v,end=",")

# #range is immutable

# # r1[1] = 100 #not allowed
# # slicing
# print(r1[0:5])
# for value in r1[:5]:
#     print(value)

# print(r1[1])
#2.range(start,end) 
#it generate numbers from start to end-1


# r2 = range(1,10) # 1,2,3,4,5,6,7,8,9
# # for value in r2:
# #     print(value,end=",")

# print(r2[8])

#3.range(start,end,step)
#it generates numbers(integer numbers) from start to end-1 with increment/decrement of step

# r3 = range(1,100,2) # 1,3,5,7,9,11,13,,,......,99
# for value in r3:
#     print(value,end=",")

# r4 = range(10,50,5)
# for value in r4:
#     print(value,end=",")

# r5 = range(50,1,-5)
# for value in r5:
#     print(value,end=",")

# r6 = range(100,1000,1.5)
# print(type(r6))





# dasdsa