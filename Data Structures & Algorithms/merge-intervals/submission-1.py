class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 

        intervals.sort()

        lst = [intervals[0]] 
        n = len(intervals) 

        for i in range(1,n):
            if intervals[i][0] <= lst[-1][1]:
                lst[-1][1] = max(lst[-1][1], intervals[i][1]) 
            else:
                lst.append(intervals[i]) 

        return lst
        