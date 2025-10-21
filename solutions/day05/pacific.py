from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        # Store dimensions as instance variables, just like the C++ code
        self.m = len(heights)
        self.n = len(heights[0])

        # Create 'visited' grids for both oceans
        pacific = [[False] * self.n for _ in range(self.m)]
        atlantic = [[False] * self.n for _ in range(self.m)]

        # Start DFS from all cells bordering the Pacific (top and left)
        for i in range(self.m):
            self._dfs(heights, pacific, i, 0)
        for j in range(self.n):
            self._dfs(heights, pacific, 0, j)

        # Start DFS from all cells bordering the Atlantic (bottom and right)
        for i in range(self.m):
            self._dfs(heights, atlantic, i, self.n - 1)
        for j in range(self.n):
            self._dfs(heights, atlantic, self.m - 1, j)

        # Find the intersection of cells reachable by both oceans
        result = []
        for i in range(self.m):
            for j in range(self.n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result

    def _dfs(self, heights: List[List[int]], visited: List[List[bool]], r: int, c: int):
        """
        Helper DFS function to mark reachable cells from an ocean.
        We check (nr, nc) >= (r, c) because we are flowing "up" from the ocean.
        """
        visited[r][c] = True
        
        # Define directions (equivalent to static int dirs[4][2] in C++)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            # Boundary check
            if nr < 0 or nc < 0 or nr >= self.m or nc >= self.n:
                continue
            # Visited check
            if visited[nr][nc]:
                continue
            # Height check: Water can flow from (nr, nc) to (r, c) if
            # height[nr][nc] >= height[r][c]
            if heights[nr][nc] < heights[r][c]:
                continue
            
            self._dfs(heights, visited, nr, nc)
