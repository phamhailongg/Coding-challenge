class BNode:
    def __init__(self, content, left = None, right = None):
        self.content = content
        self.left = left
        self.right = right

    def __str__(self):
        if self.content is None:
            return "<<E>>"
        return f"{self.content}" + (f"L{self.left}" if self.left is not None else "") + (f"R{self.right}" if self.right is not None else "")

    def add(self, val):
        if self.content is None:
            self.content = val
        if self.content > val:
            if self.left is None:
                self.left = BNode(val)
            else:
                self.left.add(val)
        if self.content < val:
            if self.right is None:
                self.right = BNode(val)
            else:
                self.right.add(val)

    def find(self, val):
        if self.content is None:
            return None
        if self.content > val:
            if self.left is None:
                return None
            return self.left.find(val)
        if self.content < val:
            if self.right is None:
                return None
            return self.right.find(val)
        if self.content == val:
            return self
        return None


class BTree:
    def __init__(self, root=None):
        self.root = BNode(root)

    def __str__(self):
        return self.root.__str__()

    def add(self, val):
        self.root.add(val)

    def find(self, val):
        return self.root.find(val)