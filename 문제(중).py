def is_palindrome(s):
    s = s.lower()  # 모든 문자를 소문자로 변환
    s = ''.join(filter(str.isalnum, s))  # 알파벳과 숫자만 남김

    stack = list(s)  # 문자열을 스택에 넣음

    # 스택의 내용을 역순으로 확인하면서 원래 문자열과 비교
    for char in s:
        if char != stack.pop():
            return False

    return True

print(is_palindrome("eye"))  # True
print(is_palindrome("race car"))  # True
print(is_palindrome("I'm Adam"))  # False
print(is_palindrome("Hello"))  # False
