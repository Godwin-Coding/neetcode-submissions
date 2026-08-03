class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lc = len(matrix[0])-1

        def recurse_row(s, e):
            if s > e:
                return False
            else:
                mid = (s + e) // 2
                if target == matrix[mid][0] or target == matrix[mid][lc]:
                    return True
                elif target < matrix[mid][0]:
                    return recurse_row(s, mid-1)
                elif target > matrix[mid][lc]:
                    return recurse_row(mid+1, e)
                else:
                    return recurse_cols(0, lc, matrix[mid])

        def recurse_cols(s, e, row):
            if s > e:
                return False
            else:
                mid = (s + e) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    return recurse_cols(mid+1, e, row)
                else:
                    return recurse_cols(s, mid-1, row)

        return recurse_row(0, len(matrix)-1)
        