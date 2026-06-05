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
        for index, item in enumerate(s):
            decoded_word = ""
            if item.isdigit():
                # if we find a digit ever, then we know that
                # it is the start of a new word.
                len_word = int(item)
                hashtag_index = index + 1
                # double check that we have the beginning of a word
                word_starting_index = hashtag_index + 1
                while len(decoded_word) < len_word:
                    decoded_word += s[word_starting_index]
                    word_starting_index += 1
                seen.append(decoded_word)
        return seen

