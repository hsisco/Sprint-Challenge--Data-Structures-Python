class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None:                # If the node contails something:
            next = node.next_node           # add it to the list
            node.next_node = prev           # set the new node's next to prev
            self.reverse_list(next, node)   # run it again until all the nodes 'next's = prev & it passes the next node to the end
        else:
            self.head = prev                # if node == None, that's the end, so set the head to prev