# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def AbirLinkedList(self, A, I):
        curA = A.head
        curI = I.head

        while curA and curI:
            if curA.val == curI.val:
                curA = curA.next
                curI = curI.next
            elif curA.val > curI.val:
                self.addToEnd(curI.val)
                curI = curI.next
            else:
                self.addToEnd(curA.val)
                curA = curA.next

        while curA:
            self.addToEnd(curA.val)
            curA = curA.next

        while curI:
            self.addToEnd(curI.val)
            curI = curI.next

    def addToStart(self, data):
        tempNode = ListNode(data)
        tempNode.next=self.head
        self.head = tempNode
        del tempNode

    def addToEnd(self, data):
        start = self.head
        if start is None:
            self.addToStart(data)
        else:
            while start.next:
                start = start.next
            tempNode = ListNode(data)
            start.next = tempNode
            del tempNode
        return True

    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.val), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
        print()


Abir = Solution()
Ahmed = Solution()
Islam = Solution()

Ahmed.addToEnd(1)
Ahmed.addToEnd(3)
Ahmed.addToEnd(5)
Ahmed.addToEnd(6)
Ahmed.addToEnd(7)
Ahmed.addToEnd(10)

Islam.addToEnd(1)
Islam.addToEnd(2)
Islam.addToEnd(3)
Islam.addToEnd(4)
Islam.addToEnd(5)
Islam.addToEnd(8)
Islam.addToEnd(9)

Ahmed.display()
Islam.display()
Abir.AbirLinkedList(Ahmed,Islam) # I dont know how to test this so I assume my code is correct
Abir.display()