x=1
a=float(x)

import random
print(random.randrange(1,10))

my_list=[1, 2, 3, 4, 5]  #for loop
for item in my_list:
   print(item)

my_string = "Python"   #for loop in string
for char in my_string:
    print(char)

for i in range(5):    #iteration using range
    print(i)  

my_dict = {"a": 1, "b": 2, "c": 3}   #for loop in dictionary
for key in my_dict:
    print(key)    
 
for i in range(3):   #nested for loop
    for j in range(2):
        print(f"({i}, {j})")

for i in range(5):
    if i==10:
        break
    print(i)
else:
    print("loop finished without breaking")        


x = [5, 6, 7, 8, 9]     # using list comprehension
res = [val**2 for val in x]
print(res)    


x = 1
a = float(x)
print(type(a))

a="jahnavi"
print(len(a))

txt="i am 20 years old"
print("am"in txt)

a=("python")
print(a[-5:-2])

a=("python")
print(a.upper())
a=("python")
print(a.lower())


a = ("       india is a country      ")
print(a.strip())

a = ("india is a country")
print(a.replace("n","m"))

a = "india is a country"
print(a.split(","))

a = "india is a country "
b = "it is amazing"
print(a + b)


price = 100
str = f"the price of the bat is {price}"
print(str)


a = "india is a country"
print(a.capitalize())

a = "india is a country"
print(a.count(a))

a = "india is a country"
x = a.rpartition("country")
print(x)

a = ("       india is a country      ")
print(a.rstrip())

a = ("india is a country")
print(a.title())

a = 200
print(isinstance(a, int))

list = ["apple", "banana", "cherry"]
print(len(list))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list = ["apple", "banana", "cherry"]
list[1] = "blackberry"
print(list)

list = ["apple", "banana", "cherry"]
list.insert(2, "blackberry")
print(list)

list = ["apple", "banana", "cherry"]
list.append("blackberry")
print(list)

list = ["apple", "banana", "cherry"]
fruit = ["mango", "pineapple", "papaya"]
list.extend(fruit)
print(list)

list = ["apple", "banana", "cherry"]
list.remove("cherry")
print(list)

list = ["apple", "banana", "cherry"]
list.pop(2)
print(list)

list = ["apple", "banana", "cherry"]
list.clear()
print(list)

list = ["apple", "banana", "cherry"]
for x in list:
   print(x)

list = ["apple", "banana", "cherry"]
for i in range(len(list)):
  print(list[i])

  list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
  print(list[i])
  i = i + 1

list = ["apple", "banana", "cherry"]
[print(x) for x in list]

list = ["apple", "banana", "cherry", "kiwi", "mango"]
list2 = [x for x in list if "a" in x]
print(list2)


list = ["apple", "banana", "cherry", "kiwi", "mango"]
list.sort()
print(list)

list = ["apple", "banana", "cherry", "kiwi", "mango"]
list.sort(reverse=True)
print(list)

list = ["apple", "banana", "cherry", "kiwi", "mango"]
list.reverse()
print(list)

tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple)

tuple = ("apple",)
print(type(tuple))




fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

tuple=("apple", "banana", "cherry")
i=0
while i<len(tuple):
  print(tuple[i])
  i=i+1


  set1 = {"X", "Y", "Z"}
set2 = {10, 21, 33}

set3 = set1.union(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)  # CAN ALSO USE &
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)  # CAN ALSO USE - 
print(set3)


dict={"name":"jahnavi", "age:":20}
print(dict["name"])

dict={"name":"jahnavi", "age:":20}
print(dict["name"])
