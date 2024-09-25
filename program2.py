class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        
        return total

# Example usage with user input:
solution = Solution()
user_input = input("Enter a Roman numeral: ")
print(solution.romanToInt(user_input))
