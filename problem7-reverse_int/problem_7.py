class Solution:
    def reverse(self, x: int) -> int:
        # Initialize reversed.
        reversed = 0
        # Work on positive, and flip sign eventually if needed.
        temp = abs(x)
        # 0 is skipped, no need to reverse.
        while temp > 0:
            reversed = int(reversed * 10 + temp % 10)
            temp = int(temp / 10)

        if x < 0:
            # flip reversed sign to negative, because X was negative.
            reversed = 0 - reversed
        if (reversed > 2 ** 31 - 1) or (reversed < -2 ** 31):
            # Return 0 on values that cannot be stored in int32.
            return 0
        else:
            return reversed