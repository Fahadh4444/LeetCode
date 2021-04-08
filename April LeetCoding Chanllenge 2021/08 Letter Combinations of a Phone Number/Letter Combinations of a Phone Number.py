L = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}


def letterCombinations(digits: str):
    l = len(digits)
    ans = []
    if(digits == ""):
        return ans

    def BT(level: int, st: str):
        if(l == level):
            ans.append(st)
        else:
            letters = L[digits[level]]
            for letter in letters:
                BT(level+1, st+letter)
    BT(0, "")
    print(ans)


string = input("Enter string of NUmbers: ")
letterCombinations(string)
