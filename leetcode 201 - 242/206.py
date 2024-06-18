class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDict = collections.defaultdict(set)
        for a, b in prerequisites:
            preDict[a].add(b)

        visit = [0] * numCourses

        def DFS(course):
            if visit[course] == -1:
                return False
            if visit[course] == 1:
                return True

            visit[course] = -1
            for i in preDict[course]:
                if not DFS(i):
                    return False

            visit[course] = 1
            return True

        for i in range(numCourses):
            if not DFS(i):
                return False

        return True
