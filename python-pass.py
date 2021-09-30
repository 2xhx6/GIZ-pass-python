

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        longest_palindrome = ''

        # If it's only one character, then return it.
        s_len = len(s)
        if s_len == 1:
            return s

        """
            We will make two loops, the outside loop will be a normal loop through the string, 
            and the inside loop will be a reverse loop, we will check if both slices 
            (the normal slice and the reverse one) match then it is the longest palindrome.
        """

        # Loop through the string
        for index in range(s_len):
            # Reverse loop through the string
            for reverse_index in range(s_len, index, -1):
                if len(longest_palindrome) >= len(s[index:reverse_index]):
                    break
                elif s[index:reverse_index] == s[index:reverse_index][::-1]:
                    longest_palindrome = s[index:reverse_index]
                    break
        return longest_palindrome


# Tests
print(Solution.longest_palindromic("babad"))
print(Solution.longest_palindromic("cbbd"))
print(Solution.longest_palindromic("a"))
print(Solution.longest_palindromic("ac"))
