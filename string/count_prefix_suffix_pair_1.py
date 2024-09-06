class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        total = 0
        for i in range(len(words)-1):
            word = words[i]
            length = len(word)
            for j in range(i+1, len(words)):
                checkword = words[j]
                if len(word) > len(checkword):
                    pass
                elif (word == checkword[:length] and word == checkword[-length:]):
                    total+=1
                else:
                    pass
                
        return total