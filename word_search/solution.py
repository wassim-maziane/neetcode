class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                print(i, j)
                self.backtrack(i, j, "", set(), board, word)
        return self.res

    def backtrack(
        self,
        i: int,
        j: int,
        cur: str,
        visited: set[tuple[int, int]],
        board: list[list[str]],
        word: str,
    ):
        cur += board[i][j]
        if cur == word:
            self.res = True
        if cur != word[: len(cur)]:
            return
        n = len(board)
        m = len(board[0])
        visited.add((i, j))

        if i > 0 and (i - 1, j) not in visited and len(cur) < len(word):
            self.backtrack(i - 1, j, cur, visited.copy(), board, word)
        if j > 0 and (i, j - 1) not in visited and len(cur) < len(word):
            self.backtrack(i, j - 1, cur, visited.copy(), board, word)
        if i < n - 1 and (i + 1, j) not in visited.copy() and len(cur) < len(word):
            self.backtrack(i + 1, j, cur, visited.copy(), board, word)
        if j < m - 1 and (i, j + 1) not in visited and len(cur) < len(word):
            self.backtrack(i, j + 1, cur, visited.copy(), board, word)
