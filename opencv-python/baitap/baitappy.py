#biến python
# nhiều giá trị đến nhiều biến
print("nhiều giá trị đến nhiều biến")
x1, y1, z1 = 'chao', 'cac', 'ban'
print(x1)
print(y1)
print(z1)

# một giá trị thành nhiều biến
print("\nmột giá trị thành nhiều biến")
x2 = y2 = z2 = 'chao cac ban'
print(x2)
print(y2)
print(z2)

#có một dánh sách và trích xuất nó
print("\ncó một dánh sách và trích xuất nó")
tapbien = ["chao", "cac", "ban"]
x3, y3, z3 = tapbien
print(x3)
print(y3)
print(z3)

#biến đầu rai
print("\nbiến đầu ra")
name = "Dang Ho Huu Phuc"
name1 = "dang"
name2 = "phuc"
name3 = name1 + name2
print("chao " + name)
print("chao " + name1 + name2)
print("chao " + name3 )

#biến toàn cục
print("\nbiến toàn cục")
bientoancuc = "bien toan cuc"
def hambientoancuc():
    print("Day la " + bientoancuc)
hambientoancuc()

#biến toàn cục sử dụng bên trong hàm
print("\nbiến toàn cục sử dụng bên trong hàm")
bien = "ben ngoai"
def hambientoancuc():
    bien = "ben trong"
    print("Day la " + bien)
hambientoancuc()
print(bien)

#global từ khóa toàn cầu
print("\nglobal từ khóa toàn cầu")
def hamglobal():
    global _global
    _global = "global toan cau"
hamglobal()
print("day la " + _global)

#global bên trong cùng tên với biến bên ngoài
print("\nglobal bên trong cùng tên với biến bên ngoài")
_global1 = "bien ben ngoai"
def hamglobal1():
    global _global1
    _global1 = "bien ben trong"
hamglobal1()
print("day la " + _global1)


#Dạng văn bản:	str
#Loại số:	int, float, complex
#Các loại trình tự:	list, tuple, range
#Loại ánh xạ:	dict
#Đặt các loại:	set, frozenset
#Loại Boolean:	bool
#Loại nhị phân:	bytes, bytearray, memoryview

#lấy loại dữ liệu
print("\nlấy loại dữ liệu")
layloaidulieu = 5
print(type(layloaidulieu))

#Số python
print("\nso python")
soint = 1
sofloat = 2.8
socomplex = 2j

print(type(soint))
print(type(sofloat))
print(type(socomplex))

#chuyen doi loai so
print("\n chuyen doi loai so")
soint_float = float(soint)
sofloat_int = int(sofloat)
soint_complex = complex(soint)
print(soint_float)
print(sofloat_int)
print(soint_complex)

print(type(soint_float))
print(type(sofloat_int))
print(type(soint_complex))

#so ngau nhien random
import random
print(random.randrange(1, 10))
print("\n")

#chi dinh gia tri cua 1 bien
chidinhx = int(2.5)
print(chidinhx)
chidinhy = float(2)
print(chidinhy)
chidinhz = complex(1)
print(chidinhz)
chidinha = str("chao1")
print(chidinha)

#String
#gan chuoi cho 1 bien
stringa = "day la chuoi a"
print("\n " + stringa)

#chuoi nhieu dong
stringnhieudong = """chao,
cac,
ban."""
print(stringnhieudong)

#chuoi mang
stringmang = "hello, phuc"
print("\n" + stringmang[1])

#vong qua 1 chuoi
stringvonglap = " string vong lap"
for i in stringvonglap:
    print(i)
print("\n")

#String length (len())
stringlength = "string length"
print(len(stringlength))
print("\n")

#Check String
check_string = "day la chuoi can phai kiem tra"
print("phuc" in check_string)
print("chuoioi" in check_string)
if "chuoi" in check_string:
    print("chuoi in check_string")
else:
    print("khong co")
print("\n")

#Slicing (chonj vi tri cua tu se xuat hien)
string_slicing = "chuoi can chon vi tri xuat hien cua chu"
print(string_slicing[2:9])
print(string_slicing[:9])
print(string_slicing[2:])
print(string_slicing[-2:-9])

