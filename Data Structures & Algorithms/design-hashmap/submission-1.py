class Node:
    def __init__(self, key: int, value: int, right = None):
        self.right = right
        self.key = key
        self.value = value

class MyHashMap:
    def __init__(self):
        self.map = [Node(None, None)] * 10

    def put(self, key: int, value: int) -> None:
        node = self.map[self.hash(key)]
        while node.right:
            if node.right.key == key:
                node.right.value = value
                return
            node = node.right
        node.right = Node(key, value)

    def get(self, key: int) -> int:
        node = self.map[self.hash(key)].right
        while node:
            if node.key == key:
                return node.value
            node = node.right
        return -1

    def remove(self, key: int) -> None:
        node = self.map[self.hash(key)]
        while node.right:
            if node.right.key == key:
                node.right = node.right.right
                return
            node = node.right

    def hash(self, key: int) -> int:
        return key % 10

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)