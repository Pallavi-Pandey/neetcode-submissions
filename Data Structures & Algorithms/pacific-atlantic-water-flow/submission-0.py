class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pac = [[False]*cols for _ in range(rows)]
        atl = [[False]*cols for _ in range(rows)]

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 
                    0 <= nc < cols and 
                    not visited[nr][nc] and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Start from all pacific edges
        for r in range(rows):
            dfs(r, 0, pac)
        for c in range(cols):
            dfs(0, c, pac)

        # Start from all atlantic edges
        for r in range(rows):
            dfs(r, cols-1, atl)
        for c in range(cols):
            dfs(rows-1, c, atl)

        ans = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    ans.append([r, c])

        return ans
