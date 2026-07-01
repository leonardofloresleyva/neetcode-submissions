class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # MergeSort video solution (tweaked for less memory)
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i = L

            while left and right:
                if left[0] <= right[0]:
                    arr[i] = left.pop(0)
                else:
                    arr[i] = right.pop(0)
                i += 1

            while left:
                arr[i] = left.pop(0)
                i += 1

            while right:
                arr[i] = right.pop(0)
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums