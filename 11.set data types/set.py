#set
#group of values within the {}
# s1 = {1,2,3,4,5,6}
# print(s1)
# print(type(s1))
#insertion order is not preserved

#indexing and slicing are not applicable
# print(s1[0]) #not allowed
# print(s1[0:2]) # not allowed

#duplicates values are removed even though we are insering them
# s2 = {1,2,3,4,1,2}

# print(s2)

#heterogenous values are allowed

# s3 ={10,3.14,True,"hello",5+7j}
# print(s3)

#sets are mutable(growable nature)

s4 = {1,2,3}
s4.add(0.4)
s4.add(10.5)

print(s4)

s4.remove(2)

print(s4)
# s4.remove(7)
print(s4)

is_available = 7 in s4 
if is_available:
    s4.remove(7)
print(s4)

#  git push -u origin main



