from btree import BNode, BTree

bn = BNode(0)
assert(hasattr(bn, "content"))
assert(hasattr(bn, "left"))
assert(hasattr(bn, "right"))
assert(hasattr(bn, "__str__"))

tree = BTree()
assert(hasattr(tree, "root"))
assert(hasattr(tree, "__str__"))
assert(hasattr(tree, "add"))
assert(hasattr(tree, "find"))

assert(tree.__str__() == "<<E>>")
tree.add(20)
assert(tree.__str__() == "20")
tree.add(10)
assert(tree.__str__() == "20L10")
tree.add(25)
assert(tree.__str__() == "20L10R25")
tree.add(2)
assert(tree.__str__() == "20L10L2R25")
tree.add(15)
assert(tree.__str__() == "20L10L2R15R25")
tree.add(30)
assert(tree.__str__() == "20L10L2R15R25R30")
tree.add(23)
assert(tree.__str__() == "20L10L2R15R25L23R30")

n = tree.find(-9)
assert(n is None)

n = tree.find(20)
assert(n is not None)
assert(n.__str__() == "20L10L2R15R25L23R30")

n = tree.find(10)
assert(n is not None)
assert(n.__str__() == "10L2R15")

n = tree.find(25)
assert(n is not None)
assert(n.__str__() == "25L23R30")

n = tree.find(23)
assert(n is not None)
assert(n.__str__() == "23")