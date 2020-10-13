#Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(x):
    return x

n = 5
result = int_return(n)


#Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(x):
    y = x + 2
    return y

n = 2
result = add(n)


#Write a function called change that takes any string, adds “Nice to meet you!” to
#the end of the argument given, and returns that new string.

def change(x):
    y = x + "Nice to meet you!"
    return y

n = "hello"
result = change(n)


#Write a function, accum, that takes a list of integers as input and returns
#the sum of those integers.

def accum(x):
    num = 0
    for ch in x:
        num = num + ch
    return num

lst = [1, 2, 3, 4]
result = accum(lst)


#Write a function, length, that takes in a list as the input. If the length of the
#list is greater than or equal to 5, return “Longer than 5”. If the length is less
#than 5, return “Less than 5”.

def length(x):
    for ch in x:
        if len(x) >= 5:
            return "Longer than 5"

    return "Less than 5"


lst = ["nj", "pa", "wc", "dc", "la"]
result = length(lst)


#You will need to write two functions for this problem. The first function, divide
#that takes in any number and returns that same number divided by 2. The second
#function called sum should take any number, divide it by 2, and add 6. It should
#return this new number. You should call the divide function within the sum function.
#Do not worry about decimals.


def divide(n):
    y = n/ 2
    return y

def sum(x):
    num = divide(x) + 6
    return num
