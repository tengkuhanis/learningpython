#Hash Tables
#Implementation
#Example: Count alphabets on a string

# Hash Table -> { Key : value} : Hash table size

# array size 10 -> idx 0 ->, the index 13 x

# Hash -> key : new_key = key % size_table ;
# Y = a%b -> Y will never be greater than b, 0->(b-1)

# hash_table = [None,None,None,None,None] ; size =5

#15 -> "random"
#12 -> "ok"
#4 -> "dog"
#33 -> "cat"
#23 -> "good"
#we going to show these value in the upper table

# def gethashedkey(key,size): 15,5
  # new_key = key%size
  # return

# hash_table(gethashedkey(key1,5)) = value1;
# hash_table = [random,None,ok,cat,dog] ; size = 5

#collision open address
# 33 & 23 - when mod 5, remainder = 3 -> collision at cat
# first - replace good at cat, then cat put at empty(none)
#this is open addressing
# hash_table = [random,cat,ok,good,dog] ; size = 5

#if there is collision
#  i) check is there is empty
#  ii) if no empty, depends whether to replace or refuse to hash the new element

#getitem- getting an element
#setitem- setting an element and put it on the list


#Searching
#Linear Search - complexity = O(n)

#Binary Search
#time complexity of binary search = log(n)
  #Binary Search Over the answer
