class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}



        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagramDict[sortedWord] = anagramDict.get(sortedWord, [])
            anagramDict[sortedWord].append(word)

        anagrams = list(anagramDict.values())
        return(anagrams)
        