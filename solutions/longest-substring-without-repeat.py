'''
3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class String:
    def length_of_longest_substring(self, s: str) -> int:
        return len(self.longest_substring(s))

    def longest_substring(self, s: str) -> str:
        longest_substring = str()
        for window_upper in range(0, len(s)+1):
            for window_lower in range(0, window_upper):
                string = s[window_lower:window_upper]
                if len(set(string)) == len(string):
                    if len(string) > len(longest_substring):
                        longest_substring = string
        return longest_substring


s = "pwwkew"
print(String().length_of_longest_substring(s))
