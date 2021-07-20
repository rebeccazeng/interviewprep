class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        letters = {"2": ["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"],
                  "5": ["j", "k", "l"],"6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        for digit in digits:
            new_letters = letters[digit]
            combos = self.combine(new_letters, combos)
        return combos
    def combine(self, list1, list2):
        combined = []
        if len(list1) == 0 or len(list2) == 0:
            return list1+list2
        for piece in list1:
            for letter in list2:
                combined.append(letter+piece)
        print(combined)
        return combined
            
        