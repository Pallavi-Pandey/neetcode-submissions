from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            print("Empty grid, nothing to process")
            return

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        print("Initial Grid:")
        for row in grid:
            print(row)

        # Step 1: Push all treasures (0) into queue
        print("\nAdding all treasure cells to queue:")
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    print(f"Treasure found at ({r}, {c}) → added to queue")

        # Directions: down, up, right, left
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        print("\nStarting BFS...\n")

        # Step 2: BFS
        while q:
            r, c = q.popleft()
            print(f"Processing cell ({r}, {c}) with value {grid[r][c]}")

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # boundary + condition checks
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    print(f"  Skipping ({nr}, {nc}) → out of bounds")
                    continue

                if grid[nr][nc] != INF:
                    print(f"  Skipping ({nr}, {nc}) → not INF (value={grid[nr][nc]})")
                    continue

                # update distance
                grid[nr][nc] = grid[r][c] + 1
                print(
                    f"  Updating ({nr}, {nc}) to distance {grid[nr][nc]} → added to queue"
                )
                q.append((nr, nc))

            print("Queue state:", list(q))
            print("Current Grid:")
            for row in grid:
                print(row)
            print("-" * 40)

        print("\nFinal Grid:")
        for row in grid:
            print(row)