#Upper Case
string_uppercase = "string upper case"
print(string_uppercase.upper())
#lower case
string_lowercase = "String Lower Case"
print(string_lowercase.lower())
#strip
string_remove_whitespace = " xoa khoang trang "
print(string_remove_whitespace.strip())
#Replace String
string_replace = "thay the chuoi"
print(string_replace.replace("the", "vao"))
#Split string
string_split = "split string"
print(string_split.split(" "))
#String concatenation
string_concatenation_1 = "noi chuoi"
string_concatenation_2 = "lai voi nhau"
string_concatenation_3 = string_concatenation_1 + string_concatenation_2
string_concatenation_4 = string_concatenation_1 + " " + string_concatenation_2
print(string_concatenation_3)
print(string_concatenation_4)

#String format dung ham format()
string_format_age = 15
string_format_school = "can tho"
string_format_tinh = "dong thap"
string_format_ten = "my name is phuc, I am {} year old"
string_format_ttsv = "phuc {} tuoi song o {} que o {}"
print(string_format_ten.format(string_format_age))
print(string_format_ttsv.format(string_format_age, string_format_school, string_format_tinh))

#Escape Characters
# \' Single Quote
# \\  Backslash
# \n  New Line
# \r  Carriage Return
# \t  Tab
# \b  Backspace
# \f  Form Feed
# \ooo    Octal value
# \xhh    Hex value

string_escape = "chu tich \"ho chi minh\" la chu tich nuoc"
print(string_escape)

#String Methods
#Method Description
# capitalize()    Converts the first character to upper case
# casefold()  Converts string into lower case
# center()    Returns a centered string
# count() Returns the number of times a specified value occurs in a string
# encode()    Returns an encoded version of the string
# endswith()  Returns true if the string ends with the specified value
# expandtabs()    Sets the tab size of the string
# find()  Searches the string for a specified value and returns the position of where it was found
# format()    Formats specified values in a string
# format_map()    Formats specified values in a string
# index() Searches the string for a specified value and returns the position of where it was found
# isalnum()   Returns True if all characters in the string are alphanumeric
# isalpha()   Returns True if all characters in the string are in the alphabet
# isdecimal() Returns True if all characters in the string are decimals
# isdigit()   Returns True if all characters in the string are digits
# isidentifier()  Returns True if the string is an identifier
# islower()   Returns True if all characters in the string are lower case
# isnumeric() Returns True if all characters in the string are numeric
# isprintable()   Returns True if all characters in the string are printable
# isspace()   Returns True if all characters in the string are whitespaces
# istitle()   Returns True if the string follows the rules of a title
# isupper()   Returns True if all characters in the string are upper case
# join()  Joins the elements of an iterable to the end of the string
# ljust() Returns a left justified version of the string
# lower() Converts a string into lower case
# lstrip()    Returns a left trim version of the string
# maketrans() Returns a translation table to be used in translations
# partition() Returns a tuple where the string is parted into three parts
# replace()   Returns a string where a specified value is replaced with a specified value
# rfind() Searches the string for a specified value and returns the last position of where it was found
# rindex()    Searches the string for a specified value and returns the last position of where it was found
# rjust() Returns a right justified version of the string
# rpartition()    Returns a tuple where the string is parted into three parts
# rsplit()    Splits the string at the specified separator, and returns a list
# rstrip()    Returns a right trim version of the string
# split() Splits the string at the specified separator, and returns a list
# splitlines()    Splits the string at line breaks and returns a list
# startswith()    Returns true if the string starts with the specified value
# strip() Returns a trimmed version of the string
# swapcase()  Swaps cases, lower case becomes upper case and vice versa
# title() Converts the first character of each word to upper case
# translate() Returns a translated string
# upper() Converts a string into upper case
# zfill() Fills the string with a specified number of 0 values at the beginning

#Boolean Values
print(10 > 5)
print(10 == 5)
print(10 < 11)

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator    Name    Example Try it
# +   Addition    x + y
# -   Subtraction x - y
# *   Multiplication  x * y
# /   Division    x / y
# %   Modulus x % y
# **  Exponentiation  x ** y
# //  Floor division  x // y

# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator    Example Same As Try it
# =   x = 5   x = 5
# +=  x += 3  x = x + 3
# -=  x -= 3  x = x - 3
# *=  x *= 3  x = x * 3
# /=  x /= 3  x = x / 3
# %=  x %= 3  x = x % 3
# //= x //= 3 x = x // 3
# **= x **= 3 x = x ** 3
# &=  x &= 3  x = x & 3
# |=  x |= 3  x = x | 3
# ^=  x ^= 3  x = x ^ 3
# >>= x >>= 3 x = x >> 3
# <<= x <<= 3 x = x << 3

# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator    Name    Example Try it
# ==  Equal   x == y
# !=  Not equal   x != y
# >   Greater than    x > y
# <   Less than   x < y
# >=  Greater than or equal to    x >= y
# <=  Less than or equal to   x <= y
# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator    Description Example Try it
# and     Returns True if both statements are true    x < 5 and  x < 10
# or  Returns True if one of the statements is true   x < 5 or x < 4
# not Reverse the result, returns False if the result is true not(x < 5 and x < 10)
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator    Description Example Try it
# is  Returns True if both variables are the same object  x is y
# is not  Returns True if both variables are not the same object  x is not y
# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator    Description Example Try it
# in  Returns True if a sequence with the specified value is present in the object    x in y
# not in  Returns True if a sequence with the specified value is not present in the object    x not in y
# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator    Name    Description
# &   AND Sets each bit to 1 if both bits are 1
# |   OR  Sets each bit to 1 if one of two bits is 1
#  ^  XOR Sets each bit to 1 if only one of two bits is 1
# ~   NOT Inverts all the bits
# <<  Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>  Signed right shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#List
thislist = ["this", "list"]
print(thislist)

#List Items
print(thislist[0])

#Type() list
print(type(thislist))

#The list() Constructor
thelist_constructor = list(('chao', 'cac'))
print(thelist_constructor)

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Negative Indexing
print(thislist[-1])

#Change Item Value
thislist[1] = "change_item_value"
print(thislist)

#Insert Items
thislist.insert(1, "insert_item")
print(thislist)

#Append Items
thislist.append("append_item")
print(thislist)

#Extend List
extend_list = ["extend", "list"]
thislist.extend(extend_list)
print(thislist)

#Add Any Iterable
add_any_iterable = ('add', 'any', 'iterable')
thislist.extend(add_any_iterable)
print(thislist)

#Remove Specified Item remove() method
thislist.remove("extend")
print(thislist)

#Remove Specified Index pop() method
thislist.pop(1)
print(thislist)

#The del keyword also removes the specified index:
del thislist[0]
print(thislist)

#Clear the List clear() method
thislist.clear()
print(thislist)

thislist_loop = ['chao', 'cac', 'ban']
#Loop Through a List
for i in thislist_loop:
    print(i)
#Loop Through the Index Numbers
#Use the range() and len() functions
for x in range(len(thislist_loop)):
    print(x)
    print(thislist_loop[x])

#Using a While Loop
while_loop = 0
while while_loop < len(thislist_loop):
    print(thislist_loop[while_loop])
    while_loop = while_loop + 1

#Looping Using List Comprehension
[print(x) for x in thislist_loop]
print("\n")


#List Comprehension
thislist_loop_1 = []
for t in thislist_loop:
    if "a" in t:
        thislist_loop_1.append(t)
print(thislist_loop_1)

#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

sort_list_alpanumerically = ["a", "c", "o", "z", "w", "l"]
sort_list_alpanumerically.sort()
print(sort_list_alpanumerically)

#Sort Descending
#To sort descending, use the keyword argument reverse = True:
sort_descending = ["a", "c", "o", "z", "w", "l"]
sort_descending.sort(reverse = True)
print(sort_descending)

#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.

def customize_sort_function(n):
    return abs(n - 50)
