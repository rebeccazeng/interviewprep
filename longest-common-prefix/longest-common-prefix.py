class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            s1, s2 = max(strs), min(strs)
            i, match = 0, 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i, match = i+1, match + 1
            return s1[0:match]
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         longest = ""
#         if len(strs) == 1:
#             longest = strs[0]
#         for i in range(len(strs)-1):
#             s1, s2 = strs[i], strs[i+1]
#             comp = self.compareStr(s1, s2)
#             if not comp:
#                 # meaning that the strings are not equal
#                 return longest
#             else:
#                 # meaning that the strings are equal
#                 longest = comp
                
#         return longest
    
#     def compareStr(self, s1, s2):
#         if s1 is None or s2 is None:
#             return ""
#         elif len(s1) != len(s2):
#             #whichever is longer, cut it down
            
#             return self.compareStr(s1[:mid], s2[:mid]) + self.compareStr(s1[mid:], s2[mid:])
#         elif s1 == s2:
#             return s1
#         else:
#             mid = len(s1) // 2
#             return self.compareStr(s1[:mid], s2[:mid]) + self.compareStr(s1[mid:], s2[mid:])
        
        