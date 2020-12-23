"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position <= 1:
            return self.head
        else:
            current = self.head
            for _ in range(1, position):
                # we do not want to count the head
                if current.next is None:
                    return None
                else:
                    current = current.next
            return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
            That means it need to be at 2nd elements position only
        """
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            current = self.head
            for _ in range(1, position - 1):
                current = current.next
            new_element.next = current.next
            current.next = new_element
        # pass

    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head:
            if self.head.value == value:
                self.head = self.head.next

            current = self.head
            while current.next:
                if current.next.value != value:
                    current = current.next
                else:  # means that we found the node has the value
                    current.next = current.next.next

    def printLinkedList(self):
        if self.head:
            current = self.head
            print(current.value, end=" -> ")
            while current.next:
                current = current.next
                print(current.value, end=" -> ")
            print()
        else:
            print("Empty list")


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.printLinkedList()

# Test get_position
# Should print 3
print(ll.head.next.next.value)

# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
ll.printLinkedList()
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)

ll.printLinkedList()

# Should print 2 now
print(ll.get_position(1).value)

# Should print 4 now
print(ll.get_position(2).value)

# Should print 3 now
print(ll.get_position(3).value)
