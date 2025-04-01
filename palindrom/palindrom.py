def is_palindrome(word):
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


print(is_palindrome("potop"))

