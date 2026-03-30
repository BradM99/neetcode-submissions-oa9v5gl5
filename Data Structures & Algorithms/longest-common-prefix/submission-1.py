class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Iterate through the length of the first word
        for i in range(len(strs[0])):
            # Look through each word
            for s in strs:
                # If at the end of the word, OR the words element doesn't match that in the first string
                # Return this word up to that point
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        # Return the entire first word if nothing breaks
        return strs[0]