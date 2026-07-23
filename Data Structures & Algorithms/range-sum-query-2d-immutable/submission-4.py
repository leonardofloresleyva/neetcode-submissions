class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__prefixSum = []
        self.__initialize(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.__prefixSum[row2][col2]
        # Checks if there are upper and left areas to substract
        isUpper = row1 - 1 >= 0
        isLeft = col1 - 1 >= 0
        # Substracts both areas if any is present
        if isUpper or isLeft:
            upper = self.__prefixSum[row1 - 1][col2] if isUpper else 0
            left = self.__prefixSum[row2][col1 - 1] if isLeft else 0
            left -= self.__prefixSum[row1 - 1][col1 - 1] if isUpper and isLeft else 0
            ans -= upper + left
        return ans
    
    def __initialize(self, matrix: List[List[int]]):
        # Numbers of rows and columns
        rowsSize = len(matrix)
        colSize = len(matrix[0])
        # Prefix sum
        for i in range(rowsSize):
            row = []
            for j in range (colSize):
                # Store the initial value
                cell = matrix[i][j]
                # Add to it all previous values
                for z in range(j):
                    cell += matrix[i][z]
                # Add the value of the upper cell (the above submatrix sum) if possible
                if i - 1 >= 0:
                    cell += self.__prefixSum[i - 1][j]
                # Append the cell to the new row
                # The cell contains the sum of the submatrix
                row.append(cell)
            # Append the full row
            self.__prefixSum.append(row)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)