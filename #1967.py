class Solution(object):
    def numOfStrings(self, patterns, word):
        substrings = 0
        for pattern in patterns:
            if pattern in word:
                substrings += 1
        
        return substrings