class Solution:
    def lastStoneWeightII(self, stones) -> int:
#        while len(stones) > 1:
#            stones = sorted(stones)
#            #remove the matches
#            stones = sorted(stones)
#            last_val = -1
#            new_stones = []
#            for i, val in enumerate(stones):
#                if val != last_val:
#                    new_stones.append(val)
#                    last_val = val
#
#            print(f'remove dupes: stones:{stones} new_stones:{new_stones}')
#            stones = new_stones
#
#            new_stones = []
#            n = len(stones)
#            # for i in range(0,n//2):
#            i = 0
#            left = stones[i]
#            right = stones[n-1-i]
#            diff = abs(right - left)
#            if diff > 0:
#                new_stones.append(diff)
#            # if n % 2:
#            new_stones += stones[1:n-1]
#            print(f'stones:{stones} news_stones:{new_stones}')
#            stones = new_stones
#            
#        if len(stones) == 1:
#            return stones[0]
#        else:
#            return 0
        lookup = {}
        
        def sub_result(i, r):
            key = (i,r)
            if key in lookup:
                return lookup[key]
            
            if i == len(stones):
                return abs(r)

            res = min(sub_result(i+1, r+stones[i]), sub_result(i+1, r-stones[i]))
            lookup[key] = res
            return res

        return sub_result(0,0)

A = [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98]

sol = Solution()
print(sol.lastStoneWeightII(A))
