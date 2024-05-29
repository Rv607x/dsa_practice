def palindrome(word: str):
    rev = ""
    for i in range(len(word)):
        rev = word[1:] + word[0]
    print(rev)

print(palindrome("wow"))
