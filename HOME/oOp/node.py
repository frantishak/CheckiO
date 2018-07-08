class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data=None):
        self.data = data

    def get_next_node(self):
        return self.get_next_node

    def set_next_node(self, next_node=None):
        self.next_node = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def inser_head(self, data):
        next_node = Node(data)
        self.head, self.new_next_node = next_node, self.head



if __name__ == "__node__":
    test_node = Node("234")
    print(test_node())