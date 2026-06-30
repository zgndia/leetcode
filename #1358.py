class Solution(object):
    def numberOfSubstrings(self, s):
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        total_substrings = 0
        
        for i, char in enumerate(s):
            last_pos[char] = i
            
            min_index = min(last_pos.values())
            
            if min_index != -1:
                total_substrings += (min_index + 1)
                
        return total_substrings