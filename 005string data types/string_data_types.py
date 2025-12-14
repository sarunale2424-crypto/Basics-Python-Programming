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


# num1 = 450

# num2String  = "500"

# sum = num1 + int(num2String)
# print("The sum is ",sum)

#float()
# print(float(50)) #50.0
# print(float(10+20j)) # Error occurred
# print(float(True)) #1.0
# print(float(False)) #0.0
# print(float("hello")) # error occured : ValueError
# print(float("20")) #20.0
# print(float("3.14")) #3.14

#complex: convert other type to complex type
#form1: complex(a) => a+0j
#form2:complex(a,b) => a+bj

#form1:complex(a) => a+0j
# print(complex(4)) # 4+0j
# print(complex(23.5)) # 23.5+0j
# print(complex(True)) #1+0j
# print(complex(False)) #0+0j = 0j
# print(complex("30"))  #30+0j
# print(complex("10.5")) # 10.5 + 0j
# print(complex("five")) # error occured : ValueError

#form2:complex(a,b) => a+bj
# print(complex(2,3)) # 2+3j
# print(complex(1.5,2.4)) # 1.5+2.4j
# print(complex(True,True)) #1+1j
# print(complex("100","200")) #error occurred
# print(complex(10,"20")) #error occurred
# print(complex("10",20)) #error
# print(complex(10,24.5)) # 10+24.5j

#bool()
#for int argument => 0: False, Non 0 :True

# print(bool(5))
#for float argument=> 0: False,Non 0: True
# print(bool(0.0))
# print(bool(3.4))
# print(bool(-13.4))

#str argument :> empty string : False , not empty : True

# print(bool(""))
# print(bool("abc"))
# print(bool(" "))

#for complex argument=> real,imag both 0 : False,Non 0 => True

# print(bool(10+20j))
# print(bool(0+0j))





 
