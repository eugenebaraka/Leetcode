class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # initialize the first element as a reference prefix
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # str.find will return 0 if the while prefix was found within strs[i]
            # otherwise will return -1 if prefix not found
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
                
        return prefix
        
        
        