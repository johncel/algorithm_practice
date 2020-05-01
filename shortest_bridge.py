class Solution:
                    
                    
    
    def shortestBridge(self, A) -> int:
        def find_island(A):
            nx = len(A[0])
            ny = len(A)
            for y, y_row in enumerate(A):
                for x, val in enumerate(y_row):
                    print(f'find island y,x:{y},{x}')
                    if val == 0:
                        print(f'wawa')
                        continue
                    if x > 0 and A[y][x-1] != 0:
                        print(f'stuff left')
                        continue
                    if x < nx - 1 and A[y][x+1] != 0:
                        print(f'stuff right')
                        continue
                    if y > 0 and A[y-1][x] != 0:
                        print(f'stuff up')
                        continue
                    if y < ny - 1 and A[y+1][x] != 0:
                        print(f'stuff down')
                        continue
                    
                    return y,x

        def get_next_visit(y, x, ny, nx, visited):
           next_visit = []
           if y-1 > 0 and visited[y-1][x] == 0:
               next_visit.append([y-1,x])
           if y+1 < ny and visited[y+1][x] == 0:
               next_visit.append([y+1,x])
           if x-1 > 0 and visited[y][x-1] == 0:
               next_visit.append([y,x-1])
           if x+1 < nx and visited[y][x+1] == 0:
               next_visit.append([y,x+1])

           return next_visit

        def find_path(y,x, A):
            nx = len(A[0])
            ny = len(A)
            visited = [[0] * len(A[0])] * len(A)
            visited[y][x] = 1
            to_visit = get_next_visit(y, x, ny, nx, visited)
            flips = 0
            while to_visit:
                next_visit = []
                for y,x in to_visit:
                    if A[y][x] == 1:
                        return flips
    
                to_visit = get_next_visit(y, x, ny, nx, visited)

                flips += 1

        y,x = find_island(A)
        flips = find_path(y, x, A)
        return flips
        print(f'island y,x: {y},{x}')


A = [[0,1],[1,0]]
A = [[0,1,0],[0,0,0],[0,0,1]]
# A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

sol = Solution()
flips = sol.shortestBridge(A)
print(f'flips: {flips}')
