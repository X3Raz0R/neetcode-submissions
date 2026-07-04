class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            fr = {}
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in fr:
                        return False
                    fr[val] = 1

        for j in range(9):
            fr = {}
            for i in range(9):
                val = board[i][j]
                if val != ".":
                    if val in fr:
                        return False
                    fr[val] = 1

        for ki in range(3):
            for kj in range(3):
                fr = {}
                for i in range(ki*3, ki*3 + 3):
                    for j in range(kj*3, kj*3 + 3):
                        a = board[i][j]
                        if a != ".":
                            if a in fr:
                                return False
                            fr[a] = 1
        return True