class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value_mapping = {
            "I": [1,0],
            "V": [5,1],
            "X": [10,2],
            "L": [50,3],
            "C": [100,4],
            "D": [500,5],
            "M": [1000,6]
        }
        total = roman_value_mapping.get(s[0])[0]
        prev_total = 0
        for i in range(1,len(s)):
            value = roman_value_mapping.get(s[i])[0]
            prev_value = roman_value_mapping.get(s[i-1])[0]
            if (roman_value_mapping.get(s[i-1])[1] >= roman_value_mapping.get(s[i])[1]):
                total += value
            else:
                total = total - prev_value + (value  - prev_value)
        return total
