# -*- coding: utf-8 -*-
"""data types.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IFqGYlfLtRR4sXaJ90VosFI3RqI3CJu4
"""

my_list = [1,2,3,4]
print(my_list)
#Add
my_list.append(5)
print(my_list)
#Remove
my_list.remove(4)
print(my_list)
#Modify
my_list[3]=10
print(my_list)

my_dict ={'Name' : 'Niya', 'Age' : '30', 'Place':'Goa'}
print(my_dict)
#Add
my_dict['Job'] = 'Doctor'
print(my_dict)
#Remove
del my_dict['Place']
print(my_dict)
#Modify
my_dict['Age'] = '45'
print(my_dict)

my_set = {1,2,3,4,5,6}
print(my_set)
#Add
my_set.add(7)
print(my_set)
#Remove
my_set.remove(3)
print(my_set)
#Modify
my_set.discard(1)
my_set.add(10)
print(my_set)