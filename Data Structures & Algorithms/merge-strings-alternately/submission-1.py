class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Word length is 1 at minimum
        w1 = 0
        w2 = 0
        mergedStr = []

        while w1 < len(word1) and w2 < len(word2):
            mergedStr.append(word1[w1])
            mergedStr.append(word2[w2])
            w1 += 1
            w2 += 1
        mergedStr.append(word1[w1:])
        mergedStr.append(word2[w2:])

        return "".join(mergedStr)
        