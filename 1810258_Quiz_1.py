# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def updateData(self, val):
        self.val = val

    #-----------method to set Link for the Next Node---------------------------
    def setLink(self, node):
        self.next = node

    #----------method returns data stored in the Node--------------------------
    def getData(self):
        return self.val

    #-----method returns address of the next Node // goes to the Next Node-----
    def getNextNode(self):
        return self.next


    # ------method adds elements to the right of the Linked List---------------


class AbirLinkedList:
    def AbirLinkedList(self, Ahmed: ListNode, Islam: ListNode) -> ListNode:
        self.head = None
        self.tail = None

    def addToStart(self, val):
        tempNode = ListNode(val)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode
        if self.tail is None:
            self.tail = self.head

    def addToEnd(self, val):
        start = self.head
        if start is None:
            self.addToStart(val)
        else:
            while start.getNextNode():
                start = start.getNextNode()
            tempNode = Node(val)
            start.setLink(tempNode)
            del tempNode
            self.tail = start.getNextNode()
        return True

    def display(self):
         start = self.head
         if start is None:
             print("Empty List!!!")
             return False

         while start:
             print(str(start.getData()), end=" ")
             start = start.next
             if start:
                 print("-->", end=" ")
         print()
#---------------creating linked list------------------------------------
myList = AbirLinkedList()

myList.addToStart(50)
myList.addToStart(31)
myList.addToStart(17)
myList.addToStart(12)
myList.addToStart(8)
myList.addToStart(6)
myList.addToStart(3)

print("First Linked List Created:")
myList.display()
