class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            # Definition of strstr, return 0 if needle is empty.
            return 0
        elif len(haystack) == 0:
            # If haystack is empty but needle is not empty, needle not in haystack.
            # Here only for readability. if actually the case, below for will be skipped and -1 will be returned.
            return -1
        for index, char in enumerate(haystack):
            if index + len(needle) > len(haystack):
                # Needle cannot be in haystack because there's not enough chars left in haystack for finding needle.
                break
            elif needle == haystack[index:index+len(needle)]:
                # Needle found! return index it was found.
                return index
        return -1
        
        
        