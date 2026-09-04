class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            seenRow = set()
            seenCol = set()
            seenBox = set()
            for j in range(len(board[i])):
                #row check
                if(board[i][j] != '.'):
                    if(board[i][j] in seenRow):
                        return False
                seenRow.add(board[i][j])

                #col check
                if(board[j][i] != '.'):
                    if(board[j][i] in seenCol):
                        return False
                seenCol.add(board[j][i])

                #box check
                boxRow = 3 * (i // 3) + (j // 3)
                boxCol = 3 * (i % 3) + (j % 3)
                boxVal = board[boxRow][boxCol]
                if(boxVal != '.'):
                    if(boxVal in seenBox):
                        return False
                seenBox.add(boxVal)
            


        return True