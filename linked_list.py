
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)
        return helper(self.head)    

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        def helper(prev,current):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return helper(current,next_node)
        self.head = helper(None, self.head)
            

    def recursive_search(self, target):
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)
        return helper(self.head)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Display list and results of methods
ll = LinkedList()
ll.insert_at_front(2)
ll.insert_at_front(1)
ll.insert_at_end(3)

ll.display()
print(ll.recursive_sum())
ll.recursive_reverse()
ll.display()


