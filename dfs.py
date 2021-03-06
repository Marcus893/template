The DFS solution is straightforward. Starting from each point, and dfs its neighbor if the neighbor is equal or less than itself. And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. Finally go through all nodes again and see if it can be both reached by two oceans. The trick is if a node is already visited, no need to visited again. Otherwise it will reach the recursion limits.

This question is very similar to https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ And here are some common tips for this kind of question

init a directions var like self.directions = [(1,0),(-1,0),(0,1),(0,-1)] so that when you want to explore from a node, you can just do
for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
this is a what I normally do for a dfs helper method for exploring a matrix
def dfs(self, i, j, matrix, visited, m, n):
  if visited:
    # return or return a value
  for dir in self.directions:
    x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j] (or a condition you want to skip this round):
           continue
        # do something like
        visited[i][j] = True
        # explore the next level like
        self.dfs(x, y, matrix, visited, m, n)
