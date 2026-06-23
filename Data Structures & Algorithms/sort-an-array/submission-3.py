class Solution:
    # QuickSort implementation
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums)
        return nums

    def partition(self, arr: List[int], start: int, end: int) -> int:
        # Swap middle value with last value
        self.swap(arr, (start + end) // 2, end)
        # Takes last value as the pivot (previously middle value)
        pivot = arr[end]
        i = start - 1
        # Swapping
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                self.swap(arr, i, j)
        # Swaps last value with pivot index
        self.swap(arr, i + 1, end)
        # Returns pivot index
        return i + 1

    # Swapping function
    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    # Recursive sorting function
    def quickSort(self, nums: List[int], start = 0, end = None) -> None:
        if end is None:
            end = len(nums) - 1
        
        if start < end:
            pivotInx = self.partition(nums, start, end)
            self.quickSort(nums, start, pivotInx - 1)
            self.quickSort(nums, pivotInx + 1, end)
            