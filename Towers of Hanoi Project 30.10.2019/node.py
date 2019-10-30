class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        self.link_node = link_node

    def get_next_node(self, link_node):
        return self.link_node

    def get_value(self):
        return self.value
