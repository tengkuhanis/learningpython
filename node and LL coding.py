#NODE CLASS
#test_node(15)
#test_node.setLink(node_2)
# *default constructre
class Node:
    #default value of data and link is none if no data
    def _init_(self, data=None, link=None):
        self.data = data
        self.link = link

    #method to update the data of the Node
        def updateData(self, data):
            self.data = data

    #method to set link for the next node
    def setLink(self, node):
        self.link = node

    #method returns data stored in the node
        def getData(self):
            return self.data

#LINKED LIST CLASS

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None


    #method adds elements to the left of the LL
    def addToStart(self, data): # 21
        #create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode


    #method adds elements to the right of the LL
    def addToEnd(self, data): # data = 16
        start = self.head
        tempNode = Node(data) # data = 16 : link =none
        # start = 18 (head)

        #reach the last elmnt/ the tail:
        while start.getNextNode():
            start = start.getNextNode()
            start.setLink(tempNode)
        del tempNode
        return True

    #method displays Linked List
    def display(self):
        start = self.head
        #what if there is no element at all? - check head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            # the end space fx is to prevent it from printing new line
            start = start.link
            if start:
                print("-->", end=" ")
        print ()

        #method returns length of LL
        def length(self):
            start = self.head
            size = 0
            while start: #start != none
                size += 1
                start = start.getNextNode()
                #print(size)
             return size

         
        #method returns index of the received data
        def index(self, data):
            start = self.head
            position = 1

            while start:
                if start.getDsta() == data:
                    return position
                else:
                    position += 1
                    start = start.getNextNode()

        #method removes ite passed from the LL
        def remove(self, item):
            start = self.head
            previous =  None
            found = False

        #method returns max element from list
        def Max(self):
            start = self.head
            largest = start.getData()
            while start:
                if largest < start.getData():
                    largest = start.getData()
                start = start.getNextNode()
            return largest


        #method returns min element from list
        def Min(self):
            start = self.head
            smallest = start.getData()
            while start:
                if smallest > start.getData():
                    smallest = start.getData()
                start = start.getNextNode()
            return smallest

        #method pushes element to the LL
        def push(self, data):
            self.addToEnd(data)
            return True

        #method removes (pop) and returns the last element from LL
        def pop(self):
            start = self.head
            previous = None

            while start.getNextNode():
                previous = start
                start = start.getNextNode()

            if previous is None:
                self.head = None
                
            else:
                previous.setLink(None) // to tell the prev elmnt that you are the new last elmnt
                data = start.getData()
                del start
                return data

            #method removes item passed from the LL
            def remove(self, item):
                start = self.head
                previous = None
                found = False

                #search element in list
                while not found:
                    if start.getData() == item:
                        found = True
                    else:
                        previous = start
                        start = start.getNextNode()

                #if prev is None then the data is found
                    if previous is None:
                        self.head = start.getNextNode()
                    else:



            #method to clear LL
            def clear(self):
                self.head = None
                return True

            

#creating Linked List
myList = LinkedList()

#adding some elmnts to the start of LL
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
#1 2 3 4 5

myList.display()

#adding some elmnt to the end
myList.addToend(12)
myList.addToend(13)
myList.addToend(14)
#1 2 3 4 5 12 13 14

myList.display()

#print index of an elmnt
print(myList.index(12))

#removing elmnt
print(myList.remove(12))

myList.display()

#print max and min
print(myList.Max())
print(myList.Min())

#pushing and poping
print



#time complexity for adding to end = O(n) - bcs we need to go thru all elements















        























    
