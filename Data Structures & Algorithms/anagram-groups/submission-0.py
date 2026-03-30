class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A regular dict would give a KeyError when adding a word to an array key
        # defaultdict(list) allows access by creating an empty list
        anagrams = defaultdict(list)
        # Loop through words
        for word in strs:
            # Each word needs a number array to be filled with its characters
            wordChars = [0] * 26
            # For each letter in word, increase the count of the char at its position using ord.
            for char in word:
                wordChars[ord(char) - ord('a')] += 1
            # The array needs to be made immutable before it can become a key for the dict
            key = tuple(wordChars)
            # Add the word to the key, the key being its array of char counts
            anagrams[key].append(word)
        
        # Need to return a list so convert it to list
        return list(anagrams.values())

