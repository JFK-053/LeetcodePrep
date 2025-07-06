class Solution:
    def isPalindrome(self, s: str) -> bool:

        loweredS = s.lower()

        sList = [character for character in loweredS if character.isalnum()]

        j = len(sList)-1

        for i in range(len(sList)//2):
            if sList[i] != sList[j]:
                return False
            j -= 1
        return True