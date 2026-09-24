class Solution:
    def countBits(self, n: int) -> List[int]:
        OutputList = []
        for i in range(n+1):
            counter = 0
            q = i
            while(q>0):
                p = q%2
                q = q >> 1
                if p == 1:
                    counter = counter + 1
            OutputList.append(counter)
        return OutputList
        