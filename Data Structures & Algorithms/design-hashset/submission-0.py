class MyHashSet:
    # Low buckets solution
    def __init__(self):
        self.hashSet = [[]] * 6

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet[self.hashCode(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet[self.hashCode(key)].remove(key)

    def contains(self, key: int) -> bool:
        code = self.hashCode(key)
        return self.hashSet[code].count(key) > 0

    def hashCode(self, key: int) -> int:
        if key % 11 == 0:
            return 5
        if key % 7 == 0:
            return 4
        if key % 5 == 0:
            return 3
        if key % 3 == 0:
            return 2
        if key % 2 == 0:
            return 1
        else: 
            return 0
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)