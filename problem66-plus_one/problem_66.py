class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Solution with no python trickery, wanted to practice recursion.
        # Possible easier solutions would be to convert this list to either a string or an int, perform the operation, and go back to list.
        if digits[-1] == 9:
            # Only 9 acts differently than "+1", because this affects other list items.
            # Current last item should be zero.
            digits[-1] = 0
            if len(digits) > 1:
                # Recursion without last item
                temp_digits = self.plusOne(digits[:-1])
                # add last item to solution
                temp_digits.append(digits[-1])
                return temp_digits

            else:
                # Last item is 9, should add a leading "1" to enlarge list size.
                temp_digits = [1]
                temp_digits.extend(digits)
                return temp_digits

        else:
            digits[-1] += 1
            return digits