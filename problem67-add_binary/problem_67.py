class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_result = 0
        iteration = 0
        while a or b:
            current = 0
            if not a:
                current += int(b[-1])
                b = b[:-1]
            elif not b:
                current += int(a[-1])
                a = a[:-1]
            else:
                current += int(a[-1])
                current += int(b[-1])
                a = a[:-1]
                b = b[:-1]
            int_result += current*(2**iteration)
            iteration += 1
        
        remain = 0
        result = ""
        if not int_result:
            return "0"
        while int_result:
            int_current = remain + (int_result%2)
            int_result //= 2
            if int_current % 2:
                current = "1"
            else:
                current = "0"
            if int_current > 1:
                remain = 1
            else:
                remain = 0
            result = current + result
            
        return result

        