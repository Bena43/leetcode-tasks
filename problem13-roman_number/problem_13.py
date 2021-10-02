class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        converting_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        roman_list = [char for char in s]
        # Reverse order of list, easier to handle special characters.
        roman_list_reversed = roman_list[::-1]
        for index, char in enumerate(roman_list_reversed):
            # Add value of current char to list, using the converting dictionary.
            value += converting_dict[char]
            if index == len(roman_list_reversed) - 1:
                # For last item of list, break here, no need for "special treatment"
                break
            elif self.is_special_combi(roman_list_reversed[index + 1], roman_list_reversed[index]):
                # Special treatment, next char's values should be decreased and not increased.

                # Continue to next char
                index += 1
                # Decrease it's value
                value -= converting_dict[roman_list_reversed[index]]
                # And remove it from the list for next attempt.
                roman_list_reversed.pop(index)

        return value

    def is_special_combi(self, next_char, current_char):
        if next_char == 'I' and current_char in ['V', 'X']:
            return True
        elif next_char == 'X' and current_char in ['L', 'C']:
            return True
        elif next_char == 'C' and current_char in ['D', 'M']:
            return True
        else:
            return False