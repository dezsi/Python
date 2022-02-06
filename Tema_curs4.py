# 2.1)
# def sum(n):
#     sum=int(n*(n+1)/2)
#     line=""
#     for a in range(1,n):
#         line=line+str(a)+"+"
#     line=line+str(n)+"="+str(sum)
#     print(line)

# num = #enter input
# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)

#2.2)

# n = int(input())
# sum = 0
# for i in range(0, n):
# 	if(i % 2 == 0):
# 		sum += i
# print(sum)

# value = int(input("Please enter the value: "))
# total = 0
#
# for num in range(1, value+1):
#     if(num % 2 == 0):
#         print("{0}".format(num))
#         total = total + num
#
# print("The Sum of Even Numbers from 1 to {0} = {1}".format(num, total))

#2.3)

# n = int(input("Enter the end number : "))
# oddsum = 0
# for i in range(1, n+1):
#   if i % 2 != 0:
#     oddsum += i
# print(oddsum)

#3.)

# x = int(input())
# if x > 0:
#     print(x)
# else:
#     print(0)


#1.1)

# number1 = input('Enter first number: ')
# number2 = input('Enter second number: ')
# number3 = input('Enter third number')
# sum = int(number1) + int(number2) + int(number3)
# print(sum)


#1.2)


# x = int(input())
# if x > 0:
#     print(0)
# else:
#     print(0)

#1.3

# number1 = input('Enter first number: ')
# number2 = input('Enter second number: ')
# sum = int(number1) + int(number2) + int(number3)
# print(sum)


# lst = []
# num = int(input("Enter the size of the array: "))
# print("Enter array elements: ")
# for n in range(num):
#   numbers = int(input())
#   lst.append(numbers)
# print("Sum:", sum(lst))