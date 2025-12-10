#String: any sequence of characters enclosed within single or double quotes
# s = "Learning Python is fun"
# s1 = 'Python is very easy to learn and understand' #string literal
# s2 = """
# Python is High level general purpose programming language
# Learning Python is very fun
# """

# s3 = '''
# Python is High level general purpose programming language
# Learning Python is very  very fun
# '''

# print(s)
# print(s1)
# print(s2)
# print(s3)


# st1 = 'Learning "Python" is fun'
# print(st1)

#indexing
# sentence = "I love to programming so much."

# # print(sentence[-1])
# print(sentence[-2])

#slicingh

# s4 = "Kathmandu" #s4[begin: end: step]
# print(s4[1:3]) # at
# print(s4[4:7]) #man
# print(s4[:7]) #Kathman
# print(s4[1:]) #athmandu
# print(s4[:]) #Kathmandu

# print(s4[-1:-4:-1]) #""
# print(s4[-4:-1]) #and
# print(s4[-6:-2]) #hman
# print(s4[1:100]) #athmandu #no error in slicing

# print(s4[100])  #error: string index out of range : error occured in indexing
#len() function : to count number of character present in given string literal

# print(len(s4)) #9 
#slicing
# string[begin: end: step] # step : 1 default

# s5  = "Mount Everest"
# print(s5[1:6:2]) #on 
# print(s5[2: 9: 3]) #u e

# Type casting: type coersion(conversion)
# functions
# int() , float(), complex(), bool(), str()
#1.int(): to convert any other type value to int if possible
# print(int(123.45)) #123
# print(int(12+4j)) # impossible to convert
# print(int(True)) #1
# print(int(False)) #0

# print(int("ten")) #Impossible to convert
# print(int("123")) #possible to convert
# print(type(int("123"))) #possible to convert
# print(int("123.35")) #Error: ValueError Old 
# print(int("123abc")) #Impossible to convert

# print(int("123.35")) #Error occured: ValueError


num1 = 450

num2String  = "500"

sum = num1 + int(num2String)
print("The sum is ",sum)



 
