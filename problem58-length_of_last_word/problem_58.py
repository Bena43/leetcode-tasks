class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing and leading spaces
        stripped_str = s.strip()
        # Reverse the string
        reversed_str = stripped_str[::-1]
        # Find the index of first space (which is the beginning of last word). this is also the len of the last word.
        len_of_last_word = reversed_str.find(" ")
        if len_of_last_word == -1:
            # If no spaces, singular word, result is the string len
            len_of_last_word = len(reversed_str)

        return len_of_last_word