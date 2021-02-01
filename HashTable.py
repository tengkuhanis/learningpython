# Program to implement Hashing with Quadratic and Cubic Probing
'''
ECIE3101/ECIE3312 DATA STRUCTURE AND ALGORITHM DESIGN
SEMESTER 1 20/21
PROJECT THEME: VISUALIZATION OF DATA STRUCTURE

=============== COLLABORATORS =====================

ECIE3312:
-Tengku Hanis Sofea Tengku Effendy (1810258)
-Nur Ain Nabila binti Mohd Rozi    (1815508)
-Siti Nur Farzana Binti Mohd Nasir (1818400)
-Nurul Farah Hazry binti Edy Hazry (1817042)
-Sarah Hannani binti Abdul Manah   (1912850)

ECIE3101:
-Tengku Hanis Sofea Tengku Effendy (1810258)
-Muhammad Adhwa Fathullah bin Nor Asmadi (1729131)
-Siti Nur Farzana Binti Mohd Nasir (1818400)
-Nur Ain Nabila binti Mohd Rozi (1815508)
-Ahmad Rahimi bin Yusoff (1722199)
'''
class hashTable:
    # initialize hash Table
    def __init__(self):
        choose = int(input("1-Quadratic Probing\n2-Cubic Probing.\nChoose the type of hash algorithm (1 or 2):"))
        if choose == 1 or choose == 2:
            self.probetype = choose
            self.size = int(input("Enter the Size of the hash table : "))

            # initialize table with all elements None
            self.table = list(0 for i in range(self.size))
            self.elementCount = 0
            self.hash_comp = 0
            self.hash_next_fail = 0
            self.hash_next_success = 0

        # exit program when user insert neither 1 or 2
        elif choose != 1 or choose != 2:
            print("Error!! Program has stopped. Please restart program and choose only 1 or 2.")
            exit()

    # method that checks if the hash table is full or not
    def isfull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    # method that returns position for a given element
    # replace with your own hash function
    def hashfunction(self, element):
        return element % self.size

    # method to resolve collision by quadratic/cubic probing method
    def probing(self, element, position):
        global newPosition
        if self.probetype == 1:  # performs quadratic probing
            posFound = False
            # limit variable is used to restrict the function from going into infinite loop
            # limit is useful when the table is 80% full
            limit = 50
            i = 1
            # start a loop to find the position
            while i <= limit:
                # calculate new position by quadratic probing
                newPosition = position + (i * i)
                newPosition = newPosition % self.size
                # if newPosition is empty then break out of loop and return new Position
                if self.table[newPosition] == 0:
                    posFound = True
                    break
                else:
                    # as the position is not empty increase i
                    i += 1
            return posFound, newPosition

        elif self.probetype == 2:  # perform cubic probing
            posFound = False
            # limit variable is used to restrict the function from going into infinite loop
            # limit is useful when the table is 80% full
            limit = 50
            i = 1
            # start a loop to find the position
            while i <= limit:
                # calculate new position by cubic probing
                newPosition = position + (i * i * i)
                newPosition = newPosition % self.size
                # if newPosition is empty then break out of loop and return new Position
                if self.table[newPosition] == 0:
                    posFound = True
                    break
                else:
                    # as the position is not empty increase i
                    i += 1
            return posFound, newPosition

    # method that inserts element inside the hash table
    def insert(self, element):
        # checking if the table is full
        if self.isfull():
            print("Hash Table Full")
            return False

        isStored = False

        position = self.hashfunction(element)

        # checking if the position is empty
        if self.table[position] == 0:
            # empty position found , store the element and print the message
            self.table[position] = element
            print("Element " + str(element) + " is at position " + str(position))
            isStored = True
            self.elementCount += 1

        # collision occurred, hence we do quadratic/cubic probing
        else:
            if self.probetype == 1: #performs quadratic probing
                print("Collision has occured for element " + str(element) + " at position " + str(
                    position) + ". Finding new Position.")
                isStored, position = self.probing(element, position)
                if isStored:
                    self.table[position] = element
                    self.elementCount += 1

            elif self.probetype == 2: #performs cubic probing
                print("Collision has occured for element " + str(element) + " at position " + str(
                    position) + ". Finding new position.")
                isStored, position = self.probing(element, position)
                if isStored:
                    self.table[position] = element
                    self.elementCount += 1

        return isStored

    # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, element):
        found = False

        position = self.hashfunction(element)
        self.hash_comp += 1

        if (self.table[position] == element):
            self.hash_next_success += 1
            return position

        # if element is not found at position returned hash function
        # then we search element using quadratic probing
        else:
            limit = 50
            i = 1
            newPosition = position
            # start a loop to find the position
            while i <= limit:
                if self.probetype == 1:
                    # calculate new position by quadratic probing
                    newPosition = position + (i * i)
                    newPosition = newPosition % self.size
                    self.hash_comp += 1

                elif self.probetype == 2:
                    # calculate new position by cubic probing
                    newPosition = position + (i * i * i)
                    newPosition = newPosition % self.size
                    self.hash_comp += 1

                # if element at newPosition is equal to the required element
                if self.table[newPosition] == element:
                    found = True
                    self.hash_next_success += 1
                    break

                elif self.table[newPosition] == 0:
                    found = False
                    break

                else:
                    # as the position is not empty increase i
                    i += 1
            if found:
                return newPosition
            else:
                print("Element not Found")
                self.hash_next_fail += 1
                return found

    # method to remove an element from the table
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
        return

    # method to display the hash table
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("The number of element(s) in the Table are : " + str(self.elementCount))

    #method to allow user enter input
    def input(self):
        d = self.size
        for i in range(d):
            x = int(input("Enter the value: "))
            table1.insert(x)

    #method to allow user search any element
    def seek(self):
        val = int(input("Enter element to search: "))
        print("The position of element " + str(val) + " is : " + str(table1.search(val)))

    # method to allow user delete any element
    def delete(self):
        m = int(input("Enter value to be deleted: "))
        table1.remove(m)


# main function
table1 = hashTable()
# storing elements in table
table1.input()
# displaying the Table
table1.display()
print()

#searching and printing position of elements
print("You can search up to 3 elements.")
table1.seek()
table1.seek()
table1.seek()

print("\nTotal number of comparisons done for searching = " + str(table1.hash_comp))
print("\nTotal number of times that the hashing scheme has to move to another slot "
      "during successful searches = " + str(table1.hash_next_success))
print("\nTotal number of times that the hashing scheme has to move to another slot "
      "during failed searches = " + str(table1.hash_next_fail))
print()

#deleting elements
print("You can delete up to 3 elements.")
table1.delete()
table1.delete()
table1.delete()

table1.display()