number_sort_list = [100, 200, 500, 250, 55]
number_sort_list.sort(key = customize_sort_function)
print(number_sort_list)

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
case_insensitive_sort = ["banana", "Orange", "Kiwi", "cherry"]
case_insensitive_sort.sort()
print(case_insensitive_sort)

#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:
case_insensitive_sort.sort(key = str.lower)
print(case_insensitive_sort)

#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.
reverse_order = ["banana", "Orange", "Kiwi", "cherry"]
reverse_order.reverse()
print(reverse_order)

#copy list
copy_list = ["a", "b" , "c"]
copy_list_1 = copy_list.copy()
print(copy_list_1)

copy_list_2 = list(copy_list)
print(copy_list_2)

#Join Two Lists
join_one = ["a", "b"]
join_two = [1, 2]
join_two_list = join_one + join_two
print(join_two_list)

#append() with join two list
for i in join_two:
    join_one.append(i)
print(join_one)

#extend() with join two list
join_one.extend(join_two)
print(join_one)

# List Methods

# Python has a set of built-in methods that you can use on lists.
# Method  Description
# append()    Adds an element at the end of the list
# clear() Removes all the elements from the list
# copy()  Returns a copy of the list
# count() Returns the number of elements with the specified value
# extend()    Add the elements of a list (or any iterable), to the end of the current list
# index() Returns the index of the first element with the specified value
# insert()    Adds an element at the specified position
# pop()   Removes the element at the specified position
# remove()    Removes the item with the specified value
# reverse()   Reverses the order of the list
# sort()  Sorts the list


#Python Sets {}

mysets = {"dang", "ho", "huu", "phuc"}

#SET
print(mysets)

#Get the Length of a Set len()
print(len(mysets))

#Type()

print(type(mysets))

#Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Set Methods

# Python has a set of built-in methods that you can use on sets.
# Method  Description
# add()   Adds an element to the set
# clear() Removes all the elements from the set
# copy()  Returns a copy of the set
# difference()    Returns a set containing the difference between two or more sets
# difference_update() Removes the items in this set that are also included in another, specified set
# discard()   Remove the specified item
# intersection()  Returns a set, that is the intersection of two other sets
# intersection_update()   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()    Returns whether two sets have a intersection or not
# issubset()  Returns whether another set contains this set or not
# issuperset()    Returns whether this set contains another set or not
# pop()   Removes an element from the set
# remove()    Removes the specified element
# symmetric_difference()  Returns a set with the symmetric differences of two sets
# symmetric_difference_update()   inserts the symmetric differences from this set and another
# union() Return a set containing the union of sets
# update()    Update the set with the union of this set and others

#https://www.w3schools.com/python/python_dictionaries.asp

#Python dictionaries
huuphuc = {
    "ho": "dang",
    "ten": "phuc",
    "tenlot": "ho huu",
    "daybith": 2000
}

print(huuphuc)
#dictionary items
print("ten la : " + huuphuc["ten"])

#Dictionary Ordered or Unordered?
# Duplicates Not Allowed
huuphuc1 = {
    "ho": "dang",
    "ten": "phuc",
    "tenlot": "ho huu",
    "daybith": 2000,
    "daybith": 2021
}
#nó sẽ in ra 2021 thay vì 2000 vì sẽ lấy giá trị ở cuối của biến
print(huuphuc1)

# Dictionary length
print(len(huuphuc))

#dictionary items - data types

huuphuc2 = {
    "ho": "dang",
    "ten": "phuc",
    "tenlot": "ho huu",
    "daybith": 2000,
    "datotnghiep": False,
    "caphoc": ["cap1", "cap2", "cap3", "daihoc"]
}

print(huuphuc2)

print(type(huuphuc2))

#Accessing Items (truy cập các mục)
accessinng_items = huuphuc2["ho"]
print(accessinng_items)

#use method get() when accessing items
accessinng_items_get = huuphuc2.get("ten")
print(accessinng_items_get)

#Dictionary get keys
dictionary_get_keys = huuphuc2.keys()
print(huuphuc2)

huuphuc2["car"] = "wave"
print(huuphuc2)

