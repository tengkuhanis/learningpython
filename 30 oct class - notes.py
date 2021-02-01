#1-> lists (methods)
    # Appending mylist = [1,2,5,6]
    # Appending mylist = [1,"ok",5,6] 0-> based 
    # first index starts from 0
    # mylist.append(14) -> [1,"ok",5,6,14] (can also append string)
    # mylist.append("huhu")
    #create new empty list ->  add the element -1
    #print(mylist[3]) -> 6
    # len(mylist) -> 5 elements
    #last element index -> len(mylist)-1
    #print(mylist[-1]) -> 14
    #print(mylist[-2])
    # pop // remove elmnts from the right
    # mylist.pop()
    # print (mylist) -> [1,"ok",5,6]
    #mylist[1] = 0
    #print (mylist) [1,0,5,6]
    #time complexity to appending an element to the list -> O(n)- because we are adding at the last
    #n=number of elements in array
    #search an element with a known index -> time complexity = O(1)
    
#2-> linked lists + types
    #linked list - dynamic- compiler doesnt have to know what the size of error
    # i.e: const SIZE =100
    # int arr [SIZE] - this is static
    # 1 5 6 18 - need to attach this elmnts together to form a kind of list
    #1 5 6 18 || data : 18, pointing where? : 1
    #each block (in linked list) consist 2 main thing: the data and where it is pointing
    # example; not related to upper line
    # 18 -> 1 -> 6 -> 5 -> NULL // single linked list
    # 0-index -> Head - the first thing in the list
    #         -> Tail - last thing
    # 18 -> 1 -> 6 -> 5 -> 18 // circular linked list
    # 18 -> 1 <-> 6 <-> 5 // double linked list
    # 19 -> None // head || tail
    
#3-> why linked lists?



































    
#4-> linked list python implementation
