class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def print(self):
		if self.top is None:
			print("Stack is empty, nothing to print!!!")
			return

		current = self.top # reference
		while current != None:
			print(current.data)
			current = current.next

	def push(self, data): #this
		node = Node(data)
		node.next = self.top
		self.top = node

	def pop(self):
		if self.top is None:
			return "Stack empty"

		element = self.top
		self.top = self.top.next
		return element

	def topElement(self):
		if self.top is None:
			return "Stack empty"

		return self.top.data

	def isEmpty(self):
		if self.top is None:
			return True
		else:
			return False

st = Stack()

st.push(1)
st.push(5)
st.push(10)
st.push(17)

# 17 -> 10 - > 5 -> 1 -> None
print("Elements of the Stack :")
st.print()

print("Top : ",st.topElement())

print("is it Empty ?", st.isEmpty())

st.pop()
print("Elements after Pop function")
st.print()

print("Top : ",st.topElement())
