"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # flatten the List:
        flattened_list = list(itertools.chain(*board))
        
        ColHashmap = defaultdict(lambda: defaultdict(int))
        RowHashmap = defaultdict(lambda: defaultdict(int))
        SubboxHashmap = defaultdict(lambda: defaultdict(int))

        for i in range(81):
            if flattened_list[i] != '.':
                ColHashmap[i % 9][flattened_list[i]] += 1 # col index
                RowHashmap[i // 9][flattened_list[i]] += 1 # row index

                subbox_index = (i // 27) * 3 + ((i % 9) // 3) # sub box index
                SubboxHashmap[subbox_index][flattened_list[i]] += 1 
            else:
                continue
        
        # check each col    
        for hmap in list(ColHashmap.values()) :
            if any(x > 1 for x in list(hmap.values())):
                
                return False                
        # check each row
        for hmap in list(RowHashmap.values()) :
            if any(x > 1 for x in list(hmap.values())):
                
                return False

        # check subboxes:
        for hmap in list(SubboxHashmap.values()) :
            if any(x > 1 for x in list(hmap.values())):
                
                return False

        return True