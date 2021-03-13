from typing import List, Optional


class Node:
    def __init__(self,
                 key: Optional[int],
                 left: "Node" = None,
                 right: "Node" = None):

        self.key = key
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node {self.key}"

    def append(self, key: int) -> None:
        if self.key is None:
            self.key = key
            return

        if key < self.key:      # go to left subtree
            if self.left is None:
                self.left = Node(key=key)
            else:
                self.left.append(key)       #rekurencja wywołuje siebie i leci od poczatku
        else:       # go to right subtree
            if self.right is None:
                self.right = Node(key=key)
            else:
                self.right.append(key=key)

    def traverse(self) -> None:
        # NLR
        print(self.key)
        if self.left is not None:
            self.left.traverse()
        if self.right is not None:
            self.right.traverse()

    # def traverse(self) -> None:
    #     #  LNR
    #
    #     if self.left is not None:
    #         self.left.traverse()
    #     print(self.key)
    #
    #     if self.right is not None:
    #         self.right.traverse()

    # def traverse(self) -> None:
    #     # LRN
    #
    #     if self.left is not None:
    #         self.left.traverse()
    #
    #
    #     if self.right is not None:
    #         self.right.traverse()
    #
    #     print(self.key)


#nie rekurencyjna metoda traversu:

def traverse(root: Node) -> List[Node]:

    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

        # if node.right is not None:        jeśli ten kod będzie w tym miejscu to ze stack najpier
        #     stack.append(node.right)      bedzie wyciagana wartosc right zamiast left, i bedzie trochę kolejnaość poprzestawiana


# data = [1,2,10,9,4,10,11]
def create_binsearch_tree(root: Node, data: List[int]) -> Node:
    size = len(data)
    if size != 0:

        items = sorted(data)
        size = len(items)

        middle = size // 2
        root.append(items[middle])

        create_binsearch_tree(root, items[:middle])
        create_binsearch_tree(root, items[middle+1:])
    return root


if __name__ == "__main__":
    root = Node(key=None)
    data = [1, 2, 10, 9, 4, 10, 11]
    root = create_binsearch_tree(Node(key=None), data)
    root.traverse()
    # root.append(42)
    # root.append(40)
    # root.append(50)
    # root.append(30)
    # root.append(60)
    # root.append(70)

    ##print(root, root.left, root.right, root.left.left, root.right.right)  #kolejne poziomy to kolejne righ.right.left.right ipt itd

    # root.traverse()
    #
    # for node in traverse(root):
    #     print(node)
