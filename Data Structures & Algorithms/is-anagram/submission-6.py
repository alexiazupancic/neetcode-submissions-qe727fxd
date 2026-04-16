class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def count_letters(x: str):
            letters = {}
            for letter in x:
                letters[letter] = letters.get(letter, 0) + 1
            return letters

        s_letters = count_letters(s)
        t_letters = count_letters(t)

        if s_letters == t_letters:
            return True
        else:
            return False

        