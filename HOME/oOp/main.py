class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node =next_node

    def get_data(self):
        return self.data
