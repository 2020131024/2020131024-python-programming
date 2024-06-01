class Solution:
    # AC, fast
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)

        max_len = 0
        result = None

        for i in range(s_len):
            left, right = i, i

            while left-1 >= 0 and right+1 < s_len and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            
            _len = right - left + 1
            if _len > max_len:
                max_len = _len
                result = s[left: right+1]

            left, right = i+1, i
            while left-1 >= 0 and right+1 < s_len and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            _len = right - left + 1
            if _len > max_len:
                max_len = _len
                result = s[left: right+1]

        return result
