class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        columns = len(grid[0])
        for row in range(rows):
            if grid[row][0] < 0:
                count += ((rows - row) * columns)
                break
            for column in range(columns):
                if grid[row][column] < 0:
                    count += (columns - column)
                    break
        return count