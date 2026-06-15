class MyHashSet:
    # Lesser memory usage
    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key)
            self.hashSet.sort()

    def remove(self, key: int) -> None:
        i = self.bfs(key)
        if i > -1:
            self.hashSet.pop(i)

    def contains(self, key: int) -> bool:
        return self.bfs(key) > -1

    def bfs(self, target: int) -> int:
        left = 0
        right = len(self.hashSet) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if target == self.hashSet[middle]:
                return middle

            if target > self.hashSet[middle]:
                left = middle + 1
            else:
                right = middle - 1
            
        return -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)