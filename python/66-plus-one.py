class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join([str(x) for x in digits]))
        number += 1
        new_digits = [int(x) for x in str(number)]
        return new_digits