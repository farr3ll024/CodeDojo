# Given an input string, determine whether or not it's a palindrome
def _palindromes(userinput):
    text = userinput.lower()
    return text == text[::-1]
