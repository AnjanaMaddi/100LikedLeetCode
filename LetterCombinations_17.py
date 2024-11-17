class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def iterate(list, d, index, c = ''):
            if index >= len(list):
                return [c]
            l = []
            for v in d[list[index]]:
                l += iterate(list, d, index+1, c+v)
            return l
        return iterate(digits, d, 0)
            
