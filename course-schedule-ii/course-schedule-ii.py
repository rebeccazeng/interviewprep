class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of the prereqs
        prereq = {c:[] for c in range(numCourses)}
        # fill in the adj list
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states
        # visited: crs has been added to output
        # visiting: crs not added to output, but added to cycle
        # unvisited: crs not added to output or cycle

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                # there's a cycle
                return False
            if crs in visit:
                # don't need to visit again
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        # executing with the dfs
        for c in range(numCourses):
            if dfs(c) == False: 
                return []
            
        return output
            