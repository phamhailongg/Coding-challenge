class HashNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return "({0},{1})".format(self.key, self.value) + (str(self.next) if self.next is not None else "")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.nodes = [None for _ in range(self.size)]
    def set(self, key, value):
        new_node = HashNode(key, value)
        pos = self.hashfunction(key)
        if self.nodes[pos] is None:
            self.nodes[pos] = new_node
        else:
            curr_node = self.nodes[pos]
            while curr_node.next is not None:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                curr_node = curr_node.next
            if curr_node.key == key:
                curr_node.value = value
                return
            curr_node.next = new_node

    def get(self, key):
        pos = self.hashfunction(key)
        curr_node = self.nodes[pos]
        while curr_node.key != key and curr_node.next is not None:
            curr_node = curr_node.next
        if curr_node.key != key:
            return None
        else:
            return curr_node.value

    def hashfunction(self, key):
        return sum([ord(x) for x in key]) % self.size

    def __str__(self):
        return "".join([self.nodes[i].__str__() for i in range(self.size) if self.nodes[i] is not None])