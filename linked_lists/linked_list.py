class Element(object): # Why (object) ?
    def __init__(self, value): # Ask question - what type of values does it store?
        # OOP training - __init__ is a constructor. Learn about types of constructors (in python) and their uses
        self.value = value
        self.next = None


class LinkedList(object):
    # Memorize everything!! - of course by understanding it!
    def __init__(self, head=None):
        # Initially linked list is null / None in python
        self.head = head

    def append(self, value):
        # Inserts element with given value at the end of linked list
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Element(value)
        else:
            self.head = Element(value)

    def get_position(self, position):
        # Questions to ask: 
        # 1. What is starting position (Or tell them that you assume it starts at 0)
        # 2. What to do when element is not found? Return None or return a string that says it's not available
        # or print that it's not available
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        current = self.head
        counter = 1
        while counter < position and current:
            current = current.next
            counter += 1
        
        if current:
            return current.value
    
        return None

    def insert(self, value, position):
        # Questions
        # 1. What to do when you can't insert the element as position goes out of index?
        # 2. Does this even return anything?
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position > 1: # you did not check the corner case where the ll is empty initially
            current = self.head
            counter = 1
            while counter < position-1 and current.next:
                current = current.next
                counter += 1
            
            if counter == position-1:
                el = Element(value)
                el.next = current.next
                current.next = el
        elif position == 1: # Make more precise conditions to avoid corner cases that lead to errors
            el = Element(value)
            el.next = self.head
            self.head = el

    def delete(self, value):
        # Questions
        # 1. Does it return anything?
        # 2. What does it return when it finds the el and deletes it and what does it return when it doesn't fine el.
        """Delete the first node with a given value."""
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            else:
                prev = self.head.next
                curr = self.head.next
                while curr:
                    if curr.value == value:
                        prev.next = curr.next
                        break
                    else:
                        prev = curr
                        curr = curr.next

    # def delete(self, value):
    #         current = self.head
    #         previous = None
    #         while current.value != value and current.next:
    #             previous = current
    #             current = current.next
    #         if current.value == value:
    #             if previous:
    #                 previous.next = current.next
    #             else:
    #                 self.head = current.next
                    
    def display(self):
        print('Linked List:')
        if self.head is None:
            print("None")
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

ll = LinkedList()
ll.display()
ll.insert(2, 1)
ll.display()
ll.insert(3, 2)
ll.display()
ll.insert(4, 3)
ll.display()
ll.insert(1, 1)
ll.display()
ll.delete(3)
ll.display()
ll.delete(4)
ll.display()
ll.delete(1)
ll.display()
ll.delete(2)
ll.display()

# Test cases
# Set up some Elements
# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)

# # Start setting up a LinkedList
# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
# # ll.display()

# # Test get_position
# # Should print 3
# print(ll.head.next.next.value)
# # Should also print 3
# print(ll.get_position(3).value)

# # Test insert
# ll.insert(e4,3)
# # ll.display()
# # Should print 4 now
# print(ll.get_position(3).value)

# # Test delete
# ll.delete(1)
# # ll.display()
# # Should print 2 now
# print(ll.get_position(1).value)
# # Should print 4 now
# print(ll.get_position(2).value)
# # Should print 3 now
# print(ll.get_position(3).value)

