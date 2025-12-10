#Identifier: Name of variable, function, class, module,
#for identification purpose.
# x = 20 # x is an identifier of variable
# def func(): # func is an identifer of function
#     pass
# class Test: # Test is an identifier of class 
#     pass

#Rules for defining Identifiers in Python:
#1.allowed characters: a-z, A-Z . 0-9, _
# name = "Rabin" #identifier
# _age = 23 #identifier
# address1 = "Pokhara" # address1 is an identifier
#2. Identifier should not starts with digits(0-9) but starts with letter(a-z,A-Z, _)
# 1email  ="test@test.com" #Wrong identifier
#3.Python is case sensitive programming language:
# sum = 100 #sum is an identifeir
# SUM  = 300 # SUM is an identifier 
#4.keyword or reserved word can't be used an identifier: 
# if = 678 # if is a keyword, so if can't be used as identifer
# def  = "hello" #def is a keyword , so it can not be used as identifier
#5.length limit of identifier: no limit but not recommeded to use lengthy identifier.

# hello0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000= 123 # not recommeded.
# hello = 123


# 20address = "" #ivalid
# sum12 = 100 #valid
# ca$h = 400 #invalid
# _name = "Rohit" #valid
# def  = 567 #invlid

# for  = "hu" #invlid 


# Note:

# if the identifier starts with single underscore (_) then it is treated as private 
# _age ==> private
#if the identifier starts with two underscore then it is treated as strongly private or protected
# __name ==> strongly private

#if the identifier start with __(double underscore) and ends with __(double underscore), then it is treated as dunder/special identifier
# __name_ ==> dunder variable
# __init__() ==> dunder method
