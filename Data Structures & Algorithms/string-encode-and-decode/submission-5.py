class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for s in strs:
            s_len = len(s) #length of following string for encoding. 
            # Pattern -> #s_len1<string1>#s_len2<string2>
            encoded_word = f"{s_len}#{s}"
            final_string += encoded_word

        return final_string

    def decode(self, s: str) -> List[str]:
        seen = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            # j + 1 is one character after the #
            word = s[j+1 : j+1+length]
            seen.append(word)
            # jump past the word
            i = j + 1 + length
        return seen

