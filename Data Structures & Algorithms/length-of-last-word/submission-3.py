class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        if len(s) == 1:
            return 1

        for i in range(len(s) -1, 0, -1):
            if s[i].isalpha():
                count += 1
            if s[i] == " " and count > 0:
                return count
        return count