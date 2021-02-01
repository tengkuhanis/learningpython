class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class Queue:
	def __init__(self):
		self.front = self.rear = None

	def enqueue(self, data):
		node = Node(data)
		if self.isEmpty():
			self.front = self.rear = node
		else:
			self.rear.next = node
			self.rear = self.rear.next

	def dequeue(self):
		if self.isEmpty():
			return "Queue empty"
		else:
			temp = self.front
			self.front = self.front.next
			return temp.data

	def isEmpty(self):
		if self.front == None and self.rear == None:
			return True
		else:
			return False

	def frontQ(self):
		if self.isEmpty():
			return "Queue empty"
		else:
			return self.front.data

	def print(self):
        # check Emptyness 
		while(self.front != None):
			print(self.front.data)
			self.front = self.front.next
