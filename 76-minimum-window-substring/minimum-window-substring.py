class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""

        required = {}

        for char in t:
            required[char] = required.get(char, 0) + 1

        window = {}
        left = 0
        formed = 0
        required_count = len(required)

        min_length = float("inf")
        min_left = 0
        min_right = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in required and window[char] == required[char]:
                formed += 1

            while left <= right and formed == required_count:

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right

                left_char = s[left]
                window[left_char] -= 1

                if left_char in required and window[left_char] < required[left_char]:
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_right + 1]