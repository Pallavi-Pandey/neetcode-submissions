from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0]) if ROWS > 0 else 0
        
        # Distance increments in four directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Multi-source BFS queue
        q = deque()
        
        # Step 1: Add all treasure chest (0) cells to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Step 2: BFS from all treasure chests
        while q:
            r, c = q.popleft()
            
            # For each neighbor
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Skip out of bounds
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                
                # Only update empty land (INF)
                if grid[nr][nc] == 2**31 - 1:
                    # Set distance to current cell + 1
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
