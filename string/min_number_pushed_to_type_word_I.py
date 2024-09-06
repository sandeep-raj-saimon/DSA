class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total = 0
        i = 1
        while (n > 0):
            if (n <  8):
                total += (i * n)
            else:
                total += 8 * i
            n = n - 8
            i += 1
        
        return total