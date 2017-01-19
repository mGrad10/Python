'''
Melinda Grad
CS 305 ASM 5
Program to make Binary Tree iterable
'''


class BinaryTree:
    def __init__(self, content, leftSubtree=None, rightSubtree=None):
        self.content = content
        self.leftSubtree = leftSubtree
        self.rightSubtree = rightSubtree

    def __iter__(self):

        if self.leftSubtree:
            for x in self.leftSubtree:
                yield x

        yield self.content

        if self.rightSubtree:
            for y in self.rightSubtree:
                yield y

    def __repr__(self):
        return str(self.content)


Node = BinaryTree

if __name__ == '__main__':


    s = Node(1)
    t = Node(10, s, None)
    tree = BinaryTree(20, None, t)

    for x in (s, t, tree):
        print(x)

    for node in tree:
        print(node)
