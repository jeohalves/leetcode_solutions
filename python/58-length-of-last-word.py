class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_strings = s.split(' ')
        size = 0

        while list_strings and len(list_strings[-1]) == 0:
            list_strings.pop()
        size = len(list_strings[-1])

        return size