#Dictionary Get Values
dictionary_get_values = huuphuc2.values()
print(dictionary_get_values)

huuphuc2["car"] = "exenter"
print(dictionary_get_values)

# dictionary get items
dictionary_get_items = huuphuc2.items()
print(dictionary_get_items)

huuphuc2["car"] = "oto"
print(dictionary_get_items)

#Dictionary check if key exists
if "ho" in huuphuc2:
    print("key = \"ho\" have in huuphuc2 ")

#Update Dictionary
#you can use update() method:

huuphuc2.update({"car": "exenter"})
print(huuphuc2)

#add items use update() method:
huuphuc2.update({"like": "computer"})
print(huuphuc2)

#dictionary Removing Items
#you can use pop() method:
huuphuc2.pop("like")
print(huuphuc2)

#use popitem() method:
huuphuc2.popitem()
print(huuphuc2)

#use del
del huuphuc2["caphoc"]
print(huuphuc2)

#use clear() method:
huuphuc2.clear()
print(huuphuc2)

#https://www.w3schools.com/python/python_dictionaries_loop.asp
#Loop Through a Dictionary
huuphuc3 = {
    "ho": "dang",
    "ten": "phuc",
    "tenlot": "ho huu",
    "daybith": 2000,
    "datotnghiep": False,
    "caphoc": ["cap1", "cap2", "cap3", "daihoc"]
}

for x in huuphuc3:
    print(x)
print("--------------------------------------------------\n")

for x in huuphuc3:
    print(huuphuc3[x])
print("--------------------------------------------------\n")

#you can use values() method:
for x in huuphuc3.values():
    print(x)
print("--------------------------------------------------\n")

#you can use keys()
for x in huuphuc3.keys():
    print(x)
print("--------------------------------------------------\n")

#you can use items(): để in ra tất cả giá trị của dictionary
for x, y in huuphuc3.items():
    print(x, y)
print("--------------------------------------------------\n")

#copy dictionary
#you can use copy() method:
huuphuc4 = huuphuc3.copy()
print(huuphuc4)
print("--------------------------------------------------\n")

#you can use dict() method thay vì use copy() method:
huuphuc5 = dict(huuphuc3)
print(huuphuc5)
print("--------------------------------------------------\n")

#https://www.w3schools.com/python/python_dictionaries_nested.asp

#Python - nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child11 = {
  "name" : "Emil",
  "year" : 2004
}
child22 = {
  "name" : "Tobias",
  "year" : 2007
}
child33 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
  "child1" : child11,
  "child2" : child22,
  "child3" : child33
}
print(myfamily1)

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

#Python if ... else

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

if_else_1 = 120
if_else_2 = 140

#if else
if if_else_1 < if_else_2:
    print("lớn hơn")
else:
    print("nhỏ hơn")

#elif
if if_else_1 > if_else_2:
    print(" lon hon")
elif if_else_1 < if_else_2:
    print("nho hon")

#short hand if
if if_else_1 < if_else_2: print("be hon")

#short hand if ... else
print("lon hon") if if_else_1 > if_else_2 else print("nho hon")

if_else_3 = 160
#if ... else with and
if if_else_1 < if_else_2 and if_else_2 < if_else_3:
    print("nho hon")

#if ..else with or
if if_else_1 < if_else_2 or if_else_1 > if_else_3:
    print("1 lon")
print("\n")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#dùng để chứa một khối lệnh rỗng khi bạn chưa biết sử dụng nó thế nào

#Python while loops
#the while loop
while_loop = 1
while while_loop <= 5:
    print(while_loop)
    while_loop += 1
print("===================================================================\n")

#https://www.w3schools.com/python/python_while_loops.asp
#The break Statement
while_loop_1 = 1
while while_loop_1 < 5:
  print(while_loop_1)
  if while_loop_1 == 3:
    print("\n")
    break
  while_loop_1 += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#The continue Statement
while_loop_2 = 0
while while_loop_2 < 6:
    while_loop_2 += 1
    if while_loop_2 == 3:
        continue
    print(while_loop_2)

#Python For Loops
