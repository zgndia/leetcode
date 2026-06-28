class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        pnum = strs[0] # primary index number - we will compare this value to others while finding the common
        pnum_index = strs.index(pnum)
        i = 0
        while i < len(pnum):
            current_letter = pnum[i]
            conf = 0

            ic = 0 # index counter for word in strs
            for word in strs:
                if ic == pnum_index:
                    ic += 1
                    continue
                if i >= len(word):
                    break

                if current_letter == word[i]:
                    conf += 1
                
                ic += 1
            
            if conf == len(strs) - 1:
                common += current_letter
            else:
                break
            
            i += 1

        return common
