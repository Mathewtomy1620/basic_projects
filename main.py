# //// 1.Check a given number is a perfect number or not //////
# num = int(input("Enter the number: "))
# a = 0
# for i in range(1, num):
#     if num % i == 0:
#         a += i
# if a == num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")

# ////// 2.Print the pattern //////////
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# row = int(input("Enter the number of rows: "))
# for i in range(1, row+1):
#     print(" " * i, end="")
#     print("* " * (row+1 - i))

# ///// 3.Print the pattern
# A
# B B
# C C C
# D D D D
# E E E E E
# my_lst = ['A', 'B', 'C', 'D', 'E']
# for i in range(0, len(my_lst)):
#     print((my_lst[i] + " ") * (i+1))

# //// 4.Print only even length words in a given string
# 4. Method 1
# my_lst = input("Enter your string: ").split(" ")
# for i in my_lst:
#     count = 0
#     for k in i:
#         count += 1
#     if count % 2 == 0:
#         print(i)

# 4. Method 2
# my_list = input("Enter your string: ").split(" ")
# for i in my_list:
#     if len(i) % 2 == 0:
#         print(i)
#     else:
#         pass

# ///// 5.Find words which are greater than given length /////
# my_lst = input("Enter the string: ").split(" ")
# len_limit = int(input("Enter the limit of characters in a word: "))
# print("Words which are greater than limit ", len_limit, "are: ")
# for i in my_lst:
#     if len(i) > len_limit:
#         print(i)


# //// 6.Check a string is symmetrical /////
# my_string = input("Enter your string: ")
# mid = 0
#
# if len(my_string) % 2 == 0:
#     mid = len(my_string) // 2
# else:
#     mid = len(my_string) // 2 + 1
# print(my_string[0:mid])
# print(my_string[mid:])
#
# if my_string[mid:] in my_string[0:mid]:
#     print(my_string, "is symmetrical")
# else:
#     print(my_string, "is not symmetrical")


# //// 7.Removes the characters at even indices of a string///
# Method 1
# my_string = input("Enter your string: ")
# print(my_string[0::2], end=" ")

# Method 2
# my_string = input("Enter your string: ")
# for i in range(0, len(my_string), 2):
#     print(my_string[i], end="")

# ///// 8.Count the number of words in a string//////
# Method 1 --> By converting a string into list and by iterating through the list
# my_list = input("Enter your string: ").split()
# count = 0
# for i in my_list:
#     count += 1
# print(f'There are {count} words in the string')

# Method 2 --> By counting the number of spaces in a string and by adding it with 1
# my_string = input("Enter your string: ")
# print(f'Number of words in the string  = {my_string.count(" ")+1}')

# //// 9.Check a given year is leap year or not/////
# year = int(input("Enter year the year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("The year is a leap year")
#
# else:
#     print("The year is not a leap year")

# ///// 10.Multiply all the numbers in a list/////
# my_list = ['Mathew', 22, 'Jhon', 78, 'paul', 45, 'Joseph', 56, 'Kevin', 12, 'Thomas', 52]
# num_list = []
# mul_factor = int(input("Enter the multiplication factor: "))
# new_list = []
# for i in my_list:  # To remove strings from the list
#     if not isinstance(i,str):
#         num_list.append(i)
# print(num_list)
# for i in num_list: # To multiply the number list with a factor
#     new_list.append(i*mul_factor)
# print(new_list)

# //// 11.Sort elements in a list without using the built-in function sort()
# Method 1 --> By appending all minimum elements in successful iteration
# 1 --> By using while loop
# my_list = [14, 8, 79, 45, 63, 52, 1, 98]
# sort_list = []
# while my_list:
#     minimum = my_list[0]
#     for i in my_list:
#         if i < minimum:
#             minimum = i
#     sort_list.append(minimum)
#     my_list.remove(minimum)
# print(sort_list)

# 2 --> By using for loop only
# for i in range(1, len(my_list) + 1):
#     minimum = my_list[0]
#     for j in my_list:
#         if j < minimum:
#             minimum = j
#     sort_list.append(minimum)
#     my_list.remove(minimum)
# print(sort_list)

# 3 --> By using while loop and min function
# my_list = [14, 8, 79, 45, 63, 52, 1, 98]
# min_list = []
# while my_list:
#     minimum = min(my_list)
#     min_list.append(minimum)
#     my_list.remove(minimum)
# print(min_list)

# Method 2 --> By comparing two adjacent index elements
# my_list = [14, 8, 79, 45, 63, 52, 1, 98]
# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i]
# print(my_list)

# ///// 12.Count the numbers in a list which is greater than a given number //////
# my_list = [10, 42, 5, 8, 23, 15, 14, 1, 0]
# new_list = []
# num = int(input("Enter your number limit: "))
# for i in my_list:
#     if i > num:
#         new_list.append(i)
# print(new_list)
# print(f'Number of elements greater than number {num} = {len(new_list)}')

# /// 13.Count the number of lower case and upper case characters in a list
# my_string = input("Enter your desired string: ")
# upper_lst = []
# lower_lst = []
# for i in my_string:
#     if i.isupper():
#         upper_lst.append(i)
#     elif i.islower():
#         lower_lst.append(i)
#     else:
#         pass
# print("Number of upper case elements in the string: ", len(upper_lst))
# print("Number of lower case elements in the string: ", len(lower_lst))

# //// 14. Let farm = {1:'Eeman', 2:'Catrine', 3:'David'} be a dictionary.
# farm = {
#     1: "Eeman",
#     2: 'Catrine',
#     3: 'David'
# }
# 14.a Add key value pair (8:'Jack').
# Method 1
# farm[8] = 'Jack'
# print(farm)

# Method 2
# lst = {8: 'Jack'}
# farm.update(lst)
# print(farm)

# 14.b Display the number of items in the dict
# print(f'Values in the dict: {farm.items()}')
# print("Number of items in the dict: ", len(farm))

# 14.c To remove the key value pair (2:'Catrine')
# farm.pop(2)
# print(farm)

# 15. Create a tuple from an existing tuple. New tuple contains only the elements divisible by 3
# my_tuple = (11, 45, 60, 15, 42, 10, 33, 17, 21, 24)
# my_lst = []
# for i in my_tuple:
#     if i % 3 == 0:
#         my_lst.append(i)
# new_tuple = tuple(my_lst)
# print(new_tuple)
