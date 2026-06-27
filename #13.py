class Solution(object):
    def romanToInt(self, s):
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        i = 0
        str_len = len(s)

        while i < str_len:

            cur = val[s[i]]
            next = None
            if i + 1 < str_len:
                next = val[s[i + 1]]

            if next != None:
                if cur < next:
                    num += next - cur
                    i += 2
                    continue

            num += cur
            i += 1
        
        return num