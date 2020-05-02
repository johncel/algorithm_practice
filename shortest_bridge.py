# import matplotlib.pyplot as plt
# import numpy as np
class Solution:
                    
                    
    
    def shortestBridge(self, A) -> int:
        def find_island(A):
            nx = len(A[0])
            ny = len(A)
            for y, y_row in enumerate(A):
                for x, val in enumerate(y_row):
                    # print(f'find island y,x:{y},{x}')
                    if val == 0:
                        # print(f'wawa')
                        continue
                    if x > 0 and A[y][x-1] != 0:
                        # print(f'stuff left')
                        continue
                    if x < nx - 1 and A[y][x+1] != 0:
                        # print(f'stuff right')
                        continue
                    if y > 0 and A[y-1][x] != 0:
                        # print(f'stuff up')
                        continue
                    if y < ny - 1 and A[y+1][x] != 0:
                        # print(f'stuff down')
                        continue
                    
                    return y,x

        def get_next_visit(y, x, ny, nx, visited, next_visit):
            if y-1 >= 0 and visited[y-1][x] == 0:
                next_visit.add((y-1,x))
            if y+1 < ny and visited[y+1][x] == 0:
                next_visit.add((y+1,x))
            if x-1 >= 0 and visited[y][x-1] == 0:
                next_visit.add((y,x-1))
            if x+1 < nx and visited[y][x+1] == 0:
                next_visit.add((y,x+1))
 
            # print(f'get_next_visit {y}, {x}, visited:{visited} next_visit:{next_visit}')
            return next_visit
 
        def find_path(visited, A):
            # print(f'find_path visited:{visited} A:{A}')
            nx = len(A[0])
            ny = len(A)
            # visited = [[0] * len(A[0])] * len(A)
            # visited = [[0]*len(A[0]) for _ in range(len(A))]
            # for y,x in to_visit:
            #     visited[to_visit] = 1
            # print(f'visited: {visited} {y},{x}')
            # visited[y][x] = 1
            # print(f'visited: {visited}')
            # to_visit = get_next_visit(y, x, ny, nx, visited)
            # where to go next off this big island
            to_visit = set()
            for y, y_row in enumerate(visited):
                for x, val in enumerate(y_row):
                    if visited[y][x] == 1:
                        get_next_visit(y, x, ny, nx, visited, to_visit)
            flips = 0
            while to_visit:
                next_visit = set()
                # print(f' flips  length now:{flips} to_visit:{to_visit} visited:{visited} A:{A}')
                for y,x in to_visit:
                    # print(f'visiting {y}, {x}, val:{A[y][x]}')
                    visited[y][x] = 1
                    if A[y][x] == 1:
                        # print(f'bingo')
                        return flips
    
                    get_next_visit(y, x, ny, nx, visited, next_visit)
                to_visit = next_visit

                flips += 1


        def get_visited_for_island(y, x, visited, A_mod):
            # print(f'get_visited_for_island: y,x {y},{x} visited:{visited} A_mod:{A_mod}')
            nx = len(A_mod[0])
            ny = len(A_mod)

            to_visit = [[y,x]]

            local_visited = [[0]*len(A[0]) for _ in range(len(A))]

            levels = 0
            while to_visit:
                next_visit = set()
                for y,x in to_visit:
                    # print(f'get_visited_for_island:: visiting {y}, {x}, visited:{visited[y][x]}')
                    local_visited[y][x] = 1
                    if A_mod[y][x] == 1:
                        visited[y][x] = 1
                        get_next_visit(y, x, ny, nx, local_visited, next_visit)
    
                to_visit = list(next_visit)
                levels = levels + 1
                # print(f'get_visited_for_island levels: {levels} to_visit:{to_visit} nx:{nx} ny:{ny}')

            # print(f'get_visited_for_island:: DONE, visited:{visited}, A_mod: {A_mod}')
            # fig = plt.figure(figsize=(7,8))
            # np_visited = np.array(visited)
            # np_A_mod = np.array(A_mod)
            # ax1 = fig.add_subplot(121)
            # ax1.imshow(np_visited)
            # ax1 = fig.add_subplot(122)
            # ax1.imshow(np_A_mod)
            # plt.show()
            return

        # y,x = find_island(A)

        nx = len(A[0])
        ny = len(A)
        min_flips = nx * ny
        # to_visit = []
        island_visited = [[0]*len(A[0]) for _ in range(len(A))]
        for y, y_row in enumerate(A):
            for x, val in enumerate(y_row):
                # print(f'A::::::::::::: {y},{x} {A}')
                if not A[y][x]:
                    continue
                if island_visited[y][x]:
                    # print(f'skip')
                    continue

                ############# FIXME pass visited instead, say we visited all of these points, where is land! where are the jokes?
                # to_visit.append([y,x])
                # A_mod = A.copy()
                # A_mod = [a[:] for a in A]
                print(f'working an island')
                visited = [[0]*len(A[0]) for _ in range(len(A))]
                get_visited_for_island(y, x, visited, A)
                for y, row in enumerate(visited):
                    island_visited[y] = [ r | island_visited[y][x] for x,r in enumerate(row)]
                # fig = plt.figure(figsize=(7,8))
                # np_island_visited = np.array(island_visited)
                # ax1 = fig.add_subplot(121)
                # ax1.imshow(np_island_visited)
                # plt.show()
                # island_visited = visited
                # for y, y_row in enumerate(A_mod):
                #         A_mod[y] = [val for val in A[y]]
                # print(f'looking for paths from {y},{x}')
                # remove_me_island(y, x, A_mod)
                flips = find_path(visited, A)
                # print(f'found {flips} from {y},{x}')
                if flips < min_flips:
                    min_flips = flips
        return min_flips


A = [[0,1],[1,0]]
# A = [[0,1,0],[0,0,0],[0,0,1]]
# A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# A = [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
# A = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0]]
# A = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,0],[1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0],[0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

A = [[1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

sol = Solution()
flips = sol.shortestBridge(A)
print(f'flips: {flips}')
