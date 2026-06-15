class MyHashSet:
    # Many buckets solution
    def __init__(self):
        self.hashSet = [None] * 1000001

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet[key] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet[key] = None

    def contains(self, key: int) -> bool:
        return self.hashSet[key] == key

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)