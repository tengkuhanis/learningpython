class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
        #self.prev = self.next - 1

class QueQue:
    def __init__(self):
        self.front = self.rear = None

    def push_back(self, data):
        node = Node(data)
    	if self.isEmpty():
            self.rear = node
        else:
    		self.rear.next = node
    		self.rear = self.rear.next

    def push_front(x):
        node = Node(data)
    	if self.isEmpty():
    		self.front = node
    	else:
    		self.front.next = node
    		self.front = self.front.next

#    def push_middle(x):
#        node = Node(data)
#    	if self.isEmpty():
#    		self.rear = node
#    	else:
#    		self.rear.prev = node
#    		self.rear = self.rear.prev

#    def get(i):
#        for

QQ = QueQue()
QQ.push_back(9)
QQ.push_front(3)
QQ.push_middle(5)
QQ.get(0)
QQ.get(1)
QQ.get(2)
QQ.push_middle(1)
QQ.get(1)
QQ.get(2)
